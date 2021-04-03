import cv2
import numpy as np

img=cv2.imread("lena.jpg")
cv2.imshow("image",img)
cv2.waitKey(0)

blurrr=cv2.blur(img,(7,7))
cv2.imshow("image1",blurrr)
cv2.waitKey(0)

G_blurrr=cv2.GaussianBlur(img,(7,7),0)
cv2.imshow("image2",G_blurrr)
cv2.waitKey(0)


M_blurrr=cv2.medianBlur(img,5)
cv2.imshow("image3",M_blurrr)
cv2.waitKey(0)