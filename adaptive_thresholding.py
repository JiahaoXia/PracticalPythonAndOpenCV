__author__ = 'XJH'
import numpy as np
import cv2

image_dir = "coins.png"
image = cv2.imread(image_dir)
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(image, (5, 5), 0)
cv2.imshow("Image", image)

thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
							   cv2.THRESH_BINARY_INV, 11, 4)
cv2.imshow("Mean Threshold", thresh)

thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
							   cv2.THRESH_BINARY_INV, 15, 3)
cv2.imshow("Gaussian Threshold", thresh)
cv2.waitKey(0)