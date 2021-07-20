#-*- encoding=utf8 -*-
#Author:
#Time:  2021/4/21 15:59
#File:  element_lib.py
from selenium import webdriver
from selenium.webdriver.common.by import By
class Use_Browser():
    def __init__(self, browser):
        try:
            if browser == "Chrome" or "C":
                driver = webdriver.Chrome()
            elif browser == "Ie" or "I":
                driver = webdriver.Ie()
            elif browser == "Safari" or "S":
                driver = webdriver.Safari()
            elif browser == "Firefox" or "F":
                driver = webdriver.Firefox()
            else:
                print("请输入正确浏览器")
            self._base_driver = driver
        except:
            raise NameError("请检查浏览器")

    def _convert_selector_to_locator(self, selector):
        """
        获取元素和值
        """
        select_element = selector.split(",")[0].strip()
        select_value = selector.split(",")[1].strip()
        if select_element == "id" or "i":
            locator = (By.ID, select_value)
        elif select_element == "partial_link_text" or "p_l_text":
            locator = (By.PARTIAL_LINK_TEXT, select_value)
        elif select_element == "class_name" or "c_name":
            locator = (By.CLASS_NAME, select_value)
        elif select_element == "name" or "n":
            locator = (By.NAME, select_value)
        elif select_element == "tag_name" or "t_name":
            locator = (By.TAG_NAME, select_value)
        elif select_element == "link_text" or "l_text":
            locator = (By.LINK_TEXT, select_value)
        elif select_element == "xpath" or "x":
            locator = (By.XPATH, select_value)
        elif select_element == "css_selector" or "c_selector":
            locator = (By.CSS_SELECTOR, select_value)
        else:
            raise NameError("请输入正确的定位元素")
        return locator

