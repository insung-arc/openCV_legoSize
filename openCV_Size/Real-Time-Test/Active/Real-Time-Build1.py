'''
    coding by

                    /$$$$$$                /$$   /$$ /$$ /$$$$$$$ 
                   /$$__  $$              | $$$ | $$| $/| $$__  $$
                  | $$  \ $$ /$$$$$$/$$$$ | $$$$| $$|_/ | $$  \ $$
                  |$$$$$$$$| $$_  $$_  $$ | $$ $$ $$    | $$  | $$
                  | $$__  $$| $$ \ $$ \ $$| $$  $$$$    | $$  | $$
                  | $$  | $$| $$ | $$ | $$| $$\  $$$    | $$  | $$
                  | $$  | $$| $$ | $$ | $$| $$ \  $$    | $$$$$$$/
                  |__/  |__/|__/ |__/ |__/|__/  \__/    |_______/ 
                                                
                         *!*!THIS PROGRAME IS COPYLEFT!*!*
     You can use anywhere. But please add this comment title or end of the code
                            [original code by Amn'D]

                	Amn'D-LEGO Bean Size Check release : v0.3.1 (May 5 2018)
            Amn'd-Cleaner is open source cleaning dictoray. This code made by AmN'D

                      FACEBOOK : https://facebook.com/insung.bahk
                        GITHUB : https://github.com/insung3511
                            EMAIL : insung3511@icloud.com
'''
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
import os

print("======================START======================")

# GUI Grapic Funtion
def midpoint(ptA, ptB):
	return ((ptA[0] + ptB[0]) * 0.5, (ptA[1] + ptB[1]) * 0.5)

'''
# Take Object Picture
 ndef TakePic():
	camera = cv2.VideoCapture(0)
	frame = camera.read()[1]
	cv2.imwrite(filename='ObjectPic.JPG', img=frame)

# First take picture to get object
TakePic()
'''

# The Main Code...
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to the input image")
ap.add_argument("-w", "--width", type=float, required=True,
    help="width of the left-most object in the image (in inches)")	

args = vars(ap.parse_args())

# openCV image Setting
image = cv2.imread("ObjectPic.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (5, 5), 0)	
	
# Here is also image setting
edged = cv2.Canny(gray, 50, 80)
edged = cv2.dilate(edged, None, iterations=1)
edged = cv2.erode(edged, None, iterations=1)

# Setting object size mesauring
cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,
cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if imutils.is_cv2() else cnts[1]

(cnts, _) = contours.sort_contours(cnts)
pixelsPerMetric = None

# This is object count essenace.
# And under is file to write the log
objectCount = 0
file = open('./Results/NAME_HERE!.csv', 'w')

# Here is measuring the code
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

	Messages = 'Length : ' + str(dimA) + ' | Width : ' + str(dimB) + ' | Count Number : ' + str(objectCount) + '\n'
	file.write(Messages)

	cv2.imshow("Image", orig)
	cv2.waitKey(0)
	print "				"
	

print("=======================END=======================")
