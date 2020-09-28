#-*- encoding=utf8 -*-
#Author:
#Time:  2020/9/10 16:02
#File:  zf_message_test.py

from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.yunpian.com/entry")
driver.maximize_window()
# 登录短信平台
driver.find_element_by_name('mobile').send_keys("18565620423")
driver.find_element_by_name('password').send_keys('qzj7758991')
driver.find_element_by_xpath('//*[@id="__layout"]/div/div[1]/div/div/div[2]/div/div[1]').click()
# 关闭弹窗涉及到frame
# driver.find_element_by_xpath('//*[@id="container"]/div[2]/div/div[2]/div/div[2]/button/span/i/svg').click()
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/ul/li[2]/ul/li[1]/div/span').click()
# 点击短信记录
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/ul/li[2]/ul/li[1]/ul/li[4]').click()
P_xpath = "/html/body/div[1]/div[2]/div[2]/div/div/div/div[2]/div/div/div[2]/div[1]/div/div[2]/form/div[4]/div/div/input"
S_xpath = "/html/body/div[1]/div[2]/div[2]/div/div/div/div[2]/div/div/div[2]/div[1]/div/div[2]/form/div[6]/div/button"
driver.find_element_by_xpath(P_xpath).send_keys("17866669999")
driver.find_element_by_xpath(S_xpath).click()
M_xpath = '/html/body/div[1]/div[2]/div[2]/div/div/div/div[2]/div/div/div[2]/div[1]/div/div[5]/div[1]/div[3]/table/tbody/tr/td[3]/div/div/span[1]'
get_text = driver.find_element_by_xpath(M_xpath).text
message = []
message.append(get_text)
print(message)



