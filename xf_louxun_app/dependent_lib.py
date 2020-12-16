#-*- encoding=utf8 -*-
#Author:
#Time:  2020/7/31 14:22
#File:  dependent_lib.py
from appium import webdriver

# app依赖库
class App_Dependent_Lib:
    def __init__(self):
        # decried_caps = {
        #     "platformName": "Android",
        #     "platformVersion": "5.1.1",
        #     "deviceName": "127.0.0.1:62001",
        #     "appPackage": "com.xinfang.louxun",
        #     "appActivity": "com.xinfang.louxun.ui.SplashActivity",
        #     "resetKeyboard": "true",
        #     "unicodeKeyboard": "true",
        # }
        decried_caps = {
            "platformName": "Android",
            "platformVersion": "5.1.1",
            "deviceName": "127.0.0.1:62001",
            "appPackage": "com.xinfang.louxun",
            "appActivity": "com.xinfang.louxun.ui.SplashActivity",
            "resetKeyboard": "true",
            "unicodeKeyboard": "true",
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", decried_caps)
    def wait(self):
        self.driver.implicitly_wait(10)

    #滑动函数
    def swipe(self, x1, y1, x2, y2):
        self.driver.swipe(x1, y1, x2, y2)

    def find_ele_id_cilck(self, ele):
        self.driver.find_element_by_id(ele).click()
    def find_ele_id_send(self, ele, value):
        self.driver.find_element_by_id(ele).send_keys(value)

# web依赖库
class Web_Dependent_Lib:
    def __init__(self):
        
