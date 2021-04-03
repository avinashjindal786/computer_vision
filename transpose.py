import cv2
import numpy as np

img=cv2.imread("lena.jpg")

rotated=cv2.transpose(img)
cv2.imshow("translation",rotated)
cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()