# 2d Histogram and BackProjection

import cv2
import numpy as np 
import matplotlib.pyplot as plt 

goalkeeper = cv2.imread('goalkeeper.jpg',1)
pitch = cv2.imread('pitch_ground.jpg',1)


pitch_hsv = cv2.cvtColor(pitch,cv2.COLOR_BGR2HSV)
goalkeeper_hsv = cv2.cvtColor(goalkeeper,cv2.COLOR_BGR2HSV)

roi_hist = cv2.calcHist([pitch_hsv],[0,1],None,[180,256],[0,180,0,256])

hue,sat,val = cv2.split(pitch_hsv)

mask = cv2.calcBackProject([goalkeeper_hsv],[0,1],roi_hist,[0,180,0,256],1)


kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
cv2.imshow('mask1',mask)



for k in kernel:
	print(k)
mask = cv2.filter2D(mask,-1,kernel)

_,mask = cv2.threshold(mask,70,255,cv2.THRESH_BINARY)

kernel1 = np.ones((5,5),np.uint8)
mask = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel1)



cv2.imshow('mask',mask)



mask = cv2.merge((mask,mask,mask))

result = cv2.bitwise_and(goalkeeper,mask)

cv2.imshow('result',result)
cv2.imshow('original',goalkeeper)




#plt.imshow(roi_hist)



#plt.show()


cv2.waitKey(0)

cv2.destroyAllWindows()
