#-*- encoding=utf8 -*-
#Author:
#Time:  2020/9/10 15:47
#File:  zf_wap_login.py
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("http://10.1.220.5:8017/chaozhou/personalCenter/register")
time.sleep(3)
driver.maximize_window()
# 输入账号和密码
driver.find_element_by_xpath('//*[@id="__layout"]/div/section/div[2]/div[1]/input').send_keys("lll")
driver.find_element_by_xpath('//*[@id="__layout"]/div/section/div[2]/div[3]/input').send_keys("ooo")
# 点击获取验证码
driver.find_element_by_xpath('//*[@id="__layout"]/div/section/div[2]/div[2]/div[1]').click()
# 登录获取短信平台
driver.get("https://www.yunpian.com/entry")
driver.find_element_by_name('mobile').send_keys("账号")
driver.find_element_by_name('password').send_keys('密码')
driver.find_element_by_xpath('//*[@id="__layout"]/div/div[1]/div/div/div[2]/div/div[1]').click()
driver.find_element_by_xpath('//*[@id="__layout"]/div/section/div[2]/div[2]/input').send_keys("验证码")
