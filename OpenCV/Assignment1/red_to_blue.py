import cv2 
import numpy as np
from matplotlib import pyplot as plt


src = cv2.imread('wallpaper.jpg', cv2.IMREAD_UNCHANGED)

img = np.zeros(src.shape)

img[:,:,0] = src[:,:,0]
img[:,:,1] = src[:,:,1]
img[:,:,2] = src[:,:,0]

plt.imshow(img)
plt.show()
