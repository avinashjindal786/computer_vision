
import cv2
import numpy as np

img=cv2.imread("lena.jpg")
cv2.imshow("image",img)
cv2.waitKey(0)

B,G,R=cv2.split(img)
#cv2.imwrite("len_copy.jpg",img)
print(img.shape)
print(B.shape)
print(G.shape)
print(R.shape)
zero=np.zeros(img.shape[:2],dtype="uint8")
print(zero.shape)
cv2.imshow("ss",zero)
cv2.imshow("red",cv2.merge([zero,zero,R]))
cv2.waitKey(0)
cv2.imshow("red5",cv2.merge([B,zero,zero]))
cv2.waitKey(0)
cv2.imshow("red56",cv2.merge([zero,G,zero]))
cv2.waitKey(0)
cv2.destroyAllWindows()
