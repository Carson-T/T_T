import cv2 as cv
import numpy as np

img = cv.imread("C:\\Users\\tjt\\Desktop\\1.jpg")
img2 = cv.imread("C:\\Users\\tjt\\Desktop\\2.jpg")#读取图片，为BGR模式，不是RGB
img_ = img2[0:img.shape[0],0:img.shape[1]]  
print(img)   #打印图片的长宽和通道数组成的元组
cv.imshow("img",img)

source = cv.split(img) #拆分通道，返回列表
print(type(source))

g = img[:,:,1]  #截取整个绿色通道
cv.imshow("g",g)

img_black = np.zeros(img.shape[0:2],dtype = np.uint8)  #设置img1的size与img相等，单通道，且初始像素值为0
img_black[100:200,100:200] = 255  #设置区域内的像素值  
cv.imshow("img_black",img_black)

img_add = cv.add(img,img_,mask=img_black)  #两个同大小单通道的图像像素值相加，mask为掩膜
cv.imshow("img_add",img_add)

img_blend = cv.addWeighted(img,0.5,img_,0.1,0)  #addWeighted(img1,权重1,img2,权重2,常数)，img1*权重1+img2*权重2+常数
cv.imshow("img_blend",img_blend)


img_and = cv.bitwise_and(img,img_)  #按位和运算
img_or = cv.bitwise_or(img,img_)   #按位或运算
img_not = cv.bitwise_not(img)     #按位非运算
cv.imshow("ig_and",img_and)

lower = np.array([10,20,30])
upper = np.array([200,210,250])
img_mask = cv.inRange(img,lower,upper)   #两个像素值组成一个范围，img中所有大于最大值和小于最小值的点变为0，处于范围内的点变为255
cv.imshow("img_mask",img_mask)                #而对于多通道，必须每个通道值都要满足条件

img_hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow("img_hsv",img_hsv)

key = cv.waitKey(0)


