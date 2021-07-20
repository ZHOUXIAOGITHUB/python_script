#-*- encoding=utf8 -*-
#Author:
#Time:  2021/5/20 15:32
#File:  element_operate.py
from selenium import webdriver
from selenium.webdriver.common.by import By
class Element_Operate():
    def __init__(self, browser):
        try:
            if browser == "Chrome" or "C":
                driver = webdriver.Chrome()
            elif browser == "Ie" or "I":
                driver = webdriver.Ie()
            elif browser == "Firefox" or "F":
                driver = webdriver.Firefox()
            else:
                pass
            self._base_driver = driver
        except:
            raise NameError("请输入正确浏览器")

    def _convert_selector_to_locator(self, selector):
        """
        获取元素和值
        """
        select_element = selector.split(",")[0].strip()
        select_value = selector.split(",")[1].strip()
        if select_element == "id" or select_element == "i":
            locator = (By.ID, select_value)
        elif select_element == "partial_link_text" or select_element == "p_l_text":
            locator = (By.PARTIAL_LINK_TEXT, select_value)
        elif select_element == "class_name" or select_element == "c_name":
            locator = (By.CLASS_NAME, select_value)
        elif select_element == "name" or select_element == "n":
            locator = (By.NAME, select_value)
        elif select_element == "tag_name" or select_element == "t_name":
            locator = (By.TAG_NAME, select_value)
        elif select_element == "link_text" or select_element == "l_text":
            locator = (By.LINK_TEXT, select_value)
        elif select_element == "xpath" or select_element == "x":
            locator = (By.XPATH, select_value)
        elif select_element == "css_selector" or select_element == "c_selector":
            locator = (By.CSS_SELECTOR, select_value)
        else:
            raise NameError("请输入正确的定位元素")
        return locator

    def _locate_element(self, selector):
        """
        定位元素
        """
        locator = self._convert_selector_to_locator(selector)
        find_ele = self._base_driver.find_element(*locator)
        return find_ele


    def click(self, selector):
        ele = self._locate_element(selector)
        ele.click()
    def send_keys(self, selector, text):
        self._locate_element(selector).send_keys(text)

    def get_url(self, url):
        self._base_driver.get(url)

    def max_window(self):
        self._base_driver.maximize_window()

    def close_windows(self):
        self._base_driver.close()

    def wait(self):
        self._base_driver.implicitly_wait(10)

    def switch_iframe(self, selector):
        location_element = self._locate_element(selector)
        self._base_driver.switch_to.frame(location_element)

    def script(self, selector):
        location_element = self._locate_element(selector)
        self._base_driver.execute_script("arguments[0].click();", location_element)

    def get_text(self, selector):
        location_element = self._locate_element(selector)
        return location_element.text

    def clear_value(self, selector):
        location_element = self._locate_element(selector)
        location_element.clear()
class Act_On_Same_Browser:
    def __init__(self, driver: Element_Operate):
        self.base_driver = driver











