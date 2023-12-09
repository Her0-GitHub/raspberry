import cv2 as cv
import numpy as np

minimo = np.array([0, 97, 146])
massimo = np.array([10, 255, 255])

camera = cv.VideoCapture(0)

try:
    while(True):
        ret, frame = camera.read()
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV) #da bgr a hsv
        mask = cv.inRange(hsv, minimo, massimo)
        res = cv.bitwise_and(frame, frame, mask= mask)
        cv.imshow("Frame", frame) 
        cv.imshow("Mask", mask)
        if cv.waitKey(1) == ord('q'):
            break
except KeyboardInterrupt:
    print("a")
camera.release()
cv.destroyAllWindows()