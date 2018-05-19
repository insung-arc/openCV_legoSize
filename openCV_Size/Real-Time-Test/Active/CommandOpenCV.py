'''
    coding by

                    /$$$$$$                /$$   /$$ /$$ /$$$$$$$ 
                   /$$__  $$              | $$$ | $$| $/| $$__  $$
                  | $$  \ $$ /$$$$$$/$$$$ | $$$$| $$|_/ | $$  \ $$
                  |$$$$$$$$ | $$_  $$_  $$| $$ $$ $$    | $$  | $$
                  | $$__  $$| $$ \ $$ \ $$| $$  $$$$    | $$  | $$
                  | $$  | $$| $$ | $$ | $$| $$\  $$$    | $$  | $$
                  | $$  | $$| $$ | $$ | $$| $$ \  $$    | $$$$$$$/
                  |__/  |__/|__/ |__/ |__/|__/  \__/    |_______/ 
                                                
                         *!*!THIS PROGRAME IS COPYLEFT!*!*
     You can use anywhere. But please add this comment title or end of the code
                            [original coding by Amn'D]

                	Amn'D-LEGO Bean Size Check release : v0.3.1 (May 5 2018)
        Amn'd-CV?X!Size is open source cleaning dictoray. This code made by AmN'D

                    FACEBOOK : https://facebook.com/insung.bahk
                      GITHUB : https://github.com/insung3511
                          EMAIL : insung3511@icloud.com
'''
# Here we go.. 
print("========START========")

# Okay, Here is the your computer need library
import os
import cv2
import sys
import csv

# This is Take Picture to measuring size
# Take picture with openCV 3 
def TakePic():
	camera = cv2.VideoCapture(0)
	frame = camera.read()[1]
	cv2.imwrite(filename='ObjectPic.JPG', img=frame)

# CommandCode is function that inputs commands.
# If you want change [Real-Time-Build1.py] file dictoray. 
# Then you have to also move [Real-Time-Build1.py].
def CommandCode():
    command = "python" + " " + "Real-Time-Build1.py" + " " + "-i" + "ObjectPic.JPG" + " " + "-w" + " " + "3.5"
    process = os.popen(command)
    results = str(process.read())
    return results

# Am... This function was show the about mesauring size data.
# It have some wrong part... so, AmN'D is fixing it!
'''
def FinalResult():
    command = "cat" + " " + "./Results/NAME_HERE!.csv"
    process = os.popen(command)
    results = str(process.read())
    return results
'''

if __name__ == "__main__":
    TakePic()
    CommandCode()

# Sooo.. End... 
print("==========END=========")
