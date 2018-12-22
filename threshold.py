import numpy as np
import matplotlib.pyplot as plt 
import cv2

img = cv2.imread('bookpage.jpg',1)

grayscaled = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

retval,threshold = cv2.threshold(grayscaled,12,255,cv2.THRESH_BINARY)
gauss = cv2.adaptiveThreshold(grayscaled,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)
cv2.imshow('image',img)
cv2.imshow('threshold',threshold)
cv2.imshow('gauss',gauss)

cv2.waitKey(0)

cv2.destroyAllWindows()