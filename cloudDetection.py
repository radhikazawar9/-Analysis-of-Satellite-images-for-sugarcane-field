import cv2
import numpy as np
import pandas as pd

final = []
img = cv2.imread('5120-5120-TCI-2017-09-28.png', 1)
imgList = img.tolist()
final.append(imgList)
df = pd.DataFrame(final)
df.to_csv(r'C:\Users\radhi\Desktop\MyDatathon\oneImage.csv', index = None, header = False)

#hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

white = np.array([180, 180, 180])
lowerBound = np.array([0,0,0])

#mask = cv2.inRange(hsv, lowerBound, white)
"""
fgbg = cv2.BackgroundSubtractorMOG2(128,cv2.THRESH_BINARY,1)
masked_image = fgbg.apply(img)

#masked_image[masked_image==127]=0

cv2.imshow("shadow",masked_image)
"""
"""
range = np.array([76, 68, 65])
lowerBound1 = np.array([60,90,70])

mask1 = cv2.inRange(img, lowerBound1, range)
cv2.imshow("shadow",mask1)
"""
res = cv2.bitwise_and(img, img, mask=mask)

cv2.imwrite("new.png",res)

cv2.imshow("mywindow",res)

cv2.waitKey(0)
