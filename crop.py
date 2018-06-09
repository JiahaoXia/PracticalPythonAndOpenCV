__author__ = 'XJH'
import numpy as np
import cv2

image_dir = "trex.png"
image = cv2.imread(image_dir)
cv2.imshow("Original", image)

cropped = image[30:120, 240:335]
cv2.imshow("T-Rex Face", cropped)
cv2.waitKey(0)