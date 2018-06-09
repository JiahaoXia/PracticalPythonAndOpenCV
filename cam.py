__author__ = 'XJH'
from facedetector import FaceDetector
import imutils
import cv2

fd = FaceDetector("H:/Machine Learning/computer vision/[10307938]Books/Books/Case Studies, 3nd Edition/code/face_detection/cascades/haarcascade_frontalface_default.xml")

camera = cv2.VideoCapture("adrian_face.mov")

while True:
	(grabbed, frame) = camera.read()
	if not grabbed:
		break
	frame = imutils.resize(frame, width = 300)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	faceRects = fd.detect(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
	frameClone = frame.copy()
	for (fX, fY, fW, fH) in faceRects:
		cv2.rectangle(frameClone, (fX, fY), (fX + fW, fY + fH), (0, 0, 255), 2)
	cv2.imshow("Face", frameClone)
	if cv2.waitKey(1) & 0xFF == ord("q"):
		break

camera.release()