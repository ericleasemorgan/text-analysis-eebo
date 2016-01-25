#!/bin/bash

# make-structure.sh - given a name, create a set of directories

# Eric Lease Morgan <emorgan@nd.edu>
# January 25, 2016 - first cut


# get input
NAME=$1

# sanity check; needs additional error checking
if [ -z $NAME ]; then

    echo "Usage: $0 <name>"
    exit 1
    
fi

# build the directory structure
echo "creating directory structure"
if [ ! -d "$NAME" ];        then mkdir $NAME;        fi
if [ ! -d "$NAME/graphs" ]; then mkdir $NAME/graphs; fi
if [ ! -d "$NAME/html" ];   then mkdir $NAME/html;   fi
if [ ! -d "$NAME/index" ];  then mkdir $NAME/index;  fi
if [ ! -d "$NAME/pos" ];    then mkdir $NAME/pos;    fi
if [ ! -d "$NAME/text" ];   then mkdir $NAME/text;   fi
if [ ! -d "$NAME/xml" ];    then mkdir $NAME/xml;    fi

# finished
exit 0

