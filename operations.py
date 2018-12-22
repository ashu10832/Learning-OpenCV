import numpy as np
import matplotlib.pyplot as plt 
import cv2

img = cv2.imread('ashu2.jpeg',cv2.IMREAD_COLOR)
img = cv2.resize(img,(350,350))

print(img.shape)

img[50,50] = [0,0,0]


# Region Of Interest ROI
img[100:150,100:150] = [255,255,255]

face = img[100:200,100:200]
print(face.shape)

img[200:300,200:300] = face

cv2.imshow('image',img)

cv2.waitKey(0)

cv2.destroyAllWindows()