import numpy as np
import matplotlib.pyplot as plt 
import cv2

img1 = cv2.imread('ashu2.jpeg',cv2.IMREAD_COLOR)
img1 = cv2.resize(img1,(350,350))

img2 = cv2.imread('ashu.jpg',cv2.IMREAD_COLOR)
img2 = cv2.resize(img2,(350,350))

#add = img1 + img2

#cv2.imshow('image1',img1)
#cv2.imshow('image2',img2)

rows,cols,channels = img2.shape

roi = img1[0:rows,0:cols]

img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

ret, mask = cv2.threshold(img2gray,220,255,cv2.THRESH_BINARY_INV)

mask_inv = cv2.bitwise_not(mask)

img2_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)

img1_fg = cv2.bitwise_and(img2,img2,mask = mask)

ds2 = cv2.add(img1_fg,img2_bg)

img1[0:rows,0:cols] = ds2
cv2.imshow('img',ds2)

#cv2.imshow('add',add)
cv2.waitKey(0)

cv2.destroyAllWindows()