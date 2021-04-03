import cv2
import matplotlib.pyplot as plt

def sketch(image):
    img=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    G_img=cv2.GaussianBlur(img,(5,5),0)
    canny_img=cv2.Canny(G_img,10,70)
    ret,mask=cv2.threshold(canny_img,70,150,cv2.THRESH_BINARY)
    return mask

cap=cv2.VideoCapture(0)
while True:
    ret,frame=cap.read()
    cv2.imshow("live",sketch(frame))
    if cv2.waitKey(1)==13:
        break

cap.release()
cv2.destroyAllWindows()