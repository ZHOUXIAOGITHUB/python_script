#-*- encoding=utf8 -*-
#Author:
#Time:  2021/4/21 15:59
#File:  element_lib.py
from selenium import webdriver
# class Use_Browser():
#     def __init__(self, browser):
#         try:
#             if browser == "Chrome" or "C":
#                 driver = webdriver.Chrome()
#             if browser == "Ie" or "I":
#                 driver = webdriver.Ie()
#             if browser == "Safari" or "S":
#                 driver = webdriver.Safari()
#             if browser == "Firefox" or "F":
#                 driver = webdriver.Firefox()
#             self._base_driver = driver
#         except:
#             raise NameError("请输入正确浏览器")

from selenium import webdriver
class Use_Browser():
    def __init__(self, browser):
        try:
            if browser == "Chrome" or "C":
                driver = webdriver.Chrome()
            if browser == "Ie" or "I":
                driver = webdriver.Ie()
            if browser == "Safari" or "S":
                driver = webdriver.Safari()
            if browser == "Firefox" or "F":
                driver = webdriver.Firefox()
            self._base_driver = driver
        except:
            raise NameError("请输入正确浏览器")

