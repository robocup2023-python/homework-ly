import cv2
import numpy as np
# 读取图像
img = cv2.imread(r"C:\Users\sz\Desktop\dog222.jpeg", 0)
# 计算直方图
hist = cv2.calcHist([img], [0], None, [256], [0, 256])
# 进行直方图均衡化
equ = np.zeros_like(hist)
for i in range(256):
    hist_i = hist[i]
    min_i = np.min(hist)
    max_i = np.max(hist)
    if min_i < max_i:
        equ[i] = min_i + (hist_i - min_i) / (max_i - min_i) * (255 - equ[i])
# 显示均衡化后的图像
cv2.imwrite('Equalized.jpg', equ)
cv2.waitKey(0)