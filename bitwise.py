import cv2
import numpy as np

square=np.zeros((300,300),np.uint8)
cv2.rectangle(square,(50,50),(250,250),(255,255,255),-1)
cv2.imshow("squre",square)
cv2.waitKey(0)

elli=np.zeros((300,300),np.uint8)
cv2.ellipse(elli,(150,150),(150,150),30,0,180,(255,255,255),-1)
cv2.imshow("squre",elli)
cv2.waitKey(0)

And=cv2.bitwise_and(square,elli)
cv2.imshow("And",And)
cv2.waitKey(0)

cv2.destroyAllWindows()