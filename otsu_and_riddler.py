__author__ = 'XJH'
import numpy as np
import mahotas
import cv2

image_dir = "coins.png"
image = cv2.imread(image_dir)
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(image, (5, 5), 0)
cv2.imshow("Image", image)

T = mahotas.thresholding.otsu(blurred)
print("Otsu's threshold: {}".format(T))

thresh = image.copy()
thresh[thresh > T] = 255
thresh[thresh < T] = 0
thresh = cv2.bitwise_not(thresh)
cv2.imshow("Otsu", thresh)

T = mahotas.thresholding.rc(blurred)
print("Riddler-Calvard: {}".format(T))
thresh = image.copy()
thresh[thresh > T] = 255
thresh[thresh < T] = 0
thresh = cv2.bitwise_not(thresh)
cv2.imshow("Riddler-Calvard", thresh)
cv2.waitKey(0)