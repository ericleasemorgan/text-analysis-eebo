#!/usr/bin/env python

# make-everything.cgi - get list of identifiers from the reader and initialize a collection

# Eric Lease Morgan <emorgan@nd.edu>
# December 28, 2015 - first investigations
# December 31, 2015 - replace user-supplied title with computer generated title
# January 25, 2016  - moved created content in collections


# configure
ROOT        = '/var/www/html/eebo'
TMP         = 'tmp/'
URL         = 'https://kilgour.library.nd.edu/eebo/'
LENGTH      = 8
TEMPLATE    = '/var/www/html/eebo/etc/template-make-everything.txt'
COLLECTIONS = 'collections'

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

# create a unique name (key) for this collection; see http://stackoverflow.com/questions/2257441/random-string-generation-with-upper-case-letters-and-digits-in-python
name = os.environ[ 'REMOTE_USER' ] + '-' + ''.join( random.SystemRandom().choice( string.ascii_lowercase + string.digits ) for _ in range( LENGTH ) )

# save the identifiers to a file
identifiers_file = ROOT + '/' + TMP + 'identifiers-' + name + '.txt'
file = open( identifiers_file, 'w' )
file.write( identifiers )
file.close()

# define the log file
log_file = ROOT + '/' + TMP + 'log-' + name + '.txt'

# build the shell command
command = '( /bin/bash /var/www/html/eebo/bin/make-everything.sh ' + name + ' ' + identifiers_file + ' &> ' + log_file + ') &'

# do the work; Danger! Danger! Danger Will Robinson! Intruder alert! Danger! Danger!
os.system( command )

# define the URL of the (hopefully) newly created collection
url = URL + COLLECTIONS + '/' + name + '/'

# slurp up the template; sort of dumb but keeps all templates in one place
template = open( TEMPLATE, 'r' )
html     = template.read()
html     = html.replace( '##URL##',   url )
html     = html.replace( '##NAME##', name )

# done
print "Content-Type: text/html"
print 
print html
exit
