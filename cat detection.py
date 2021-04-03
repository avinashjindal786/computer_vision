
import cv2

img= cv2.imread("download (4).jpg")

gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cat_classifier=cv2.CascadeClassifier('C:/Users/karam chand/AppData/Local/Programs/Python/Python37/Lib/site-packages/cv2/data/haarcascade_frontalcatface_extended.xml')


face = cat_classifier.detectMultiScale(gray, 1.1,5,minSize=(75,75))

for x,y,w,h in face:
    print(x,w,y,h)
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),1)
    cv2.putText(img,"Cat # {}".format(len(face)),(x,y-10),cv2.FONT_HERSHEY_COMPLEX,0.55,(0,0,255),2)


print("face found", len(face))

cv2.imshow("face",img)
cv2.imshow("gray",gray)
cv2.waitKey(0)
cv2.destroyAllWindows()