import cv2
import numpy as np
img=cv2.imread(r"C:\Users\sz\Desktop\dog222.jpeg",0)
dst = cv2.cornerHarris(img,blockSize= 2,ksize= 3,k= 0.04)
def corner_nms(corner,kernal=3):
	out = corner.copy()
	row_s = int(kernal/2)
	row_e = out.shape[0] - int(kernal/2)
	col_s,col_e = int(kernal/2),out.shape[1] - int(kernal/2)
	for r in range(row_s,row_e):
		for c in range(col_s,col_e):
			if corner[r,c]==0: #不是可能的角点
				continue
			zone = corner[r-int(kernal/2):r+int(kernal/2)+1,c-int(kernal/2):c+int(kernal/2)+1]
			index = corner[r,c]<zone
			(x,y) = np.where(index==True)
			if len(x)>0 : #说明corner[r,c]不是最大，直接归零将其抑制
				out[r,c] = 0
	return out
	#nms
score_nms = corner_nms(img)
img_show3 = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
img_show3[score_nms != 0] =  (0,0,255)
cv2.imwrite('corners-nms.jpg',img_show3)
cv2.waitKey(0)