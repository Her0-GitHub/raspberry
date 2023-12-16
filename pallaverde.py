#Imports
import cv2
import numpy as np
import imutils

def trova_colore(immagine):

    global cx,cy,cz
    hsv = cv2.cvtColor(immagine, cv2.COLOR_BGR2HSV)
    low = np.array([36,50,50])
    high = np.array([85,255,255])
    mask = cv2.inRange(hsv, low, high)
    cv2.imshow("Canvas0", mask)
    cnts = cv2.findContours(mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)#problemi di compatibilità
    if len(cnts)!=0:
        c = max(cnts, key = cv2.contourArea)
        x,y,w,h = cv2.boundingRect(c)
        area=w*h
        if area>2000:
            cx=(x+(w//2))
            cy=(y+(h//2))
            cz=area
    

        
#Initalizations
cap=cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cx=0
cy=0
cz=0
#Main
while True:

    #Prende immagini dalla cam e le mostra ad ogni iterazione del ciclo
    ret,img=cap.read()
    k=cv2.waitKey(1)
    print("frame")
    cv2.imshow("Canvas", img)
    