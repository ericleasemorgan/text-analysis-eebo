#!/bin/bash

# make-graphs.sh - assuming R (and all of its friends) is installed, create some charts

# Eric Lease Morgan <emorgan@nd.edu>
# May 30, 2015     - first cut; brain dead
# June 2, 2015     - added sanity checking
# June 4, 2015     - added graph-catalog.R (creeping featuritis!)
# January 25, 2016 - moved created content in collections


# configure
HOME='/var/www/html/eebo'
COLLECTIONS='collections'

# get input
NAME=$1

# sanity check
if [ -z $NAME ]; then

    echo "Usage: $0 <name>"
    exit 1
    
fi

# make things relative
cd $HOME/$COLLECTIONS

# do the work
echo "graphing clusters"
$HOME/bin/graph-cluster.R $NAME

echo "graphing wordclouds"
$HOME/bin/graph-wordcloud.R $NAME

echo "graphing catalog"
$HOME/bin/graph-catalog.R $NAME

# done
exit 0


