#-*- encoding=utf8 -*-
#Author:
#Time:  2020/9/10 16:02
#File:  zf_message_test.py

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.yunpian.com/entry")
driver.maximize_window()
# 登录短信平台
driver.find_element_by_name('mobile').send_keys("18565620423")
driver.find_element_by_name('password').send_keys('qzj7758991')
driver.find_element_by_xpath('//*[@id="__layout"]/div/div[1]/div/div/div[2]/div/div[1]').click()
# 关闭弹窗涉及到frame
path = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div/iframe")
driver.switch_to_frame(path)
# 插入键盘机制
driver.find_element_by_class_name("src-pages-dashboard-ad-dialog-introduce-dialog-index__btn").send_keys(Keys.ESCAPE)
driver.switch_to.default_content()
# 点击国内短信
driver.find_element_by_class_name('el-submenu__title').click()
time.sleep(3)
P_xpath = driver.find_element_by_xpath("//*[@class = 'el-menu']/../ul/li[4]")
# # 导入鼠标机制，点击不可见元素
# text = ActionChains(driver).move_to_element(P_xpath).perform()
# text1 = ActionChains(driver).click(P_xpath).perform()
driver.execute_script("arguments[0].click();", P_xpath)
# driver.find_element_by_xpath(P_xpath).send_keys(Keys.ENTER)
# 定位输入框
M_xpath = '/html/body/div[1]/div[2]/div[2]/div/div/div/div[2]/div/div/div[2]/div[1]/div/div[2]/form/div[4]/div/div/input'
# driver.find_element_by_xpath(M_xpath).send_keys("17866669999")
# search_button_path = "/html/body/div[1]/div[2]/div[2]/div/div/div/div[2]/div/div/div[2]/div[1]/div/div[2]/form/div[6]/div/button"
# driver.find_element_by_xpath(search_button_path).click()
# 获取查询后的第一条短信
first_mess = "/html/body/div[1]/div[2]/div[2]/div/div/div/div[2]/div/div/div[2]/div[1]/div/div[5]/div[1]/div[3]/table/tbody/tr[1]/td[3]/div/div/span[1]"
get_message = driver.find_element_by_xpath(first_mess).text
message_str = str(get_message)
# 获取注册短信的验证码
auth_code = get_message[21:25]
print(get_message[21:25])

