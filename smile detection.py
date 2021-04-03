
import cv2

img= cv2.imread("obama.jpg")

gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


body_classifier=cv2.CascadeClassifier('C:/Users/karam chand/AppData/Local/Programs/Python/Python37/Lib/site-packages/cv2/data/haarcascade_smile.xml')

face_classifier=cv2.CascadeClassifier('C:/Users/karam chand/AppData/Local/Programs/Python/Python37/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')

face = face_classifier.detectMultiScale(gray, 1.3, 5)


body = body_classifier.detectMultiScale(gray, 1.3,10)

for x,y,w,h in face:
    print(x,w,y,h)
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),1)
    for sx,sy,sw,sh in body:
        print(sx,sw,sy,sh)
        cv2.rectangle(img,(sx,sy),(sx+sw,sy+sh),(0,0,255),5)

print("face found", len(body))


cv2.imshow("face",img)
cv2.imshow("gray",gray)
cv2.waitKey(0)
cv2.destroyAllWindows()