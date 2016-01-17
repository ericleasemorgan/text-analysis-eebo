#!/usr/bin/env python

# xml2text.py - create a readable plain text file from TEI/XML

# Eric Lease Morgan <emorgan@nd.edu>
# January 17, 2016 - first investigations


# require
import sys
import libxml2

# sanity check
if ( len( sys.argv ) != 1 ) | ( sys.stdin.isatty() ) :
	print "Usage: cat <xml> |", sys.argv[ 0 ]
	quit()

# create an xpath parser with an xml file
xml     = sys.stdin.read()
tei     = libxml2.parseMemory( xml, len( xml ) )
context = tei.xpathNewContext()
context.xpathRegisterNs( 't', 'http://www.tei-c.org/ns/1.0' )

# parse, output, and done; simple, rudimentary, and zero normalization!
print context.xpathEval( '/t:TEI/t:text' )[ 0 ].content
quit()


