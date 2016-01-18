#!/bin/bash

# transform-xml2pos.sh - batch file to make POS files from TEI/XML

# Eric Lease Morgan <emorgan@nd.edu>
# January 18, 2016 - first cut


# configure
FILE2POS=./bin/file2pos.py
POS='pos'
XML2TEXT=./bin/xml2text.py

# get input
NAME=$1

# sanity check
if [ -z $NAME ]; then

    echo "Usage: $0 <name>"
    exit 1
    
fi

# process each xml file in the given directory
for FILE in $NAME/xml/*.xml
do
    
    # parse out the KEY and echo
    KEY=$( basename $FILE .xml )
			
	# create POS file
	if [ ! -f "$NAME/pos/$KEY.pos" ]; then
	
		echo "building $NAME/pos/$KEY.pos"
		cat $FILE | $XML2TEXT | $FILE2POS > $NAME/$POS/$KEY.pos
		
	fi
	
done
