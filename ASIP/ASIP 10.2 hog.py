
import cv2
from skimage.feature import hog
ori=cv2.imread("test.jpg")
img=cv2.imread("test.jpg")
_,hog_image=hog(img,orientations=8,pixels_per_cell=(16,16),cells_per_block=(1,1),visualize=True,multichannel=True)
cv2.imshow("Original Image",ori)
cv2.imshow("HoG",hog_image)
cv2.imwrite("original.jpg",ori)
cv2.imwrite("HoG.jpg",hog_image)
