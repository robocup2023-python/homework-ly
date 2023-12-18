#1.导入所需的库和模块
import cv2
import numpy as np
from matplotlib import pyplot as plt
#2.读取图像并将其转换为灰度图像
img = cv2.imread(r"C:\Users\sz\Desktop\dog222.jpeg",0)
#3.使用高斯滤波器平滑图像
blur = cv2.GaussianBlur(img,(5,5),0)
#4.计算图像中每个像素的梯度和方向
sobelx = cv2.Sobel(blur,cv2.CV_64F,1,0,ksize=3)
sobely = cv2.Sobel(blur,cv2.CV_64F,0,1,ksize=3)
gradmag = np.sqrt(sobelx**2 + sobely**2)
gradang = np.arctan2(sobely, sobelx) * 180 / np.pi
#5.对梯度方向进行四舍五入，并将其转换为整数
gradang = np.round(gradang / 45) * 45
gradang[gradang == 180] = -180
plt.figure(1)
plt.imshow(gradang,cmap="gray")
#6.使用非极大值抑制来消除非边缘像素
M, N = img.shape
Z = np.zeros((M,N), dtype=np.int32)
for i in range(1, M-1):
    for j in range(1, N-1):
        q = 255
        r = 255
        if gradang[i,j] == 0:
            q = gradmag[i, j+1]
            r = gradmag[i, j-1]
        elif gradang[i,j] == 45:
            q = gradmag[i+1, j-1]
            r = gradmag[i-1, j+1]
        elif gradang[i,j] == 90:
            q = gradmag[i+1, j]
            r = gradmag[i-1, j]
        elif gradang[i,j] == 135:
            q = gradmag[i-1, j-1]
            r = gradmag[i+1, j+1]
        if gradmag[i,j] >= q and gradmag[i,j] >= r:
            Z[i,j] = gradmag[i,j]
        else:
            Z[i,j] = 0
#7.使用双阈值来确定强边缘和弱边缘像素
high_threshold = 100
low_threshold = 50
M, N = Z.shape
res = np.zeros((M,N), dtype=np.int32)
weak = np.int32(25)
strong = np.int32(255)
strong_i, strong_j = np.where(Z >= high_threshold)
zeros_i, zeros_j = np.where(Z < low_threshold)
weak_i, weak_j = np.where((Z <= high_threshold) & (Z >= low_threshold))
res[strong_i, strong_j] = strong
res[weak_i, weak_j] = weak
plt.figure(2)
plt.imshow(Z,cmap="gray")
#8.使用连接弱边缘像素的方法来连接强边缘像素
M, N = res.shape
for i in range(1, M-1):
    for j in range(1, N-1):
        if res[i,j] == weak:
            if (res[i+1,j-1] == strong or res[i+1,j] == strong or res[i+1,j+1] == strong
                or res[i,j-1] == strong or res[i,j+1] == strong
                or res[i-1,j-1] == strong or res[i-1,j] == strong or res[i-1,j+1] == strong):
                res[i,j] = strong
            else:
                res[i,j] = 0
#9.显示最终结果
plt.figure(3)
plt.imshow(res, cmap='gray')
plt.show()