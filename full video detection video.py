import cv2

cap = cv2.VideoCapture("E:/openCv/data/vtest.avi")

body_classifier=cv2.CascadeClassifier('C:/Users/karam chand/AppData/Local/Programs/Python/Python37/Lib/site-packages/cv2/data/haarcascade_fullbody.xml')

while True:
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imwrite("avii11.jpg",frame)
    body= body_classifier.detectMultiScale(gray,1.3,5)
    for x, y, w, h in body:

        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 1)


    cv2.imshow("adas",frame)
    if cv2.waitKey(1)==13:
        break

cap.release()
cv2.destroyAllWindows()