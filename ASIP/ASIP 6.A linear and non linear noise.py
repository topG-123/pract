import numpy as np
import cv2
from matplotlib import pyplot as plt
from PIL import Image,ImageFilter
image=cv2.imread('test.jpg')
image=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
figure_size=9
gauss=np.random.normal(0,1,image.size)
gauss=gauss.reshape(image.shape[0],image.shape[1],image.shape[2]).astype('uint8')
img_gauss=cv2.add(image,gauss)
new_image=cv2.GaussianBlur(image,(figure_size,figure_size),0)
plt.figure(figsize=(11,6))
plt.subplot(121)
plt.imshow(cv2.cvtColor(img_gauss,cv2.COLOR_HSV2RGB))
plt.title('Gaussian Noise')
plt.xticks([]),plt.yticks([])
plt.subplot(122),plt.imshow(cv2.cvtColor(new_image,cv2.COLOR_HSV2RGB)),plt.title('Gaussian Filter')
plt.xticks([]),plt.yticks([])
plt.show()
