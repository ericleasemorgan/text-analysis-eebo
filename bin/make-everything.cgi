#!/usr/bin/env python

# make-everything.cgi - get list of identifiers from the reader and initialize a collection

# Eric Lease Morgan <emorgan@nd.edu>
# December 28, 2015 - first investigations
# December 31, 2015 - replace user-supplied title with computer generated title


# configure
ROOT        = '/var/www/html/eebo'
LOG         = 'tmp/log.txt'
IDENTIFIERS = 'tmp/identifiers.txt'
URL         = 'https://kilgour.library.nd.edu/eebo/'
LENGTH      = 8

# require
import cgi
import cgitb
import os
import random
import string

# initialize
cgitb.enable()
os.chdir( ROOT )

# read and parse the input of identifiers
input       = cgi.FieldStorage()
identifiers = input['identifiers'].value

# create a unique title (key) for this collection; see http://stackoverflow.com/questions/2257441/random-string-generation-with-upper-case-letters-and-digits-in-python
title = os.environ[ 'REMOTE_USER' ] + '-' + ''.join( random.SystemRandom().choice( string.ascii_lowercase + string.digits ) for _ in range( LENGTH ) )

# save the identifiers to a file
file = open( IDENTIFIERS, 'w' )
file.write( identifiers )
file.close()

# echo the input
print "Content-Type: text/plain"
print 
print title
print identifiers

# build the shell command
command = "/bin/bash ./bin/make-everything.sh " + title + ' ' + IDENTIFIERS + " &>" + LOG 
print command

# do the work; Danger! Danger! Danger Will Robinson! Intruder alert! Danger! Danger!
os.system( command )

# echo contents of the log file
with open( LOG, 'r' ) as input: print input.read()

# echo the location of the newly created collection
print URL + title

# done
exit
