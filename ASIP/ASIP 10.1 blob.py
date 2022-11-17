import cv2
import numpy as np

img=cv2.imread("test.jpg")

gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray_img=np.float32(gray_img)

dst=cv2.cornerHarris(gray_img,2,3,0.04)
dst=cv2.dilate(dst,None)

img[dst>0.01*dst.max()]=[0,0,255]
cv2.imshow("output",img)
cv2.waitKey(1)
cv2.imwrite("corner10.1_output,jpg",img)
