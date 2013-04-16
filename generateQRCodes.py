#!/usr/bin/env python
#coding=utf-8
import sys, os

import re
from lib.pyqrcode.pyqrcode import *
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
    cursor.execute ("SELECT isbn13, qrLink FROM `books_purchased` WHERE 1 ORDER BY isbn ASC")
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
    qrLink = isbns[isbn]
    print isbn
    print qrLink

    qr_image = MakeQRImage(qrLink)
  #  qr_image = qr_code.make_image(block_in_pixels=50, border_in_blocks=0)
    qr_image.save('./images/qrcodes_gif/'  + isbn + '.gif', "GIF")

#    max width 384

conn.close ()