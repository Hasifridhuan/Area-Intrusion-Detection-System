import cv2
import time
import threading
import numpy as np
from shapely.geometry import Point, Polygon

human = cv2.CascadeClassifier('haarcascade_fullbody.xml')
# car = cv2.CascadeClassifier('car.xml')
video = cv2.VideoCapture('dataset/test 1.mp4')

# new_img = cv2.imread('pedestrian.jpg', 0)

width = 1280
height = 720

while True:
    rc, image = video.read()
    if type(image) == type(None):
        break
    image = cv2.resize(image, (width, height))
    resultImage = image.copy()
    coord = [(27, 97), (120, 490), (1143, 623), (1140, 85)]
    # (401, 269), (331, 521), (583, 623), (825, 520), (803, 242), (657, 321)
    poly = Polygon(coord)

    pts = np.array(coord)
    # [[401, 269], [331, 521], [583, 623], [825, 520], [803, 242], [657, 321]]
    pts = np.reshape(pts, (-1, 1, 2))
    isclose = True
    color = (0, 0, 0)
    thick = 2
    imgpoly = cv2.polylines(resultImage, [pts], isclose, color, thick)

    gray = cv2.cvtColor(imgpoly, cv2.COLOR_BGR2GRAY)
    human2 = human.detectMultiScale(gray, 1.1, 5)
    # gray2 = cv2.cvtColor(imgpoly, cv2.COLOR_BGR2GRAY)
    # car = car.detectMultiScale(gray2, 1.1, 7)

    for (x, y, w, h) in human2:
        p1 = Point(x, y)
        p2 = Point(x + w, y)
        p3 = Point(x, y + h)
        p4 = Point(x + w, y + h)

        if p3.within(poly) or p4.within(poly) or p1.within(poly) or p2.within(poly):
            cv2.rectangle(imgpoly, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.putText(imgpoly, 'Warning: Restricted Area!', (46, 46), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            cv2.putText(imgpoly, 'Area Breach!', (1000, 46), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
            print('Alert: Area Breach')
        # cv2.rectangle(imgpoly, (x, y), (x+w, y+h), (0, 0, 0), 2)
    cv2.imshow('window', imgpoly)
    if cv2.waitKey(0) == ord('q'):
        break

cv2.destroyAllWindows()
