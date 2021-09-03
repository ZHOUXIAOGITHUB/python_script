#-*- encoding=utf8 -*-
#Author:
#Time:  2020/11/3 14:53
#File:  str_split.py
from selenium import webdriver

mobileEmulation = {'deviceName' :'Galaxy S5'}

option  = webdriver.ChromeOptions()

option.add_experimental_option('mobileEmulation', mobileEmulation)

chrome = webdriver.Chrome(options=option)


