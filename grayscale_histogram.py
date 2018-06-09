__author__ = 'XJH'
from matplotlib import pyplot as plt
import cv2

image_dir = "trex.png"
image = cv2.imread(image_dir)

image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
cv2.imshow("Original", image)

hist = cv2.calcHist([image], [0], None, [256], [0, 256])

plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
plt.plot(hist)
plt.xlim([0, 256])
plt.show()
cv2.waitKey(0)