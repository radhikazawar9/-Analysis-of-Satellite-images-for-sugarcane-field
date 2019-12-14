import cv2
import numpy as np
import pandas as pd

final = []
img = cv2.imread('5120-5120-TCI-2017-09-28.png', 1)

hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

white = np.array([180, 180, 180])
lowerBound = np.array([0,0,0])
mask = cv2.inRange(hsv, lowerBound, white)


cv2.imshow("mymask",mask)
res = cv2.bitwise_and(img, img, mask=mask)
cv2.imwrite("new1.png",res)

cv2.imshow("mywindow",res)

cv2.waitKey(0)
