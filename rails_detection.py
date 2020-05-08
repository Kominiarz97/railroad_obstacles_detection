import cv2
import numpy as np
import imutils
tor_film=cv2.VideoCapture("mov/mov_4.mp4")
kernel=np.ones((5,5),np.uint8)

while(1):
    left_rail_start = 1280
    right_rail_start=0
    ret,frame=tor_film.read()
    img = imutils.resize(frame, width=1280,height=720)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), cv2.BORDER_DEFAULT)
    edges = cv2.Canny(blur, 230, 250)
    dilate=cv2.dilate(edges,kernel,iterations=2)
    erode=cv2.erode(dilate,kernel,iterations=2)
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 70,minLineLength=200,maxLineGap=100)
    cv2.imshow('krawedzie', edges)
    for line in lines:
        x1, y1, x2, y2 = line[0]
        if x1<left_rail_start and x1>150:
            left_rail_start=x1
        if x1 > right_rail_start and x1>left_rail_start:
            right_rail_start = x1
        elif x2 > right_rail_start and x2>left_rail_start:
            right_rail_start=x2
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 3)
    img_crop = img[150:719, left_rail_start - 20:right_rail_start+20]
    cv2.imshow('tory', img)
    cv2.imshow('szyny',img_crop)



    if cv2.waitKey(1)==27:
        break
tor_film.release()
cv2.destroyAllWindows()

