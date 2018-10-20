import numpy as np
import cv2
from PIL import Image
import datetime
import face_recognition

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
close_gesture = cv2.CascadeClassifier('fists.xml')

cap = cv2.VideoCapture(0)

detected = 80
file_name = None
shutoff = False

while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    close_sign = close_gesture.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img,'person',(x+w,y+h), font, 0.5, (11,255,255), 2, cv2.LINE_AA)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

        if detected % 80 == 0:
        	file_name = datetime.datetime.now()
        	status = cv2.imwrite('log/{}.png'.format(file_name),gray)

        detected += 1

    for (x,y,w,h) in close_sign:
    	font = cv2.FONT_HERSHEY_SIMPLEX
    	cv2.putText(img,'hand',(x+w,y+h), font, 0.5, (11,255,255), 2, cv2.LINE_AA)
    	shutoff = True
			        
    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff 
    if k == ord('q') or shutoff == True:
        break

cap.release()
cv2.destroyAllWindows()