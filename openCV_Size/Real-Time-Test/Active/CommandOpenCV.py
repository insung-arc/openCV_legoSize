# ::::	2018-04-28	::::
# ::::	Pobculater	::::
#
# import the necessary packages
# sucess time :
# Date : 2018-04-28
# Clock : 16 : 09 
#
import os
import sys
import csv
import webbrowser

#print ("======================START======================")

def CommandCode():
    command = "python" + " " + "Real-Time-Build1.py" + " " + "-i" + "ObjectPic.JPG" + " " + "-w" + " " + "3.5"
    process = os.popen(command)
    results = str(process.read())
    return results

def FinalResult():
    command = "cat" + " " + "./Results/NAME_HERE!.csv"
    process = os.popen(command)
    results = str(process.read())
    return results

'''
def GoSOF():
    sof_search = 'https: // stackoverflow.com/search?q='
    ErrorName = input("Type here the error >>> ")
    search_url = sof_search + ErrorName
    webbrowser.open_new_tab(search_url)
'''

if __name__ == "__main__":
    CommandCode()
    FinalResult()
    
#print ("======================END======================")
