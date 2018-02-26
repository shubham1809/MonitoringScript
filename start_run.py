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
    driver.delete_all_cookies()
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
    try:
        if(status=='UP'):
    #    navigationStart = driver.execute_script("return window.performance.timing.navigationStart")
            driver.get(Constant.lOGIN_PAGE_URL)
            responseStart = driver.execute_script("return window.performance.timing.responseStart")
            
            password_tab = driver.find_element_by_id("password-tab")
            password_tab.click()
                
            username=driver.find_element_by_id("LoginModel_Username")
            username.clear()
            username.send_keys(Constant.USER_ID)
            
            password=driver.find_element_by_id("LoginModel_Password")
            password.clear()
            password.send_keys(Constant.PASSWORD)
            
            submit=driver.find_element_by_id("log-in-submit")
            submit.click()
            domComplete = driver.execute_script("return window.performance.timing.domComplete")
        #    current_url=driver.getCurrentUrl()
            elpased_time=domComplete-responseStart
        checkStatusofURL.saveFlow("Login Flow",status,elpased_time)
    except:
        checkStatusofURL.saveFlow("Login Flow","Down",elpased_time)
        

def add_to_cart():
    global driver
#    driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')
#    login_test_case()
    status=checkStatusofURL.get_URL_status(Constant.ADD_TO_CART_UTL)
    elpased_time=0
    try:
        if(status=='UP'):
    #    navigationStart = driver.execute_script("return window.performance.timing.navigationStart")
            driver.get(Constant.ADD_TO_CART_UTL)
            responseStart = driver.execute_script("return window.performance.timing.responseStart")
            
#            if(driver.find_element_by_id("zip-code__front").size()!=0):
#                postal_code=driver.find_element_by_id("zip-code__front")
#                postal_code.clear()
#                postal_code.send_keys(Constant.POSTAL_CODE)
#                
#                driver.implicitly_wait(5)
#                
#                home_pickup = driver.find_element_by_id("search-result-list-PICKUP")
#                home_pickup.click()
#                    
#                store_name=driver.find_element_by_name("ICA Supermarket Nordeviks")
#    #            store_name.click()
            for key,value in Constant.product_list.items():
                search_product=driver.find_element_by_id("search")
                search_product.clear()
                search_product.send_keys(key)
                driver.implicitly_wait(5)
                
                searched_product=driver.find_element_by_xpath('//*[@id="typeAhead"]/li[3]/article/div[1]/a/div[2]/div[2]')
                searched_product.click()
                
                
        #        product_link=driver.find_element_by_link_text(Constant.PRODUCT_1_LINK)
                product_qty=driver.find_element_by_class_name('proxyTextBox')
                product_qty.click()
                input_qty=driver.find_element_by_class_name('ica-changeCartItemQty')
                input_qty.clear()
                input_qty.send_keys(value)
                driver.implicitly_wait(5)
                driver.find_element_by_tag_name('body').click()
            driver.find_element_by_tag_name('body').click()
            driver.refresh()
            domComplete = driver.execute_script("return window.performance.timing.domComplete")
        #    current_url=driver.getCurrentUrl()
            elpased_time=domComplete-responseStart
        checkStatusofURL.saveFlow("Add to cart flow",status,elpased_time)
    except:
        checkStatusofURL.saveFlow("Add to cart flow","Down",elpased_time)
        
    
def checkOut_item():
    global driver
#    driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')
    status=checkStatusofURL.get_URL_status(Constant.ADD_TO_CART_UTL)
    elpased_time=0
    try:
        if(status=='UP'):
    #    navigationStart = driver.execute_script("return window.performance.timing.navigationStart")
            driver.get(Constant.ADD_TO_CART_UTL)
            responseStart = driver.execute_script("return window.performance.timing.responseStart")
#            if(driver.find_element_by_id("zip-code__front").size()!=0):
#            postal_code=driver.find_element_by_id("zip-code__front")
#            postal_code.clear()
#            postal_code.send_keys(Constant.POSTAL_CODE)
#            
#            driver.implicitly_wait(5)
#            
#            home_pickup = driver.find_element_by_id("search-result-list-PICKUP")
#            home_pickup.click()
#                
#            store_name=driver.find_element_by_name("ICA Supermarket Nordeviks")
#            store_name.click()
            check_out_icon=driver.find_element_by_id("showMiniCart")
            check_out_icon.click()
            check_out_button=driver.find_element_by_xpath('//*[@id="shoppingCartTemplateWrap"]/div[1]/div[3]/div/a')
            check_out_button.click()
            if(driver.find_element_by_id("phoneNumber").size()!=0):
                check_out_mob=driver.find_element_by_id("phoneNumber")
                check_out_mob.clear()
                check_out_mob.click()
                
                check_out_save=driver.find_element_by_name(" Save and continue")
                check_out_save.click()
            
            driver.implicitly_wait(5)
            driver.find_element_by_tag_name('body').click()
            
            domComplete = driver.execute_script("return window.performance.timing.domComplete")
        #    current_url=driver.getCurrentUrl()
            elpased_time=domComplete-responseStart
        checkStatusofURL.saveFlow("Check Out",status,elpased_time)
    except Exception as e:
        print(e)
        checkStatusofURL.saveFlow("Check Out","Down",elpased_time)
    
    
    
def clearcart():
    global driver
#    driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')
    status=checkStatusofURL.get_URL_status(Constant.ADD_TO_CART_UTL)
    elpased_time=0
    try:
        if(status=='UP'):
    #    navigationStart = driver.execute_script("return window.performance.timing.navigationStart")
            driver.get(Constant.ADD_TO_CART_UTL)
            responseStart = driver.execute_script("return window.performance.timing.responseStart")
            check_out_icon=driver.find_element_by_id("showMiniCart")
            check_out_icon.click()
            
            if(driver.find_element_by_xpath('//*[@id="deleteAll"]').is_enabled()):
                delete_icon=driver.find_element_by_xpath('/*[@id="deleteAll"]')
                delete_icon.click()
                click_delete_button=driver.find_element_by_xpath("/html/body/div[6]/div[4]/button[2]")
                click_delete_button.click()
            
            
            domComplete = driver.execute_script("return window.performance.timing.domComplete")
        #    current_url=driver.getCurrentUrl()
            elpased_time=domComplete-responseStart
        checkStatusofURL.saveFlow("Clear Cart",status,elpased_time)
    except Exception as e:
        print(e)
        checkStatusofURL.saveFlow("Clear Cart","Down",elpased_time)
        
        
def logout():
    global driver
#    driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')
    status=checkStatusofURL.get_URL_status(Constant.ADD_TO_CART_UTL)
    elpased_time=0
    try:
        if(status=='UP'):
            driver.get(Constant.ADD_TO_CART_UTL)
    #    navigationStart = driver.execute_script("return window.performance.timing.navigationStart")
            responseStart = driver.execute_script("return window.performance.timing.responseStart")
            log_out_icon=driver.find_element_by_id("logout-link")
            log_out_icon.click()
#            print(driver.current_url)
            log_out_submit=driver.find_element_by_xpath('/html/body/div[6]/div[4]/button[2]')
            log_out_submit.click()
            
            
            
            domComplete = driver.execute_script("return window.performance.timing.domComplete")
        #    current_url=driver.getCurrentUrl()
            elpased_time=domComplete-responseStart
        checkStatusofURL.saveFlow("log Out",status,elpased_time)
    except Exception as e:
        print(e)
        checkStatusofURL.saveFlow("Log Out","Down",elpased_time)
        
        
def endSession():
    driver.close()  
    driver.quit()

        
    