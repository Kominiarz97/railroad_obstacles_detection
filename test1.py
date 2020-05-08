import cv2
import numpy as np
import imutils
tor_film=cv2.VideoCapture("mov/mov_4.mp4")
kernel=np.ones((5,5),np.uint8)
ret,frame=tor_film.read()
img = imutils.resize(frame, width=1280,height=720)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), cv2.BORDER_DEFAULT)
edges = cv2.Canny(blur, 180, 250)
dilate=cv2.dilate(edges,kernel,iterations=4)
erode=cv2.erode(dilate,kernel,iterations=5)
lines = cv2.HoughLinesP(erode, 1, np.pi / 180, 70,minLineLength=300,maxLineGap=150)
cv2.imshow('krawedzie', edges)
cv2.imshow('krawedzi', dilate)
cv2.imshow('krawedz', erode)
for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 3)
    print("makao")


cv2.imshow('torrrr', img)
cv2.waitKey(0)



tor_film.release()
cv2.destroyAllWindows()

