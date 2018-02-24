# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 10:44:20 2018

@author: shubham
"""


import csv
import Constant
from datetime import datetime
file=""
writer=""
count=1

def initThefile():
    global file
    global writer
    try:
        print("in initThefile" )
        file_name=Constant.log_file_path+str(datetime.now().strftime('%Y_%m_%d_%H_%M_%S'))+".csv"
        file = open(file_name, 'w')
        writer = csv.writer(file)
        writer.writerow(Constant.csv_header)
        print("out initThefile" )
    except:
        print("error in file while opening")




def writeToFile(url,status,time):
    try:
        print("in writeToFile" )
        global count
        writer.writerow([str(count),url,status,time])
        count+=1;
        print("out writeToFile" )
    except:
        print('file is opened')
    
def closefile():
    global file
    try:
        print("in closefile" )
        file.close()
        print("out closefile" )
    except:
        print("error while closing")
   # <---IMPORTANT

#print("started")
#initThefile()
#writeToFile('1','2','3')
#closefile()
#print("end")