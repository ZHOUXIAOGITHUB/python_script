#-*- encoding=utf8 -*-
#Author:
#Time:  2021/5/20 15:32
#File:  element_operate.py
from selenium import webdriver
class Element_Operate():
    def __init__(self):
        self.driver = webdriver.Chrome()
    def element_xpath_click(self, xpath_value):
        self.driver.find_element_by_xpath(xpath_value).click()

    def element_xpath_send_keys(self, xpath, input_value):
        self.driver.find_element_by_xpath(xpath).send_keys(input_value)

    def get_url(self, url):
        self.driver.get(url)

    def max_window(self):
        self.driver.maximize_window()

    def close_windows(self):
        self.driver.close()

    def element_name_click(self, name_value):
        self.driver.find_element_by_class_name(name_value).click()

    def element_name_send_keys(self, name_value, input_value):
        self.driver.find_element_by_class_name(name_value).send_keys(input_value)

    def wait(self):
        self.driver.implicitly_wait(10)
    
    def switch_iframe(self, element, element_value):
        location_element = self.driver.find_element(element, element_value)
        self.driver.switch_to.frame(location_element)

    def script(self, element, element_value):
        location_element = self.driver.find_element(element, element_value)
        self.driver.execute_script("arguments[0].click();", location_element)

    def element_id_click(self, id_value):
        self.driver.find_element_by_id(id_value).click()

    def get_text(self, element, element_value):
        location_element = self.driver.find_element(element, element_value)
        return location_element.text

    def clear_value(self, element, element_value):
        location_element = self.driver.find_element(element, element_value)
        location_element.clear()











