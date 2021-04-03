import cv2
import numpy as np

img=cv2.imread("lena.jpg")
height,width=img.shape[:2]

rotation_matrix=cv2.getRotationMatrix2D((width/2,height/2),180,.7)
img_translate=cv2.warpAffine(img,rotation_matrix,(width,height))
cv2.imshow("translation",img_translate)
cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()