import cv2
import numpy as np
import matplotlib.pyplot as plt
import time
timestr = time.strftime("%Y%m%d_%H%M")
print(timestr)
img = cv2.imread("test.jpg")
for gamma in [0.1, 0.5, 1.2, 2.2]:
 gamma_corrected = np.array(255*(img / 255) ** gamma, dtype = 'uint8')
cv2.imwrite('gamma_transformed' + timestr + ' ' + str(gamma) + '.jpg', gamma_corrected)

plt.imshow(img)
plt.savefig('Original'+timestr+'.png')
plt.show()
plt.imshow(img)
plt.savefig('Power_trans'+timestr+'png')
plt.show()
