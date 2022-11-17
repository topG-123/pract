import cv2
img=cv2.imread('test.jpg')
ddepth=cv2.CV_16S
kernel_size=3
red_Noise=cv2.GaussianBlur(img,(3,3),0)
gray=cv2.cvtColor(red_Noise,cv2.COLOR_BGR2GRAY)
dst=cv2.Laplacian(gray,ddepth,ksize=kernel_size)
abs_dst=cv2.convertScaleAbs(dst)
cv2.imshow('Laplacian image',abs_dst)
