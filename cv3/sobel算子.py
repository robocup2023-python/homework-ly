import cv2
import numpy as np
# 读取灰度图像
img = cv2.imread(r"C:\Users\sz\Desktop\dog222.jpeg",0)
# Sobel算子进行图像滤波
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)
sobel = cv2.addWeighted(sobelx, 0.5, sobely, 0.5, 0)
# 显示原始图像和Sobel算子滤波后的图像
cv2.imshow('Sobel Filtered Image', sobel)
cv2.waitKey(0)