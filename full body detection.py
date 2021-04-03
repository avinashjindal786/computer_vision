
import cv2

img= cv2.imread("avii11.jpg")

gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


body_classifier=cv2.CascadeClassifier('C:/Users/karam chand/AppData/Local/Programs/Python/Python37/Lib/site-packages/cv2/data/haarcascade_fullbody.xml')


body = body_classifier.detectMultiScale(gray, 1.1,5,minSize=(75,75))

for x,y,w,h in body:
    print(x,w,y,h)
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),1)



print("face found", len(body))


cv2.imshow("face",img)
cv2.imshow("gray",gray)
cv2.waitKey(0)
cv2.destroyAllWindows()