import cv2
noisy_img=cv2.imread('test.jpg',1)
cv2.imshow('Original Image',noisy_img)
size=5
denoise_img=cv2.medianBlur(noisy_img,size)
cv2.imshow('Denoised Image',denoise_img)
