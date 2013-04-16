#!/usr/bin/env python
#coding=utf-8
import sys, os, re
import cgi
import MySQLdb

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
    cursor.execute ("SELECT preview, gTitle FROM `books_purchased` WHERE 1 ORDER BY isbn ASC")
    while (1):
        row = cursor.fetchone ()
        if row == None:
            break
        else:
            title = re.sub('[^A-Za-z0-9\ ]+', '', row[1])
            asciititle = title.decode('utf-8').encode('ascii', 'ignore')
            directory = 'blank_pages/'  + asciititle

            if not os.path.exists(directory):
                os.makedirs(directory)

            file_contents = '<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd"><plist version="1.0"><dict><key>URL</key><string>' + cgi.escape(row[0]) + '</string></dict></plist>'

            myFile = open(directory + "/" + asciititle + ".webloc", 'w')
            myFile.write(file_contents)
            myFile.close()

except MySQLdb.Error, e:
    print "Error %d: %s" % (e.args[0], e.args[1])
    sys.exit (1)

conn.close ()



