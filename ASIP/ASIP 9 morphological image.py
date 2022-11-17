import cv2 
import numpy as np 
image = cv2.imread('test.jpg') 
kernel = np.ones((5,5),np.uint8) 
erosion = cv2.erode(image,kernel,iterations=1) 
dilation = cv2.dilate(image,kernel,iterations=1) 
opening = cv2.morphologyEx(image,cv2.MORPH_OPEN,kernel) 
closing = cv2.morphologyEx(image,cv2.MORPH_CLOSE,kernel) 
gradient = cv2.morphologyEx(image,cv2.MORPH_GRADIENT,kernel) 
cv2.imshow('Original',image) 
cv2.imshow('erosion',erosion) 
cv2.imshow('dilation',dilation) 
cv2.imshow('opening',opening) 
cv2.imshow('closing',closing) 
cv2.imshow('gradient',gradient)
