import cv2
import numpy as np

img=cv2.imread("lena.jpg")

smaller=cv2.pyrDown(img)
larger=cv2.pyrUp(img)

cv2.imshow("image",img)
cv2.imshow("a",smaller)
cv2.imshow("s",larger)
cv2.waitKey(0)
cv2.destroyAllWindows()