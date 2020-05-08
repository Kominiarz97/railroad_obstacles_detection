import cv2
import numpy as np
import imutils
org_img=cv2.imread('photos/9.jpg')
kernel=np.ones((5,5),np.uint8)



left_rail_start = 600
top_rail_start=1000

img = imutils.resize(org_img, width=600,height=1000)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), cv2.BORDER_DEFAULT)
edges = cv2.Canny(blur, 130, 250)
dilate=cv2.dilate(edges,kernel,iterations=2)
erode=cv2.erode(dilate,kernel,iterations=2)
lines = cv2.HoughLinesP(erode, 1, np.pi / 180, 120,minLineLength=200,maxLineGap=100)
cv2.imshow('krawedzie', dilate)
for line in lines:
    x1, y1, x2, y2 = line[0]
    if x1<left_rail_start and x1>100:
        left_rail_start=x1
    if y2<top_rail_start:
        top_rail_start=y2
    cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 3)
img_crop=img[top_rail_start:600,left_rail_start-50:left_rail_start+250]
cv2.imshow('tory', img)
cv2.imshow('szyny',img_crop)
hsv_img_crop=cv2.cvtColor(img_crop,cv2.COLOR_BGR2HSV)

lower_green=np.array([40,70,80])
upper_green=np.array([70,255,255])
mask=cv2.inRange(hsv_img_crop,lower_green,upper_green)
cv2.imshow('maska',mask)

cv2.waitKey(0)
cv2.destroyAllWindows()

