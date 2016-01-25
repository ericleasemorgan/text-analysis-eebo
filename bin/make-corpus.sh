#!/bin/bash

# make-corpus.sh - given a list of identifiers and a keyword, cache EEBO content

# Eric Lease Morgan <emorgan@nd.edu>
# June  8, 2015    - first cut; based on HathiTrust efforts
# June 13, 2015    - migrated off everything but actual build to make-everything.sh
# June 14, 2015    - get files from GitHub instead of locally
# June 15, 2015    - migrated of the XSLT transform
# January 25, 2016 - moved mkdir stuff to separate make-structure.sh, moved created content in collections


# configure
CMD="/usr/bin/wget -t 1 -O xml/##OUTPUT## --no-check-certificate https://raw.githubusercontent.com/textcreationpartnership/##KEY##/master/##KEY##.xml"

# get input
NAME=$1

# sanity check; needs additional error checking
if [ -z $NAME ]; then

    echo "Usage: cat <identifiers> | $0 <name>"
    exit 1
    
fi

# change into the newly created collection
cd $NAME

# get and transform all the requested files
echo "getting files"
while read RECORD; do
	
	# get the identifier
	IDENTIFIER=$( echo "$RECORD" | cut -f1 )
	echo "  " $IDENTIFIER
	
	# check to see if the file was already retrieved
	if [ ! -f "$XML/$IDENTIFIER.xml" ]; then
	
		WGET=$( echo $CMD | sed "s/##KEY##/$IDENTIFIER/g")
		WGET=$( echo $WGET | sed "s/##OUTPUT##/$IDENTIFIER.xml/g")
		echo "  " $WGET
		$WGET
		
	fi
			
done

# finished
exit 0

