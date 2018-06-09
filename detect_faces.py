__author__ = 'XJH'
from facedetector import FaceDetector
import argparse
import cv2

image_dir = "messi.png"
image = cv2.imread(image_dir)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Origin", gray)

fd = FaceDetector("H:/Machine Learning/computer vision/[10307938]Books/Books/Case Studies, 3nd Edition/code/face_detection/cascades/haarcascade_frontalface_default.xml")
faceRects = fd.detect(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
print("I found {} face(s)".format(len(faceRects)))

for (x, y, w, h) in faceRects:
	cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imshow("Faces", image)
cv2.waitKey(0)