#!/usr/bin/env python
#coding=utf-8

from lib.pyqrcode.pyqrcode import *
from lib.pythermalprinter.printer import *
import Image, ImageDraw

qr_image = MakeQRImage("http://code.google.com/p/pyqrcode/")
#qr_image.show()

data = list(qr_image.getdata())
w, h = qr_image.size
p.print_bitmap(data, w, h)
