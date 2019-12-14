import cv2
import numpy as np
import pandas as pd


final = []

img = cv2.imread('C:\\Users\\radhi\\Desktop\\MyDatathon\\NDVI ouput\\NDVI ouputndviImage.tiff',1)
cv2.imshow("image",img)
#print img.shape


mask = cv2.imread('C:\\Users\\radhi\\Desktop\\MyDatathon\\mask-x6656-y7168.tiff',1)

cv2.imshow("mask",mask)

lower_black = np.array([0,0,0], dtype = "uint16")
upper_black = np.array([0,0,0], dtype = "uint16")
black_mask = cv2.inRange(mask, lower_black, upper_black)
cv2.imshow('mask inverted',black_mask)
colored_black_mask = cv2.merge([black_mask,black_mask,black_mask])
print black_mask.shape
print colored_black_mask.shape
sugarcaneField = cv2.bitwise_and(img,colored_black_mask)
cv2.imshow('NDVIsugarcane',sugarcaneField)
cv2.imwrite("NDVIsugarcaneField.png",sugarcaneField )

cv2.waitKey(0)
