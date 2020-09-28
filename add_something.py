#-*- encoding=utf8 -*-
#Author:
#Time:  2019/12/13 13:04
#File:  add_something.py

from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.implicitly_wait(10)
#登陆案场台
driver.get("http://xf.test.louxun.com/broker/loginProcess")
driver.maximize_window()
driver.find_element_by_name("j_username").clear()
driver.find_element_by_name("j_username").send_keys("15888430775")
# driver.find_element_by_name("password").clear()
driver.find_element_by_name("j_password").send_keys("123456")
driver.find_element_by_id("loginButS").click()
time.sleep(5)
# 点击案场管理
driver.find_element_by_xpath("/html/body/div[2]/div[1]/ul/li[3]/a/span[1]").click()
# 点击成交管理
driver.find_element_by_link_text("成交管理").click()
# 切换框架
driver.switch_to.frame(driver.find_element_by_xpath('//*[@id="framecenter"]/div[2]/div[2]/iframe'))
time.sleep(2)
cj=driver.find_element_by_xpath('//*[@id="tableContainer|2|r1001|c104"]/div/a').text
driver.find_element_by_xpath('//*[@id="dealAttachmentManage"]/span').click()
driver.switch_to.frame("OpendealAttachment")
time.sleep(3)
driver.find_element_by_xpath('//*[@id="transactionNumber"]').send_keys(cj)
driver.find_element_by_xpath('//*[@id="search"]/span').click()
driver.find_element_by_link_text('编辑').click()
driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div/div').send_keys(r"E:\louxun\测试用图\u=915820793,2813063642&fm=11&gp=0.jpg")
# driver.close()