
import cv2
import numpy as np

img=cv2.imread("lena.jpg")

cv2.imshow("image",img)
cv2.waitKey(0)
#M=np.ones(img.shape,dtype="uint8")*150
M=np.zeros(img.shape,dtype="uint8")+150
print(M)
added=cv2.add(img,M)
cv2.imshow("add",added)
cv2.waitKey(0)
subracted=cv2.subtract(img,M)
cv2.imshow("sub",subracted)
cv2.waitKey(0)
multi=cv2.multiply(img,M)
cv2.imshow("multy",multi)
cv2.waitKey(0)

cv2.destroyAllWindows()