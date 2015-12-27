#!/bin/bash

# make-everything.cgi - CGI interface to make-everything.sh

# Eric Lease Morgan <emorgan@nd.edu>
# December 24, 2015 - first investigations
# December 27, 2015 - got it to work after sudo setsebool httpd_can_network_connect on "Thank you, Michael Berkowski!"


# configure
ROOT=/var/www/html/eebo
NAME=lute
IDENTIFIERS=etc/identifiers-lute.txt
LOG=tmp/log.txt

# initialize
cd $ROOT
rm -rf $LOG

# do the work
/bin/bash ./bin/make-everything.sh $NAME $IDENTIFIERS &>$LOG

# output the log file
echo "Content-type: text/plain"
echo
cat $LOG

# done
exit
