#import Image
import os, sys
from PIL import Image
import numpy as np
import pandas as pd

"""
img  = Image.open('C:\\Users\\radhi\\Desktop\\MyDatathon\\mask-x6656-y7168.png')
img.save ('C:\\Users\\radhi\\Desktop\\MyDatathon\\mask-x6656-y7168.tiff')
print "done"

"""


#path = 'C:\\Users\\radhi\\Desktop\\MyDatathon\\B08'
path = 'C:\\Users\\radhi\\Desktop\\MyDatathon\\OneEachBand'
file = []
files = []

for r, d, f in os.walk(path):
    for file in f:
        if '.png' in file:
            files.append(os.path.join(r, file))

for f in files:
    img = Image.open(f)
    filename = '%s.tiff'%f
    img.save(filename)

print "completed"
