#!/usr/bin/env python
#coding=utf-8
import sys, os
import Image, ImageDraw

from lib.pyqrcode.pyqrcode import *
from lib.pythermalprinter.printer import *

if len(sys.argv) == 2:
    url = sys.argv[1]
else:
    url = "http://www.timschwartz.org"

qr_image = MakeQRImage(url)
qr_image.show()
print "done making code"

serialport = ThermalPrinter.SERIALPORT
if not os.path.exists(serialport):
    sys.exit("ERROR: Serial port not found at: %s" % serialport)

p = ThermalPrinter(serialport=serialport)

print "printer initalized"
data = list(qr_image.getdata())
print "extracted data from image"
w, h = qr_image.size
print "got size info"
p.print_bitmap(data, w, h, True)
p.linefeed()
p.linefeed()
p.linefeed()
