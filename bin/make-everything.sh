#!/bin/bash

# make-everything.sh - one script to rule them all

# Eric Lease Morgan <emorgan@nd.edu>
# June 13, 2015     - first cut; siphoned off build-corpus to another file
# June 15, 2015     - saved transform to a separate process
# December 31, 2015 - added call to update-db.sh
# January 18, 2016  - started adding creation of POS files
# January 25, 2016  - added make-structure.sh, linked logs, moved created content in collections


# configure
HTML='https://kilgour.library.nd.edu/eebo'
HOME='/var/www/html/eebo'
COLLECTIONS='collections'
TMP='tmp'

# get input
NAME=$1
IDENTIFIERS=$2

# sanity check; needs additional error checking
if [ -z $NAME -a -z $IDENTIFIERS ]; then

    echo "Usage: $0 <name> <identifiers>"
    exit 1
    
fi

# initialize
cd $HOME/$COLLECTIONS

# make directory structure
echo "making directories"
$HOME/bin/make-structure.sh $NAME

# link the log file, if possible
if [ -f "$HOME/$TMP/log-$NAME.txt" ]; then
	ln -s "$HOME/$TMP/log-$NAME.txt" "./$NAME/log.txt"
fi

# copy identifiers 
echo "caching identifiers"
cp $IDENTIFIERS "$NAME/identifiers.txt"

# build corpus
echo "building corpus"
cat "$HOME/$COLLECTIONS/$NAME/identifiers.txt" | "$HOME/bin/make-corpus.sh" $NAME

# transform TEI to HTML
echo "transforming TEI to HTML"
"$HOME/bin/transform-xml2html.sh" $NAME

# create the index
echo "making index"
"$HOME/bin/make-index.sh" $NAME

# create POS files
echo "making POS files"
"$HOME/bin/transform-xml2pos.sh" $NAME

# make dictionary
echo "making dictionary"
$HOME/bin/make-dictionary.py $HOME/$COLLECTIONS/$NAME/index/ > $HOME/$COLLECTIONS/$NAME/dictionary.db

# extract unique words
echo "extracting unique words"
cat $NAME/dictionary.db | ../bin/make-unique.py  > $NAME/unique.db

# create the catalog
echo "building catalog"
$HOME/bin/make-catalog.sh $NAME

# create sorted numeric reports
echo "creating numeric reports"
$HOME/bin/calculate-size.sh   $NAME                      | sort -k2 -n -r > $HOME/$COLLECTIONS/$NAME/sizes.db
$HOME/bin/calculate-themes.sh $NAME $HOME/etc/theme-colors.txt | sort -k2 -g -r > $HOME/$COLLECTIONS/$NAME/calculated-colors.db
$HOME/bin/calculate-themes.sh $NAME $HOME/etc/theme-names.txt  | sort -k2 -g -r > $HOME/$COLLECTIONS/$NAME/calculated-names.db
$HOME/bin/calculate-themes.sh $NAME $HOME/etc/theme-ideas.txt  | sort -k2 -g -r > $HOME/$COLLECTIONS/$NAME/calculated-ideas.db

# create reports, sorted by coefficient: colors, names, ideas
echo "calculating themes"
$HOME/bin/calculate-themes.py -v $HOME/$COLLECTIONS/$NAME/dictionary.db $HOME/etc/theme-colors.txt > $HOME/$COLLECTIONS/$NAME/dictionary-colors.db
$HOME/bin/calculate-themes.py -v $HOME/$COLLECTIONS/$NAME/dictionary.db $HOME/etc/theme-names.txt  > $HOME/$COLLECTIONS/$NAME/dictionary-names.db
$HOME/bin/calculate-themes.py -v $HOME/$COLLECTIONS/$NAME/dictionary.db $HOME/etc/theme-ideas.txt  > $HOME/$COLLECTIONS/$NAME/dictionary-ideas.db

# create charts; R needs to be installed
echo "making graphs"
$HOME/bin/make-graphs.sh $NAME

# analyze corpus and create pretty about page
echo "making about page"
$HOME/bin/make-about.sh $NAME > $NAME/about.db
$HOME/bin/transform-about2html.py $NAME > $NAME/about.html

# update list (database) of collections
echo "updating database"
$HOME/bin/update-db.sh $NAME

# all but done
echo "done -> $HTML/$COLLECTIONS/$NAME/"

# clean up
if [ -f "../$TMP/log-$NAME.txt" ]; then
	rm -rf "$NAME/log.txt"
	cp "../$TMP/log-$NAME.txt" "$NAME/log.txt"
fi

# quit
exit 0




