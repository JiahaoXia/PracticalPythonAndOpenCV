__author__ = 'XJH'
import numpy as np
import time
import cv2

blueLower = np.array([100, 67, 0], dtype="uint8")
blueUpper = np.array([255, 128, 50], dtype="uint8")

camera = cv2.VideoCapture("iphonecase.mov")

while True:
	(grapped, frame) = camera.read()
	if not grapped:
		break
	blue = cv2.inRange(frame, blueLower, blueUpper)
	blue = cv2.GaussianBlur(blue, (3, 3), 0)
	(_, cnts, _) = cv2.findContours(blue.copy(), cv2.RETR_EXTERNAL,
									cv2.CHAIN_APPROX_SIMPLE)
	if len(cnts) > 0:
		cnt = sorted(cnts, key=cv2.contourArea, reverse=True)[0]
		rect = np.int32(cv2.boxPoints(cv2.minAreaRect(cnt)))
		cv2.drawContours(frame, [rect], -1, (0, 255, 0), 2)
	cv2.imshow("Tracking", frame)
	cv2.imshow("Binary", blue)

	time.sleep(0.025)

	if cv2.waitKey(1) & 0xFF == ord("q"):
		break

camera.release()












