#!/usr/bin/env python
#coding=utf-8
import sys, os

import re
import barcode
import MySQLdb

from barcode.writer import ImageWriter

try:
    conn = MySQLdb.connect (host="localhost",
        unix_socket='/usr/local/var/mysql/Tims-MacBook-Pro.local.sock',
        user="root",
        passwd="",
        db="abebooks")
except MySQLdb.Error, e:
    print "Error %d: %s" % (e.args[0], e.args[1])
    sys.exit (1)

cursor = conn.cursor ()

isbns = {}
try:
    cursor.execute ("SELECT isbn13, gTitle FROM `books_purchased` WHERE 1 ORDER BY isbn ASC")
    while (1):
        row = cursor.fetchone ()
        if row == None:
            break
        else:
            isbns[row[0]] = row[1]

except MySQLdb.Error, e:
    print "Error %d: %s" % (e.args[0], e.args[1])
    sys.exit (1)

#print isbns

for isbn in isbns:
    title = isbns[isbn]
    print isbn
    print title


    if(len(isbn)) == 13:
        isbnBarcode = barcode.get_barcode('isbn13', str(isbn), writer=ImageWriter())
        isbnBarcode.get_fullcode()
    else:
        isbnBarcode = barcode.get_barcode('isbn', str(isbn), writer=ImageWriter())

#    title = re.sub('[^A-Za-z0-9\ ]+', '', title)
#    asciititle = title.decode('utf-8').encode('ascii', 'ignore')
#    print asciititle
    filename = isbnBarcode.save('../isbn_barcodes/'  + isbn )

conn.close ()