import cv2
import numpy as np
import matplotlib.pyplot as plt
import time
timestr = time.strftime("%Y%m%d_%H%M")
print(timestr)
image = cv2.imread('test.jpg')
c = 255 / np.log(1 + np.max(image))
log_image = c * (np.log(image + 1))
log_image = np.array(log_image, dtype = np.uint8)
plt.imshow(image)
plt.savefig('Original'+timestr+'.png')
plt.show()
plt.imshow(log_image)
plt.savefig('Log_trans'+timestr+'png')
plt.show()
