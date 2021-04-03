import cv2
import numpy as np

windowName="drawing"

img=np.zeros((512,512,3),np.uint8)
cv2.namedWindow(windowName)

def draw_circle(event,x,y,flags,prim):
    if event==cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),48,(0,255,0),-1)

    if event==cv2.EVENT_MBUTTONDOWN:
        cv2.circle(img,(x,y),20,(0,0,255),-1)

    if event==cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img,(x,y),30,(255,00,0),-1)

cv2.setMouseCallback(windowName,draw_circle)
while True:
    cv2.imshow(windowName,img)
    if cv2.waitKey(1)==13:
        break

cv2.destroyWindow()
