# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 11:25:58 2018

@author: shubham
"""
import Constant

import writeToCsv as wtv
import checkStatusofURL
import start_run
    
if __name__ == '__main__':
    try:
        print("Started...")
        wtv.initThefile()
        start_run.initWebDrriver()
        start_run.login_test_case()
#        start_run.clearcart()
#        start_run.add_to_cart()
#        start_run.checkOut_item()
        start_run.logout()
        #start_run.extractAlllinks()
        #getStatusAndTime(Constant.Home_page_url)
        #testSearchbutton()
#       start_run.endSession()
        wtv.closefile()
        print("Finished.....")
    except Exception as e:
        print(e)