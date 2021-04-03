import cv2
import matplotlib.pyplot as plt
import numpy as np

cap=cv2.VideoCapture(0)
while True:
    ret,frame=cap.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lower=np.array([110,50,50])
    upper=np.array([130,255,255])
    mask=cv2.inRange(hsv,lower,upper)
    result=cv2.bitwise_and(frame,frame,mask=mask)
    cv2.imshow("rea",result)
    cv2.imshow("live",frame)
    cv2.imshow("live1", mask)
    if cv2.waitKey(1)==13:
        break
cap.release()
cv2.destroyAllWindows()