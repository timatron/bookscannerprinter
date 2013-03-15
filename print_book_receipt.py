#!/usr/bin/env python
#coding=utf-8
import sys, os
import Image, ImageDraw

from lib.pyqrcode.pyqrcode import *
from lib.pythermalprinter.printer import *

qr_image = MakeQRImage("http://www.timschwartz.org")
qr_image.show()

#if len(sys.argv) == 2:
#     serialport = sys.argv[1]
#else:
#    serialport = ThermalPrinter.SERIALPORT
#
#if not os.path.exists(serialport):
#    sys.exit("ERROR: Serial port not found at: %s" % serialport)

print "Testing printer on port %s" % serialport
p = ThermalPrinter(serialport=serialport)

#
#data = list(qr_image.getdata())
#w, h = qr_image.size
#p.print_bitmap(data, w, h, True)
#p.linefeed()
#p.linefeed()
#p.linefeed()
