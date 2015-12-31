#!/usr/bin/env python

# initialize-collection.cgi - a CGI front-end to make-everything.cgi

# Eric Lease Morgan <emorgan@nd.edu>
# December 31, 2015 - first cut


# configure
TEMPLATE = '/var/www/html/eebo/etc/template-initialize-collection.txt'

# slurp up the template; sort of dumb but keeps all templates in one place
template = open( TEMPLATE, 'r' )
html     = template.read()

# done
print "Content-Type: text/html"
print 
print html
exit

