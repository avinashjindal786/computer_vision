
import cv2

img= cv2.imread("bill gates.jpg")

gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

face_classifier=cv2.CascadeClassifier('C:/Users/karam chand/AppData/Local/Programs/Python/Python37/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')
eye_classifier=cv2.CascadeClassifier('C:/Users/karam chand/AppData/Local/Programs/Python/Python37/Lib/site-packages/cv2/data/haarcascade_eye_tree_eyeglasses.xml')

face = face_classifier.detectMultiScale(gray, 1.1, 5)
eye = eye_classifier.detectMultiScale(gray,1.1,5)
for x,y,w,h in face:
    print(x,w,y,h)
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),5)

for ex,ey,ew,eh in eye:
    print(ex,ey,ew,eh)
    cv2.rectangle(img,(ex,ey),(ex+ew,ey+eh),(0,0,255),3)

print("face found", len(face))
print("eye",len(eye))
cv2.imshow("face",img)
cv2.imshow("gray",gray)
cv2.waitKey(0)
cv2.destroyAllWindows()