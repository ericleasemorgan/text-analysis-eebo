#!/usr/bin/env python2

# summarize-pos.py - output POS frequencies in a previously created POS file

# Eric Lease Morgan <emorgan@nd.edu>
# December 15, 2014 - first cut; my seventh python program
# January 25, 2016  - moved created content in collections


# require
import nltk
import sys
from nltk.tag import pos_tag, map_tag

# sanity check
if len( sys.argv ) != 2 :
  print "Usage:", sys.argv[ 0 ], "<file>"
  quit()
  
# get input
FILE = sys.argv[ 1 ]

# open and normalize a previously created POS file
pos = [ nltk.tag.str2tuple( tuple ) for tuple in open( FILE ).read().split() ]
pos = [ ( word.lower(), map_tag( 'en-ptb', 'universal', tag ) ) for word, tag in pos ]

# output the frequency
for tuple in nltk.FreqDist( tag for ( word, tag ) in pos ).most_common():
	print tuple[ 0 ] + '\t' + str( tuple[ 1 ] )

