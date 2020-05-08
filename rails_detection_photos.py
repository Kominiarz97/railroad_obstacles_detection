import cv2
import numpy as np
import imutils
from matplotlib import pyplot as plt
org_img=cv2.imread('photos/tree1.jpg')
kernel=np.ones((5,5),np.uint8)
area=0.0

left_rail_start = 600
top_rail_start=1000

img = imutils.resize(org_img, width=600,height=1000)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), cv2.BORDER_DEFAULT)
edges = cv2.Canny(blur, 130, 250)
dilate=cv2.dilate(edges,kernel,iterations=2)
erode=cv2.erode(dilate,kernel,iterations=2)
lines = cv2.HoughLinesP(erode, 1, np.pi / 180, 120,minLineLength=50,maxLineGap=100)
cv2.imshow('krawedzie', dilate)
for line in lines:
    x1, y1, x2, y2 = line[0]
    if x1<left_rail_start and x1>100:
        left_rail_start=x1
    if y2<top_rail_start:
        top_rail_start=y2
    cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 3)
img_crop=img[top_rail_start:600,left_rail_start-50:left_rail_start+250]
org_img_crop=org_img[top_rail_start:600,left_rail_start-50:left_rail_start+250]
cv2.imshow('tory', img)
cv2.imshow('szyny',img_crop)

hsv_img_crop=cv2.cvtColor(img_crop,cv2.COLOR_BGR2HSV)
lower_green=np.array([20,70,80])
upper_green=np.array([90,255,255])
mask=cv2.inRange(hsv_img_crop,lower_green,upper_green)
cv2.imshow('maska',mask)
contours=cv2.findContours(mask.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)[0]
for contour in contours:
    area+=cv2.contourArea(contour)
print(area)
cv2.drawContours(img_crop,contours,-1,(0,0,255),3)

plt.hist(org_img_crop.ravel(),256,[0,256])
plt.show()

cv2.imshow('zielony',img_crop)
cv2.waitKey(0)
cv2.destroyAllWindows()

