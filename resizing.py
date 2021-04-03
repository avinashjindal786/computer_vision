import cv2
import numpy as np

img=cv2.imread("lena.jpg")
cv2.imshow("image",img)
cv2.waitKey(0)


im_scale=cv2.resize(img,None,fx=0.5,fy=0.5)
cv2.imshow("image1",im_scale)
cv2.waitKey(0)
cv2.destroyAllWindows()

im_scale1=cv2.resize(img,None,fx=2,fy=2,interpolation=cv2.INTER_CUBIC)
cv2.imshow("image11",im_scale1)
cv2.waitKey(0)
cv2.destroyAllWindows()

im_scale2=cv2.resize(img,(900,400),interpolation=cv2.INTER_AREA)
cv2.imshow("image12",im_scale2)
cv2.waitKey(0)
cv2.destroyAllWindows()