__author__ = 'XJH'
import numpy as np
import cv2

image_dir = "coins.png"
image = cv2.imread(image_dir)
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(image, (11, 11), 0)
cv2.imshow("Image", image)

edged = cv2.Canny(blurred, 30, 150)
cv2.imshow("Edged", edged)

(_, cnts, _) = cv2.findContours(edged.copy(),
								cv2.RETR_EXTERNAL,
								cv2.CHAIN_APPROX_SIMPLE)

print("I count {} coins in this image".format(len(cnts)))

coins = image.copy()
# cv2.drawContours(coins, cnts, -1, (255, 0, 0), 2)

cv2.drawContours(coins, cnts, 0, (0, 255, 0), 2)
cv2.drawContours(coins, cnts, 1, (0, 255, 0), 2)
cv2.drawContours(coins, cnts, 2, (0, 255, 0), 2)

cv2.imshow("Coins", coins)
cv2.waitKey(0)

for (i, c) in enumerate(cnts):
	(x, y, w, h) = cv2.boundingRect(c)
	print("Coin #{}".format(i + 1))
	coin = image[y:y + h, x:x + w]
	cv2.imshow("Coin", coin)
	mask = np.zeros(image.shape[:2], dtype = "uint8")
	((centerX, centerY), radius) = cv2.minEnclosingCircle(c)
	cv2.circle(mask, (int(centerX), int(centerY)), int(radius), 255, -1)
	mask = mask[y:y + h, x:x + w]
	cv2.imshow("Masked Coin", cv2.bitwise_and(coin, coin, mask = mask))
	cv2.waitKey(0)