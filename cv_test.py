import cv2
import numpy as np


capture = cv2.VideoCapture( 0 )

INTERVAL= 10

cascade_file = "haarcascades/haarcascade_frontalface_alt2.xml"
cascade = cv2.CascadeClassifier(cascade_file)

while True:

    ret, frame = capture.read()
    faces = cascade.detectMultiScale( frame, minSize=(100, 100) )

    for x, y, w, h in faces:
        face = frame[ y:y+h, x:x+w ]
        color = ( 0, 0, 225 )
        pen_w = 3
        cv2.rectangle( frame, (x, y), (x+w, y+h), color, thickness=pen_w )

    cv2.imshow( 'frame', frame )

    key = cv2.waitKey( INTERVAL ) & 0xFF
    if key == ord('q'):
        break

cv2.destroyAllWindows()
capture.release()