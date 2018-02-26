# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 10:38:43 2018

@author: shubham
"""

import writeToCsv as wtv
import requests
import re

def save_url_Status_Time(url):
    print("in save_url_Status_Time" )
    res=requests.get(url)
    if(re.match("^[2]\d\d$", str(res.status_code))):
        status="UP"
    else:
        status="Down"
    responce_time=str(res.elapsed.total_seconds()*1000)+"ms"
    wtv.writeToFile(url,status,responce_time)
    print("out save_url_Status_Time" )
    


def getStatus(url,time):
    print("in getStatus" )
    res=requests.get(url)
    if(re.match("^[2]\d\d$", str(res.status_code))):
        status="UP"
    else:
        status="Down"
    responce_time=str(time)+"ms"
    wtv.writeToFile(url,status,responce_time)
    print("out getStatus" )
    
    
def get_URL_status(url):
    status='Down'
    try:
        res=requests.get(url)
#        print(res.status_code)
        if(re.match("^[2]\d\d$", str(res.status_code))):
            status="UP"
        else:
            status="Down"
        return status
    except:
        return status

def saveFlow(url,status,time):
    print("in saveFlow" )
    wtv.writeToFile(url,status,str(time/1000)+"sec")
    print("out saveFlow" )
    
#print(get_URL_status('https://www.ica.se/logga-in/?returnurl=https%3A%2F%2Fwww.ica.se%2F'))