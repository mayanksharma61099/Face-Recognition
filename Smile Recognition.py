#!/usr/bin/env python3

#Face Recognition

#Importing the Libraries
import cv2

#Loading the Cascades
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')
specs_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')

#Defining a function that will do the detection
def detect(gray, frame):
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 1)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0,255,0), 2)
        specs = specs_cascade.detectMultiScale(roi_gray, 1.1, 50)
        for (sx, sy, sw, sh) in specs:
            cv2.rectangle(roi_color, (sx, sy), (sx + sw, sy + sh), (0,255,0), 2)
        smile = smile_cascade.detectMultiScale(roi_gray, 1.1, 20)
        for (sx, sy, sw, sh) in smile:
            cv2.rectangle(roi_color, (sx, sy), (sx + sw, sy + sh), (0,0,255), 2)
            print('You\'re Smiling')
    return frame

#Doing some Face Recognition using the Webcam
video_capture = cv2.VideoCapture(0)
while True:
    _,frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    canvas = detect(gray, frame)
    cv2.imshow('Video', canvas)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
