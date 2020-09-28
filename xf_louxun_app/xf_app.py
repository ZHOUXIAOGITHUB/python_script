#-*- encoding=utf8 -*-
#Author:
#Time:  2020/7/29 14:34
#File:  xf_app.py
# from appium import webdriver
# decried_caps = {
#     "platformName": "Android",
#     "platformVersion": "5.1.1",
#     "deviceName": "127.0.0.1:62001",
#     "appPackage": "com.xinfang.louxun",
#     "appActivity": "com.xinfang.louxun.ui.SplashActivity",
#     "resetKeyboard": "true",
#     "unicodeKeyboard": "true",
#                  }
# driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", decried_caps)
from xf_louxun_app.dependent_lib import App_Dependent_Lib
driver = App_Dependent_Lib()
# driver.implicitly_wait(10)
driver.wait()
# driver.swipe(700, 1000, 200, 1000)
driver.swipe(700, 1000, 200, 1000)
driver.swipe(700, 1000, 200, 1000)
# driver.swipe(700, 1000, 200, 1000)
# driver.find_element_by_id("com.xinfang.louxun:id/next_tv").click()
driver.find_ele_id_cilck("com.xinfang.louxun:id/next_tv")
# driver.find_ele_id_cilck("com.xinfang.louxun:id/finish_bt")
import time
# time.sleep(5)
# driver.find_ele_id_cilck("com.xinfang.louxun:id/search_tv")
# driver.find_element_by_id("com.xinfang.louxun:id/finish_bt").click()
# driver.find_element_by_id("com.xinfang.louxun:id/close_img").click()
# driver.find_element_by_id("com.xinfang.louxun:id/search_tv").click()
# driver.find_element_by_id("com.xinfang.louxun:id/search_et").send_keys("南山区")
driver.find_ele_id_send("com.xinfang.louxun:id/search_et", "南山区")
# driver.find_element_by_id("com.xinfang.louxun:id/house_address_tv").click()
driver.find_ele_id_cilck("com.xinfang.louxun:id/house_address_tv")


