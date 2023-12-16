import cv2 as cv
import numpy as np
from time import sleep

minimo = np.array([0, 97, 146])
massimo = np.array([10, 255, 255])

camera = cv.VideoCapture(0)

if not camera.isOpened():
    print("camera non aperta in automatico.")
    camera.open()

try:
    while(True):
        isSuccess, frame = camera.read()
        if isSuccess:
            hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV) #da bgr a hsv
            mask = cv.inRange(hsv, minimo, massimo)
            res = cv.bitwise_and(frame, frame, mask= mask)
            cv.imshow("Frame", frame) 
            cv.imshow("Mask", mask)
        else:
            print("problemi con la read")
            sleep(5)

        if cv.waitKey(1) == ord('q'):
            break
except KeyboardInterrupt:
    print("aaa, non farlo usa 'q'")

camera.release()
cv.destroyAllWindows()
