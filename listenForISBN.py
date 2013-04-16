#!/usr/bin/env python
#coding=utf-8
import sys, os
import Image, ImageDraw
import MySQLdb

from lib.pyqrcode.pyqrcode import *
from lib.pythermalprinter.printer import *


def linepad():
    p.linefeed()
    p.linefeed()
    p.linefeed()
    p.linefeed()	

def listen():
    isbn = raw_input("Enter ISBN to Search")

    try:
        conn = MySQLdb.connect (host="localhost",
            unix_socket='/var/run/mysqld/mysqld.sock',
            user="root",
            passwd="",
            db="abebooks")
    except MySQLdb.Error, e:
        print "Error %d: %s" % (e.args[0], e.args[1])
        sys.exit (1)

    cursor = conn.cursor ()
    cursor.execute ("SELECT gTitle, author, date, description, format, subject, qrLink FROM `books_purchased` WHERE isbn ='" + str(isbn) + "' OR isbn10 ='" + str(isbn) + "' OR isbn13 ='" + str(isbn) + "'")
    row = cursor.fetchone ()
    if row == None:
        print "No book found"

	p.print_text('Book not found.')
        
	#qr_image = MakeQRImage(url)
         #generate qr code for google books link with qr code
         #print "We dont have information on that book, but feel free to check it out online here:" + qrcode
    else:
        print "Book found"

	p.print_text('Book found. Printing...')	
	linepad()
	
        gTitle = row[0]
        author = row[1]
        date = row[2]
        description = row[3]
        format = row[4]
        subject = row[5]
        qrLink = row[6]

        im = Image.open("./images/qrcodes_bmp/" + str(isbn) + ".bmp")
	data = list(im.getdata())
	p.print_bitmap(data,384,384,True)
	p.linefeed();
	p.print_text(gTitle)
	p.linefeed()
	p.linefeed()
	p.print_text(author)
	p.linefeed()
	p.linefeed()
	p.print_text(date + '\n' + format + '\n' + subject ) 
	p.linefeed()
	p.linefeed()
	p.linefeed()
	p.print_text('Materials On Reserve'  + '\n' + 'Victoria H. Myhren Gallery'  + '\n' + 'Through May 5, 2013' )
	linepad()
	linepad()
	
        print description
         #check to see if qr code exists
         #print out the data

    conn.close ()
    listen()


serialport = ThermalPrinter.SERIALPORT
if not os.path.exists(serialport):
    sys.exit("ERROR: Serial port not found at: %s" % serialport)
p = ThermalPrinter(serialport=serialport)

listen()


#print "printer initalized"
#data = list(qr_image.getdata())
#print "extracted data from image"
#w, h = qr_image.size
#print "got size info"
#p.print_bitmap(data, w, h, True)
#p.linefeed()
#p.linefeed()
#p.linefeed()
