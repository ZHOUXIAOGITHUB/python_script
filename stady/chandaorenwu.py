#-*- encoding=utf8 -*-
#Author:
#Time:  2020/6/29 9:45
#File:  chandaorenwu.py
from selenium import webdriver
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('http://10.1.220.18/zentao/user-login.html')
driver.maximize_window()
driver.find_element_by_name('account').send_keys('zgh')
driver.find_element_by_name('password').send_keys('123@louxun')
driver.find_element_by_id('submit').click()
driver.find_element_by_link_text('项目').click()
driver.find_element_by_link_text('任务').click()
driver.find_element_by_link_text('建任务').click()
driver.find_element_by_id("name").send_keys(input("请输入任务名称： "))