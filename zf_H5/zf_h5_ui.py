#-*- encoding=utf8 -*-
#Author:
#Time:  2021/1/21 10:24
#File:  zf_h5_ui.py


from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
import win32api,win32con # 安装 pywin32依赖库
mobileEmulation = {'deviceName': 'iPhone 6'}
option = webdriver.ChromeOptions()
option.add_argument("--auto-open-devtools-for-tabs")

driver = webdriver.Chrome(chrome_options=option)
driver.implicitly_wait(10)
driver.get("https://m.louxun.com")
driver.maximize_window()
# driver.get("@@@@@@@")
time.sleep(3)
# 按下键盘
win32api.keybd_event(17, 0, 0, 0)
win32api.keybd_event(16, 0, 0, 0)
win32api.keybd_event(77, 0, 0, 0)
time.sleep(1)
# 松开键盘
win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)
win32api.keybd_event(16, 0, win32con.KEYEVENTF_KEYUP, 0)
win32api.keybd_event(77, 0, win32con.KEYEVENTF_KEYUP, 0)
time.sleep(3)
option.add_experimental_option("mobileEmulation", mobileEmulation)
print("pass")
# try:
#     driver.find_element_by_xpath('//*[@id="__layout"]/div/section/div[3]/div[2]/div[2]').click()
#     driver.find_element_by_xpath('//*[@id="__layout"]/div/section/div[7]/div/div[3]/div[1]').click()
#     print("erro")
# except:
driver.find_element_by_class_name('s-btn').click()
print("erro1")
