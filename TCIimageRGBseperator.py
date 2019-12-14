import os, sys
from PIL import Image
import numpy as np
import pandas as pd

TCI_dataframe = pd.read_csv("C:\\Users\\radhi\\Desktop\\MyDatathon\\pixelValue_TCI.csv",header = None)

newdf = df[TCI_dataframe.columns[0:3]]
print newdf.shape

newdf.to_csv(r'C:\Users\radhi\Desktop\MyDatathon\onepixelTimeSeries_TCI.csv', index = None, header = False)

"""finalRed = []
dfRed = []
for i in range (0, 393216, 3):
    finalRed.append(TCI_dataframe[i])

finalGreen = []
dfGreen = []
for i in range (1, 393216, 3):
    finalGreen.append(TCI_dataframe[i])

finalBlue = []
dfBlue = []
for i in range (2, 393216, 3):
    finalBlue.append(TCI_dataframe[i])

dfred = pd.DataFrame(finalRed)
dfRed.to_csv(r'C:\Users\radhi\Desktop\MyDatathon\red.csv',index = None, header = False)

dfGreen = pd.DataFrame(finalGreen)
dfGreen.to_csv(r'C:\Users\radhi\Desktop\MyDatathon\green.csv',index = None, header = False)

dfBlue = pd.DataFrame(finalBlue)
dfBlue.to_csv(r'C:\Users\radhi\Desktop\MyDatathon\blue.csv',index = None, header = False)
"""

"""df = pd.DataFrame([[1,1,1,1,1,6],[3,4,5,6,7,5],[2,2,2,2,2,5],[3,3,3,3,3,5],[5,5,5,5,5,5]])
#print df.shape
final1 = []
d1= []
for i in range(0,6,3):
    final1.append(df[i])

final2 = []
d2 = []
for i in range(1,6,3):
    final2.append(df[i])

final3 = []
d3 = []
for i in range(2,6,3):
    final3.append(df[i])"""
