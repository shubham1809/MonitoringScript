# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 20:24:34 2018

@author: shubham
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

import Constant
import checkStatusofURL
#global variable

driver=''
def initWebDrriver():
    global driver
    print("in initWebDrriver")
    chrome_options = Options()
    chrome_options.add_experimental_option( "prefs", {'--lang': 'en'})
    driver = webdriver.Chrome(executable_path=Constant.Chrome_exe_path,chrome_options=chrome_options)
    driver.maximize_window()
#    driver.get(Constant.Home_page_url)
    print("out initWebDrriver")
    
def extractAlllinks():
    global driver
    print(" in extractAlllinks")
#    continue_link = driver.find_element_by_tag_name('a')
    elems = driver.find_elements_by_xpath("//*[@href]")
    for elem in elems:
        checkStatusofURL.getStatusAndTime(elem.get_attribute("href"))
    print("out extractAlllinks")

def testSearchbutton():
    print("in testSearchbutton function" )
    driver.find_elements_by_xpath('//*[@id="open-searchform"]/span').click()
    driver.find_elements_by_xpath(' //*[@id="globalSearch"]').send_keys("soap")
    driver.find_elements_by_xpath('//*[@id="globalSearchForm"]/div[2]/button"]').submit()
    
    
    
def login_test_case():
    global driver
    status=checkStatusofURL.get_URL_status(Constant.lOGIN_PAGE_URL)
    elpased_time=0
    if(status=='UP'):
#    navigationStart = driver.execute_script("return window.performance.timing.navigationStart")
        driver.get(Constant.lOGIN_PAGE_URL)
        responseStart = driver.execute_script("return window.performance.timing.responseStart")
        
        password_tab = driver.find_element_by_id("password-tab")
        password_tab.click()
            
        username=driver.find_element_by_id("LoginModel_Username")
        username.send_keys(Constant.USER_ID)
        
        username=driver.find_element_by_id("LoginModel_Password")
        username.send_keys(Constant.PASSWORD)
        
        submit=driver.find_element_by_id("log-in-submit")
        submit.click()
        domComplete = driver.execute_script("return window.performance.timing.domComplete")
    #    current_url=driver.getCurrentUrl()
        elpased_time=domComplete-responseStart
    checkStatusofURL.saveFlow("Login Flow",status,elpased_time)
    
        

    
def endSession():
    driver.close()  
    driver.quit()

        
    