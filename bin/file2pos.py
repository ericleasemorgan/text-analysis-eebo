#!/usr/bin/env python2

# file2pos.py - create a POS file

# Eric Lease Morgan <emorgan@nd.edu>
# December 15, 2014 - first cut; my fifth python program


# require
import nltk
import sys

# sanity check
if len( sys.argv ) != 2 :
  print "Usage:", sys.argv[ 0 ], "<file>"
  quit()
  
# read the input making sure it is unicode
text = unicode( open( sys.argv[ 1 ] ).read(), 'utf-8' )

# open, parse, and output the file
pos = ''
for tuple in nltk.pos_tag( nltk.word_tokenize( text ) ) : pos = pos + ' ' + tuple[ 0 ] + '/' + tuple[ 1 ]

# output as utf-8
print pos.encode( 'utf-8' )
