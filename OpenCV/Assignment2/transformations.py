import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('img.jpg')
rows,cols,channels = image.shape

translation1 = np.float32([[1,0,50],[0,1,50]])
translation2 = np.float32([[1,0,-50],[0,1,-50]])
translation3 = np.float32([[1,0,25],[0,1,50]])
translation4 = np.float32([[1,0,-25],[0,1,50]])
rotation1 = cv2.getRotationMatrix2D((cols/2,rows/2),90,1) 
rotation2 = cv2.getRotationMatrix2D((cols/2,rows/2),45,1)
rotation3 = cv2.getRotationMatrix2D((cols/2,rows/2),-90,1)
rotation4 = cv2.getRotationMatrix2D((cols/2,rows/2),-45,1)
blur1 = cv2.GaussianBlur(image,(5,5),0)
blur2 = cv2.medianBlur(image,5)

i1 = cv2.warpAffine(image,translation1,(cols,rows))
i2 = cv2.warpAffine(image,translation2,(cols,rows))
i3 = cv2.warpAffine(image,translation3,(cols,rows))
i4 = cv2.warpAffine(image,translation4,(cols,rows))
i5 = cv2.warpAffine(image,rotation1,(cols,rows))
i6 = cv2.warpAffine(image,rotation2,(cols,rows))
i7 = cv2.warpAffine(image,rotation3,(cols,rows))
i8 = cv2.warpAffine(image,rotation4,(cols,rows))

fig, axs = plt.subplots(2, 5)
axs[0,0].imshow(cv2.cvtColor(i1,cv2.COLOR_BGR2RGB))
axs[0,1].imshow(cv2.cvtColor(i2,cv2.COLOR_BGR2RGB))
axs[0,2].imshow(cv2.cvtColor(i3,cv2.COLOR_BGR2RGB))
axs[0,3].imshow(cv2.cvtColor(i4,cv2.COLOR_BGR2RGB))
axs[0,4].imshow(cv2.cvtColor(i5,cv2.COLOR_BGR2RGB))
axs[1,0].imshow(cv2.cvtColor(i6,cv2.COLOR_BGR2RGB))
axs[1,1].imshow(cv2.cvtColor(i7,cv2.COLOR_BGR2RGB))
axs[1,2].imshow(cv2.cvtColor(i8,cv2.COLOR_BGR2RGB))
axs[1,3].imshow(cv2.cvtColor(blur1,cv2.COLOR_BGR2RGB))
axs[1,4].imshow(cv2.cvtColor(blur2,cv2.COLOR_BGR2RGB))
plt.show()
