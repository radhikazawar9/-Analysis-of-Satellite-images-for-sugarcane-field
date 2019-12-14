import os, sys
from PIL import Image
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

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

x=1
y=1
final =[]
for f in files:
    img = Image.open(f)
    pix = img.load()
    final.append(pix[x,y])

df = pd.DataFrame(final)
#df = df.T
print df.shape
df.to_csv(r'C:\Users\radhi\Desktop\MyDatathon\onepixelTimeSeries_TCI.csv', index = None, header = False)

"""
box_data = [x,y,z]
plt.boxplot(box_data)
plt.show()

"""
plt.plot(df[[0]], color = 'blue')
plt.plot(df[[1]], color = 'green')
plt.plot(df[[2]], color = 'red')
plt.show()

TCI_dataframe = pd.read_csv("C:\\Users\\radhi\\Desktop\\MyDatathon\\OnepixelTransformed.csv",header = None)

plt.plot(TCI_dataframe[[0]], color = 'blue')
plt.plot(TCI_dataframe[[1]], color = 'green')
plt.plot(TCI_dataframe[[2]], color = 'red')
plt.show()


B04_dataframe = pd.read_csv("C:\\Users\\radhi\\Desktop\\MyDatathon\\pixelValue_B04.csv",header = None)

plt.plot(B04_dataframe[[0]], color = 'red')
plt.show()

B02_dataframe = pd.read_csv("C:\\Users\\radhi\\Desktop\\MyDatathon\\pixelValue_B02.csv",header = None)

plt.plot(B02_dataframe[[0]], color = 'blue')
plt.show()
