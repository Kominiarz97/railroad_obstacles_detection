import cv2
import numpy as np
import imutils
tor_film=cv2.VideoCapture("mov/mov_4.mp4")

while(1):
    ret,frame=tor_film.read()
    img = imutils.resize(frame, height=800)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), cv2.BORDER_DEFAULT)
    edges = cv2.Canny(blur, 230, 250)
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 120,maxLineGap=120)
    cv2.imshow('torr', edges)
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 5)

    cv2.imshow('tor', img)
    if cv2.waitKey(1)==27:
        break
tor_film.release()
cv2.destroyAllWindows()

