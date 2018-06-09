__author__ = 'XJH'
import numpy as np
import cv2

image_dir = "beach.png"
image = cv2.imread(image_dir)
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", image)

eq = cv2.equalizeHist(image)

cv2.imshow("Histogram Equalization", np.hstack([image, eq]))
cv2.waitKey(0)