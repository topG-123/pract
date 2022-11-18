import cv2
img= cv2.imread('test.jpg')
print("size:",img.shape)
cv2.imshow ('Upsample',cv2.pyrUp(img))
cv2.imshow ('Downsample',cv2.pyrDown(img))
