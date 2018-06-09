__author__ = 'XJH'
from eyetracker import EyeTracker
import imutils
import cv2

et = EyeTracker("haarcascade_frontalface_default.xml",
				"haarcascade_eye.xml")

# 读入视频
camera = cv2.VideoCapture("adrian_eyes.mov")
while True:
	(grabbed, frame) = camera.read()
	if not grabbed:
		break
	frame = imutils.resize(frame, width=300)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	rects = et.track(gray)

	for rect in rects:
		cv2.rectangle(frame, (rect[0], rect[1]),
					  (rect[2], rect[3]), (0, 255, 0), 2)
		cv2.imshow("Tracking", frame)
		if cv2.waitKey(1) & 0xFF == ord("q"):
			break

camera.release()








