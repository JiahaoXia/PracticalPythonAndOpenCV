__author__ = 'XJH'
import numpy as np
import imutils
import cv2

image_dir = "trex.png"
image = cv2.imread(image_dir)
cv2.imshow("Original", image)

r = 150.0 / image.shape[1]
dim = (150, int(image.shape[0] * r))

resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
cv2.imshow("Resized (Width INTER_AREA)", resized)

resized = cv2.resize(image, dim, interpolation = cv2.INTER_LINEAR)
cv2.imshow("Resized (Width INTER_LINEAR)", resized)

resized = cv2.resize(image, dim, interpolation = cv2.INTER_CUBIC)
cv2.imshow("Resized (Width INTER_CUBIC)", resized)

resized = cv2.resize(image, dim, interpolation = cv2.INTER_NEAREST)
cv2.imshow("Resized (Width INTER_NEAREST)", resized)
cv2.waitKey(0)

r = 50.0 / image.shape[0]
dim = (int(image.shape[1] * r), 50)

resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
cv2.imshow("Resized (Height)", resized)
cv2.waitKey(0)