import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
img = cv.imread(r"C:\Users\sz\Desktop\dog222.jpeg", 0)
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
rows,cols=img.shape
crow,ccrol=int(rows/2),int(cols/2)
fshift[crow-30:crow+30,ccrol-30:ccrol+30]=0
ishift=np.fft.ifftshift(fshift)
iimg=np.fft.ifft2(ishift)
iimg=np.abs(iimg)
plt.subplot(121), plt.imshow(img, cmap='gray')
plt.title('YuanZhao'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(iimg, cmap='gray')
plt.title('LvDingPinHouDeZhaoPian'), plt.xticks([]), plt.yticks([])
plt.show()
#   先学的是用numpy进行傅里叶变换，所以这里用的是numpy