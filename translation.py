__author__ = 'XJH'
import numpy as np
import imutils
import cv2

image_dir = "trex.png"
image = cv2.imread(image_dir)
cv2.imshow("Original", image)

M = np.float32([[1, 0, 25], [0, 1, 50]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("shifted Down and Right", shifted)

M = np.float32([[1, 0, -50], [0, 1, -90]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted Up and Left", shifted)
cv2.waitKey(0)

shifted = imutils.translate(image, 0, 100)
cv2.imshow("Shifted Down", shifted)
cv2.waitKey(0)