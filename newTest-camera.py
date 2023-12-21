import cv2 as cv
import numpy as np
import imutils
from time import sleep

from ControlloMotori import *

# 0 Low 1 High
orange = [np.array([4, 105, 164]), np.array([13, 255, 225])]

camera = cv.VideoCapture(0)
camera.set(3, 640)
camera.set(4, 480)
cameraPos = {'minX': 0, 'minY': 0, "cX": 640 // 2, "cY": 480 // 2, "maxX": 640, "maxY": 480}


def trova_colore(immagine):
    hsv = cv.cvtColor(immagine, cv.COLOR_BGR2HSV)
    mask = cv.inRange(hsv, orange[0], orange[1])
    cv.imshow("Canvas0", mask)
    cnts = cv.findContours(mask, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)  # problemi di compatibilità
    if len(cnts) != 0 and cnts is not None:
        c = max(cnts, key=cv.contourArea)
        if c is not None:
            x, y, w, h = cv.boundingRect(c)
            a = w * h
            if a > 150:
                rettangolo = cv.rectangle(immagine, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv.imshow("Canvas1", rettangolo)
                return x, y, w, h, a
    return None, None, None, None, None


setup()

try:
    while True:
        isSuccess, frame = camera.read()
        if isSuccess:
            x, y, w, h, a = trova_colore(frame)
            if x is not None:
                if x < cameraPos['cX']:
                    print(f"x: {x}, y: {y}, w: {w}, h: {h}, a: {a} - vai a sinistra")
                    sinitra()
                elif x > cameraPos['cX']:
                    print(f"x: {x}, y: {y}, w: {w}, h: {h}, a: {a} - vai a destra")
                    destra()
            else:
                print("non ho trovato nulla")
        else:
            print("problemi con la read")
            sleep(5)

        if cv.waitKey(1) == ord('q'):
            break
except KeyboardInterrupt:
    print("aaa, non farlo usa 'q'")

endProgram()
camera.release()
cv.destroyAllWindows()