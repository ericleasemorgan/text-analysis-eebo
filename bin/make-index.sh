#!/bin/bash

# make-index.sh - create plain text and frequency files from the contents of a directory

# Eric Lease Morgan <emorgan@nd.edu>
# June 8, 2015     - first investigations; bases on HathiTrust work
# January 25, 2016 - moved created content in collections


# configure
HOME='/var/www/html/eebo'
COLLECTIONS='collections'
XML2FREQUENCY="$HOME/bin/make-index.py"

# get input
NAME=$1

# sanity check
if [ -z $NAME ]; then

    echo "Usage: $0 <name>"
    exit 1
    
fi

# process each xml file in the given directory
for FILE in $HOME/$COLLECTIONS/$NAME/xml/*.xml
do
    
    # parse out the KEY and echo
    KEY=$( basename $FILE .xml )
		
	# index
	if [ ! -f "$HOME/$COLLECTIONS/$NAME/index/$KEY.db" ]; then
	
		echo "  building $NAME/index/$KEY.db"
		cat $FILE | $XML2FREQUENCY -d > $HOME/$COLLECTIONS/$NAME/index/$KEY.db
	
	fi
	
	# create "book"
	if [ ! -f "$NAME/text/$KEY.txt" ]; then
	
		echo "  building $NAME/text/$KEY.txt"
		cat $FILE | $XML2FREQUENCY -b > $HOME/$COLLECTIONS/$NAME/text/$KEY.txt
		
	fi
		
done
