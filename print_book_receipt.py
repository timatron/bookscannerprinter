#!/usr/bin/env python
#coding=utf-8
import sys, os
import Image, ImageDraw

from lib.pyqrcode.pyqrcode import *
from lib.pythermalprinter.printer import *


if len(sys.argv) == 2:
     serialport = sys.argv[1]
else:
    serialport = ThermalPrinter.SERIALPORT

if not os.path.exists(serialport):
    sys.exit("ERROR: Serial port not found at: %s" % serialport)

print "Testing printer on port %s" % serialport
p = ThermalPrinter(serialport=serialport)


qr_image = MakeQRImage("http://code.google.com/p/pyqrcode/")
#qr_image.show()

data = list(qr_image.getdata())
w, h = qr_image.size
p.print_bitmap(data, w, h, True)

#p.print_text("\nHello maailma. How's it going?\n")
#p.print_text("Part of this ")
#p.bold_on()
#p.print_text("line is bold\n")
#p.bold_off()
#p.print_text("Part of this ")
#p.font_b_on()
#p.print_text("line is fontB\n")
#p.font_b_off()
#p.justify("R")
#p.print_text("right justified\n")
#p.justify("C")
#p.print_text("centered\n")
#p.justify() # justify("L") works too
#p.print_text("left justified\n")
#p.upsidedown_on()
#p.print_text("upside down\n")
#p.upsidedown_off()
#
#markup = """bl bold left
#ur underline right
#fc font b centred (next line blank)
#nl
#il inverse left
#"""
#p.print_markup(markup)
#
## runtime dependency on Python Imaging Library
#import Image, ImageDraw
#i = Image.open("example-lammas.png")
#data = list(i.getdata())
#w, h = i.size
#p.print_bitmap(data, w, h, True)
#p.linefeed()
#p.linefeed()
#p.linefeed()
