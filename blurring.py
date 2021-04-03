import cv2
import numpy as np

img=cv2.imread("lena.jpg")
cv2.imshow("image",img)
cv2.waitKey(0)


kernal=np.ones((3,3),np.float32)/9

blurred=cv2.filter2D(img,-1,kernal)
cv2.imshow("imgabi",blurred)
cv2.waitKey(0)

cv2.destroyAllWindows()