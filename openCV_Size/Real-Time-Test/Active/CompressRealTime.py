from scipy.spatial import distance as dist
from imutils import perspective
from collections import deque
from imutils import contours
import numpy as np
import webbrowser
import argparse
import datetime
import logging
import imutils
import csv
import cv2
import sys

print("======================START======================")

def readlog():
	Reader = csv.reader(file)
	for line in Reader:
		print(line)
	file.close()
	
def midpoint(ptA, ptB):
	return ((ptA[0] + ptB[0]) * 0.5, (ptA[1] + ptB[1]) * 0.5)

def TakePic():
	camera = cv2.VideoCapture(0)
	frame = camera.read()[1]
	cv2.imwrite(filename='ObjectPic.JPG', img=frame)

def main():
	ap = argparse.ArgumentParser()
	ap.add_argument("")

	image = cv2.imread("ObjectPic.jpg")
	gray = cv2.GaussianBlur(gray, (5, 5), 0)	
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	edged = cv2.Canny(gray, 50, 100)
	edged = cv2.dilate(edged, None, iterations=1)
	edged = cv2.erode(edged, None, iterations=1)

	cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
	cnts = cnts[0] if imutils.is_cv2() else cnts[1]

	(cnts, _) = contours.sort_contours(cnts)
	pixelsPerMetric = None

	objectCount = 0
	file = open('./Results/NAME_HERE!.csv', 'w')

	for c in cnts:
		if cv2.contourArea(c) < 100:
		    continue

		orig = image.copy()
		box = cv2.minAreaRect(c)
		box = cv2.cv.BoxPoints(box) if imutils.is_cv2() else cv2.boxPoints(box)
		box = np.array(box, dtype="int")

		box = perspective.order_points(box)
		cv2.drawContours(orig, [box.astype("int")], -1, (0, 255, 0), 2)

		for (x, y) in box:
			cv2.circle(orig, (int(x), int(y)), 5, (0, 0, 255), -1)
        
		(tl, tr, br, bl) = box
		(tltrX, tltrY) = midpoint(tl, tr)
		(blbrX, blbrY) = midpoint(bl, br)

		(tlblX, tlblY) = midpoint(tl, bl)
		(trbrX, trbrY) = midpoint(tr, br)

		cv2.circle(orig, (int(tltrX), int(tltrY)), 5, (255, 0, 0), -1)
		cv2.circle(orig, (int(blbrX), int(blbrY)), 5, (255, 0, 0), -1)
		cv2.circle(orig, (int(tlblX), int(tlblY)), 5, (255, 0, 0), -1)
		cv2.circle(orig, (int(trbrX), int(trbrY)), 5, (255, 0, 0), -1)

		cv2.line(orig, (int(tltrX), int(tltrY)), (int(blbrX), int(blbrY)),
			(255, 0, 255), 2)
		cv2.line(orig, (int(tlblX), int(tlblY)), (int(trbrX), int(trbrY)),
			(255, 0, 255), 2)

		dA = dist.euclidean((tltrX, tltrY), (blbrX, blbrY))
		dB = dist.euclidean((tlblX, tlblY), (trbrX, trbrY))

		if pixelsPerMetric is None:
			pixelsPerMetric = dB / args["width"]
    
		dimA = dA / pixelsPerMetric
		dimB = dB / pixelsPerMetric

		cv2.putText(orig, "{:.1f}in".format(dimA),
			(int(tltrX - 15), int(tltrY - 10)), cv2.FONT_HERSHEY_SIMPLEX,
			0.65, (255, 255, 255), 2)
		cv2.putText(orig, "{:.1f}in".format(dimB),
			(int(trbrX + 10), int(trbrY)), cv2.FONT_HERSHEY_SIMPLEX,
			0.65, (255, 255, 255), 2)

		RounddimB = round(dimB, 1)
		objectCount = objectCount + 1
		print " "
		print "Conuting Result : ", objectCount
		print "Length(dimA) : ", dimA, "| Width(dimB) : ", dimB
		print "dimB Round Result : ", RounddimB

		cv2.imshow("Image", orig)
		cv2.waitKey(0)

		MessageCount = 	'Counting Result : ', objectCount, '\n', 
		MessageSize  =  'Length(dimA) : ', dimA, '| Width(dimB) : ', dimB, '\n',
		MessageRound =	'dimB Round Result : ', RounddimB, '\n'

		print('MessageCount')
		print('MessageSize')
		print('MessageRound')

		TotalMessage = str(MessageCount) + str(MessageSize) + str(MessageRound) + "\n"
		file.write (TotalMessage)
		print "				"
	readlog()
