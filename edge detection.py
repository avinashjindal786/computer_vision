import cv2
import numpy as np

img=cv2.imread("lena.jpg",0)
height,width=img.shape[:2]

sobel_x=cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
sobel_y=cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)

cv2.imshow("ori",img)
cv2.waitKey(0)

cv2.imshow("ori1",sobel_x)
cv2.waitKey(0)

cv2.imshow("ori2",sobel_y)
cv2.waitKey(0)

laplaction=cv2.Laplacian(img,cv2.CV_64F)
cv2.imshow("ori23",laplaction)
cv2.waitKey(0)

canny=cv2.Canny(img,120,170)
cv2.imshow("ori234",canny)
cv2.waitKey(0)