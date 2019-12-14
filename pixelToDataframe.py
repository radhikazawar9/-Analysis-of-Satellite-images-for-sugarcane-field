import os, sys
from PIL import Image
import numpy as np
import pandas as pd

#path = 'C:\\Users\\radhi\\Desktop\\MyDatathon\\B02'
#path = 'C:\\Users\\radhi\\Desktop\\MyDatathon\\B03'
#path = 'C:\\Users\\radhi\\Desktop\\MyDatathon\\B04'
path = 'C:\\Users\\radhi\\Desktop\\MyDatathon\\TCI'

file = []
files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.png' in file:
            files.append(os.path.join(r, file))

row_as_list = []
final = []
for f in files:
    img = Image.open(f)
    img_converted = np.array(img)
    row = img_converted.ravel()
    row_as_list = row.tolist()
    final.append(row_as_list)

df = pd.DataFrame(final)
print df.shape


#df.to_csv(r'C:\Users\radhi\Desktop\MyDatathon\pixelValue_B02.csv', index = None, header = False)
#df.to_csv(r'C:\Users\radhi\Desktop\MyDatathon\pixelValue_B03.csv', index = None, header = False)
#df.to_csv(r'C:\Users\radhi\Desktop\MyDatathon\pixelValue_B04.csv', index = None, header = False)
df.to_csv(r'C:\Users\radhi\Desktop\MyDatathon\pixelValue_TCI.csv', index = None, header = False)

print "Task completed"
