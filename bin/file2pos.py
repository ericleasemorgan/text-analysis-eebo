#!/usr/bin/env python2

# file2pos.py - create a POS file

# Eric Lease Morgan <emorgan@nd.edu>
# December 15, 2014 - first cut; my fifth python program
# January 17, 2016  - encoded the input & output as UTF-8


# require
import nltk
import sys

# sanity check
if ( len( sys.argv ) != 1 ) | ( sys.stdin.isatty() ) :
	print "Usage: cat <xml> |", sys.argv[ 0 ]
	quit()
  
# read the input making sure it is unicode
text = unicode( sys.stdin.read(), 'utf-8' )

# open, parse, and output the file
pos = ''
for tuple in nltk.pos_tag( nltk.word_tokenize( text ) ) : pos = pos + ' ' + tuple[ 0 ] + '/' + tuple[ 1 ]

# output as utf-8
print pos.encode( 'utf-8' )
