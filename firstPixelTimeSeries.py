import os, sys
from PIL import Image

x=310
y=110

im1 = Image.open("5120-5120-TCI-2017-09-28.png")

pix1 = im1.load()
print pix1[x,y]

"""im1 = Image.open("2048-1536-TCI-2017-05-11.png")
x = 1
y = 1

pix1 = im1.load()
print pix1[x,y]

im2 = Image.open("2048-1536-B02-2019-05-11.png")
x = 1
y = 1

pix2 = im2.load()
print pix2[x,y]

im3 = Image.open("2048-1536-B03-2017-05-11.png")
x = 1
y = 1

pix3 = im3.load()
print pix3[x,y]

im4 = Image.open("2048-1536-B04-2017-05-11.png")
x = 1
y = 1

pix4 = im4.load()
print pix4[x,y]"""
