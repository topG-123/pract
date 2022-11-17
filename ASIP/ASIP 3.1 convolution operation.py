import cv2
import numpy as np
image = cv2.imread('test.jpg')
blur_kernel=np.ones((5,5), np.float32)/25
img=cv2.filter2D(src=image, ddepth=-1, kernel=blur_kernel)
sharp_kernel=np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
sharp_img = cv2.filter2D(src=image, ddepth=-1, kernel=sharp_kernel)
cv2.imshow('original',image)
cv2.imshow('sharpened',sharp_img)
cv2.imshow('kernel blur', img)
cv2.imwrite('sharp_image.jpg',sharp_img)
cv2.imwrite('blur_kernel.jpg',img)
cv2.waitKey()
cv2.destroyAllWindows()
