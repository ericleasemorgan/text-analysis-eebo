#!/usr/bin/env python2

# pos.py - output desired POS and their frequencies

# Eric Lease Morgan <emorgan@nd.edu>
# December 15, 2014 - first cut; my sixth python program


# require
import nltk
import sys
from nltk.tag import pos_tag, map_tag

# sanity check
if len( sys.argv ) != 4 :
  print "Usage:", sys.argv[ 0 ], "<file> <NOUN|PRON|VERB|ADJ> <maximum>"
  quit()
  
# get input
FILE    = sys.argv[ 1 ]
POS     = sys.argv[ 2 ]
MAXIMUM = int( sys.argv[ 3 ] )

# open and normalize (simplify) a previously created POS file
pos = [ nltk.tag.str2tuple( tuple ) for tuple in open( FILE ).read().split() ]
pos = [ ( word.lower(), map_tag( 'en-ptb', 'universal', tag ) ) for word, tag in pos ]

# extract the desired POS words
words = [ tuple[ 0 ] for tuple in pos if tuple[ 1 ] == POS ]

# loop through the words and output the results; done
for tuple in nltk.FreqDist( words ).most_common( MAXIMUM ) :
	print tuple[ 0 ] + '\t' + str( tuple[ 1 ] )