import cv2
import numpy as np
import imutils
from matplotlib import pyplot as plt

def green_detection(img_crop):
    area = 0.0
    hsv_img_crop = cv2.cvtColor(img_crop, cv2.COLOR_BGR2HSV)
    lower_green = np.array([30, 20, 30])
    upper_green = np.array([90, 255, 255])
    mask = cv2.inRange(hsv_img_crop, lower_green, upper_green)
    cv2.imshow('maska', mask)
    contours = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)[0]
    for contour in contours:
        area += cv2.contourArea(contour)
    print(area)
    cv2.drawContours(img_crop, contours, -1, (0, 0, 255), 3)
    cv2.imshow('zielony', img_crop)

frame=cv2.imread('photos/6_.jpg')

kernel=np.ones((5,5),np.uint8)
left_rail_bot = 650
right_rail_bot=0
rail_top_y=1000
right_rail_top_y=0
img = imutils.resize(frame, width=550,height=800)
org_img=img.copy()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), cv2.BORDER_DEFAULT)
edges = cv2.Canny(blur, 230, 250)
dilate=cv2.dilate(edges,kernel,iterations=2)
erode=cv2.erode(dilate,kernel,iterations=2)
lines = cv2.HoughLinesP(erode, 1, np.pi / 180, 120,minLineLength=200,maxLineGap=50)
#cv2.imshow('krawedzie', edges)
if lines is not None:
    for line in lines:
        x1, y1, x2, y2 = line[0]
        if x1<left_rail_bot and x1>150:
            left_rail_bot=x1
        if x1 > right_rail_bot and x1>left_rail_bot:
            right_rail_bot = x1
        elif x2 > right_rail_bot and x2>left_rail_bot:
            right_rail_bot=x2
        if y1 <rail_top_y and y1<y2:
            rail_top_y=y1
        elif y2<rail_top_y and y2<y1:
            rail_top_y=y2
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 3)
    img_crop = img[rail_top_y:719, left_rail_bot - 20:right_rail_bot + 20]
    img_crop=imutils.resize(img_crop,width=550,height=800)
    org_img_crop = org_img[rail_top_y:800, left_rail_bot - 20:right_rail_bot + 20]
    org_img_crop = imutils.resize(org_img_crop, 550, 800)
    cv2.imshow('tory', org_img_crop)
    cv2.imshow('szyny',img_crop)
    green_detection(img_crop)
    plt.hist(org_img_crop.ravel(), 256, [0, 256])
    plt.show()
cv2.waitKey(0)

cv2.destroyAllWindows()

