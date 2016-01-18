#!/usr/bin/env python2

# ngrams.py - parse a file into ngrams and output their frequency

# Eric Lease Morgan <emorgan@nd.edu>
# December 15, 2014 - first cut; my fourth python program
# January 18, 2016  - started using unicode


# require
import nltk
import string
import sys
from nltk.corpus import stopwords
from nltk.util   import ngrams

# sanity check
if len( sys.argv ) != 4 :
  print "Usage:", sys.argv[ 0 ], "<file> <size> <maximum>"
  quit()
  
# get input
file    = sys.argv[ 1 ]
size    = int( sys.argv[ 2 ] )
maximum = int( sys.argv[ 3 ] )

# read the file as unicode
text = unicode( open( file ).read(), 'utf-8' )

# open, parse, and normalize the tokens (words) in the file
tokens = nltk.word_tokenize( text )
tokens = [ token.lower() for token in tokens ]
tokens = [ ''.join( character for character in token if character not in string.punctuation ) for token in tokens ]
tokens = [ token for token in tokens if token.isalpha() ]
tokens = [ token for token in tokens if not token in stopwords.words( 'english' ) ]
tokens = [ token for token in tokens if token ]

# output maximum most frequent ngrams and their counts
for tuple in nltk.FreqDist( ngrams( tokens, size ) ).most_common( maximum ):
	count = int( tuple[ 1 ] )
	if count == 1 : break
	phrase = ' '.join( word.encode( 'utf-8' ) for word in tuple[ 0 ] )
	print phrase + "\t" + str( count )
