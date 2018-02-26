# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 20:37:42 2018

@author: shubham
"""
import os

Chrome_exe_path='D:\\selenium\\jars\\chromedriver_win32\\chromedriver.exe'

Home_page_url="https://www.ica.se"
lOGIN_PAGE_URL="https://www.ica.se/logga-in/?returnurl=https%3A%2F%2Fwww.ica.se%2F"
ADD_TO_CART_UTL="https://www.ica.se/handla/?io_internal_content=lankpuff-icase&io_internal_campaign=online"

log_file_path=os.path.expanduser("~\\Desktop\LogMonitor")
csv_header=['S.No','URL','Status','Elapsed Time']

USER_ID="199401101234"
PASSWORD="101994"
POSTAL_CODE=47121

product_list={'Mjölkchoklad cookies 184g Marabou':2,'Gröna kärnfria druvor 500g Klass 1 ICA':1,'Banan ca 180g':2}

PRODUCT_1="Mjölkchoklad cookies 184g Marabou"
PRODUCT_1_QTY=2


PRODUCT_1="Gröna kärnfria druvor 500g Klass 1 ICA"
PRODUCT_1_QTY=2


