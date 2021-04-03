import cv2
import numpy as np

img=cv2.imread("lena.jpg")
height,width=img.shape[:2]

q_h,q_w=height/6,width/6

print(q_h)
print(q_w)
t=np.float32([[1,0,q_w],[0,1,q_h]])
print(t)
img_translate=cv2.warpAffine(img,t,(width,height))
cv2.imshow("translation",img_translate)
cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()