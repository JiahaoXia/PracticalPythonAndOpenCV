__author__ = 'XJH'
from coverdescriptor import CoverDescriptor
from covermatcher import CoverMatcher
import glob
import csv
import cv2

db = {}

for l in csv.reader(open("books.csv")):
	db[l[0]] = l[1:]

useSIFT = 0 > 0
useHamming = 0 ==0
ratio = 0.7
minMatches = 40

if useSIFT:
	minMatches = 50

cd = CoverDescriptor(useSIFT=useSIFT)
cv = CoverMatcher(cd, glob.glob("covers/*.png"),
				  ratio=ratio, minMatches=minMatches,
				  useHamming=useHamming)

queryImage = cv2.imread("queries/query01.png")
gray = cv2.cvtColor(queryImage, cv2.COLOR_BGR2GRAY)
(queryKps, queryDescs) = cd.describe(gray)

results = cv.search(queryKps, queryDescs)

cv2.imshow("Query", queryImage)

if len(results) == 0:
	print("I could not find a match for that cover!")
	cv2.waitKey(0)
else:
	for (i, (score, coverPath)) in enumerate(results):
		(author, title) = db[coverPath[coverPath.rfind("\\") + 1:]]
		print("{}. {:.2f} : {} - {}".format(i + 1, score * 100, author, title))
		result = cv2.imread(coverPath)
		cv2.imshow("Result", result)
		cv2.waitKey(0)