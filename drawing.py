import numpy as np
import matplotlib.pyplot as plt 
import cv2

img = cv2.imread('ashu2.jpeg',1)
small = cv2.resize(img,(0,0),fx = 0.2,fy = 0.2)

cv2.line(small,(0,0), (150,150 ) , (255,0,0) , 15)

cv2.rectangle(small,(15,25),(200,150),(255,124,243),5)

pts = np.array([[10,5],[20,30],[70,20],[50,10]],np.int32)

cv2.polylines(small,[pts],True,(0,0,0),3)

font = cv2.FONT_HERSHEY_SIMPLEX

cv2.putText(small,'This is me!',(0,130),font,1,(200,200,200),2,cv2.LINE_AA)


cv2.imshow('image',small)

cv2.waitKey(0)

cv2.destroyAllWindows()