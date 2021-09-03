#-*- encoding=utf8 -*-
#Author:
#Time:  2020/6/29 14:40
#File:  voting.py

# age = 19
# if age >= 18:
#     print("You are old enough to vote!")
#     print("Have you registered to vote yet?")
# age = 17
# if age >= 18:
#     print("You are old enough to vote!")
#     print("Have you registered to vote yet?")
# else:
#     print("Sorry, You are too yong to vote.")
#     print("Please register to vite as soon as you turn 18!")
#

from selenium import webdriver
from time import sleep

#{'deviceName': '必须与谷歌浏览器的值一致'}
mobileEmulation = {'deviceName': 'iPhone 6/7/8'}
options = webdriver.ChromeOptions()
options.add_argument("--auto-open-devtools-for-tabs")
options.add_experimental_option('mobileEmulation', mobileEmulation)

driver = webdriver.Chrome( chrome_options=options)
sleep(2)

driver.get('http://m.baidu.com')

sleep(3)
driver.close()
