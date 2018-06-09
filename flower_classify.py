__author__ = 'XJH'
from rgbhistogram import RGBHistogram
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import numpy as np
import glob
import cv2

imagePaths = sorted(glob.glob("images/*.png"))
maskPaths = sorted(glob.glob("masks/*.png"))

data = []
target = []

desc = RGBHistogram([8, 8, 8])

for (imagePath, maskPath) in zip(imagePaths, maskPaths):
	image = cv2.imread(imagePath)
	mask = cv2.imread(maskPath)
	mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)

	features = desc.describe(image, mask)

	data.append(features)
	target.append(imagePath.split("_")[-2])

targetNames = np.unique(target)
le = LabelEncoder()
target = le.fit_transform(target)

(trainData, testData, trainTarget, testTaeget) = train_test_split(data,
																  target,
																  test_size=0.3,
																  random_state=42)

model = RandomForestClassifier(n_estimators=25, random_state=84)
model.fit(trainData, trainTarget)

print(classification_report(testTaeget, model.predict(testData),
							target_names=targetNames))

for i in np.random.choice(np.arange(0, len(imagePaths)), 10):
	imagePath = imagePaths[i]
	maskPath = maskPaths[i]

	image = cv2.imread(imagePath)
	mask = cv2.imread(maskPath)
	mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)

	features = desc.describe(image, mask)

	flower = le.inverse_transform(model.predict([features]))[0]
	print(imagePath)
	print("I think this flower is a {}".format(flower.upper()))
	cv2.imshow("image", image)
	cv2.waitKey(0)