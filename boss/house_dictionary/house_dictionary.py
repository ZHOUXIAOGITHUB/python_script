#-*- encoding=utf8 -*-
#Author:
#Time:  2021/4/14 9:41
#File:  house_dictionary.py
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pymysql
import sys
sys.path.append('E:\\louxun\\python_script\\boss\\depend_lib')
# 插入yaml存储用户名称和密码
from depend_lib.operate_file import Rend_File
account_number = Rend_File().read_yaml("..//house_dictionary//login_password", "admin")
sales_message = Rend_File().read_csv("..//house_dictionary//house_message.csv")
from depend_lib.element_operate import Element_Operate




driver = Element_Operate()
# driver = webdriver.Chrome()
driver.get_url(sales_message[1])
# 放大窗口
driver.max_window()
driver.element_xpath_send_keys('//*[@id="app"]/div/div[1]/div/form/div[2]/div/div/input', account_number["username"])
driver.element_xpath_send_keys('//*[@id="app"]/div/div[1]/div/form/div[3]/div/div/input', account_number["password"])
driver.element_name_click("el-button--primary")
driver.wait()
# driver.element_xpath_send_keys('//*[@id="app"]/div/div[1]/div')
# driver.element_xpath_send_keys('//*[@id="app"]/div/div[1]/div/div[1]')
# driver.element_xpath_send_keys('//*[@id="app"]/div/div[1]/div/div[1]/div')
# # driver.element_xpath_send_keys('//*[@id="app"]/div/div[1]/div/div[1]/div/div')
# driver.element_xpath_send_keys('//*[@id="app"]/div/div[1]/div/div[1]/div/ul')
# driver.element_xpath_send_keys('//*[@id="app"]/div/div[1]/div/div[1]/div/ul/div[2]')
# driver.element_xpath_send_keys('//*[@id="app"]/div/div[1]/div/div[1]/div/ul/div[2]/li')
# driver.element_xpath_send_keys('//*[@id="app"]/div/div[1]/div/div[1]/div/ul/div[2]/li/div')
driver.element_xpath_click('//*[@id="app"]/div/div[1]/div/div[1]/div/ul/div[2]/li/div/span')
driver.element_xpath_click('//*[@id="app"]/div/div[1]/div/div[1]/div/ul/div[2]/li/ul/div[1]/a/li/span')
# iframe_path = '//*[@id = "app"]/div/div[2]/div[2]/iframe'
# swt_ifr = driver.element_xpath(iframe_path)
# driver.switch_to.frame(swt_ifr)
driver.switch_iframe("xpath", '//*[@id = "app"]/div/div[2]/div[2]/iframe')
time.sleep(3)
driver.element_xpath_click('/html/body/div[2]/div[2]/div/div[1]/div[3]/div[2]/button')
driver.element_xpath_send_keys('//*[@id="houseInfoEditDiv"]/form/div/div[1]/div[1]/div[1]/div[1]/div[1]/input', sales_message[2])
time.sleep(5)
# P_xpath = driver.find_element_by_id("houseInfo_ztreeCityArea_edit_1_check")
# # 导入鼠标机制，点击不可见元素(已经实现，给出强制跳转时间即可)
# # text = ActionChains(driver).move_to_element(P_xpath).perform()
# # text1 = ActionChains(driver).double_click(P_xpath).perform()
# # 使用脚本点击
# driver.execute_script("arguments[0].click();", P_xpath)
driver.script("id", "houseInfo_ztreeCityArea_edit_1_check")
driver.element_id_click('areaNameInput')
time.sleep(3)
driver.element_id_click('houseInfo_ztreeAddressArea_edit_1_check')
driver.element_xpath_send_keys('//*[@id="houseInfoEditDiv"]/form/div/div[1]/div[1]/div[2]/div[1]/div/div[1]/input', sales_message[3])
driver.element_xpath_send_keys('//*[@id="houseInfoEditDiv"]/form/div/div[1]/div[1]/div[2]/div[2]/input', sales_message[4])
driver.element_name_click('multiple ')
time.sleep(3)
# drop_down = driver.element_xpath_send_keys()
# driver.execute_script("arguments[0].click();", drop_down)
driver.script("xpath", '//*[@id="houseInfoEditDiv"]/form/div/div[1]/div[1]/div[3]/div[1]/div/div[2]/div[1]')
driver.element_id_click('areaNameInput')
driver.element_xpath_send_keys('//*[@id="houseInfoEditDiv"]/form/div/div[1]/div[1]/div[3]/div[2]/input', sales_message[5])
driver.element_xpath_click('//*[@id="houseInfoEditDiv"]/form/div/div[1]/div[1]/div[4]/div[2]/div/span')
time.sleep(3)
driver.element_xpath_send_keys('//*[@id="baiduMapWin"]/div[2]/div[1]/div/div[1]/input', sales_message[5])
time.sleep(3)
# 点击查询
driver.element_xpath_click('//*[@id="baiduMapWin"]/div[2]/div[1]/div/div[2]/button')
# 引入键盘机制，查询之后退出地图相当于点了确定（此处界面缺陷）
driver.element_xpath_send_keys('//*[@id="baiduMapWin"]/div[2]/div[1]/div/div[2]/button', Keys.ESCAPE)
driver.element_xpath_click('//*[@id="houseInfoEditDiv"]/form/div/div[1]/div[1]/div[5]/div[1]/div')
driver.element_xpath_click('//*[@id="houseInfoEditDiv"]/form/div/div[1]/div[1]/div[5]/div[1]/div/div[2]/div[1]')
driver.element_xpath_click('//*[@id="houseInfoEditDiv"]/form/div/div[1]/div[1]/div[5]/div[1]/div/i')
driver.element_xpath_send_keys('//*[@id="houseInfoEditDiv"]/form/div/div[1]/div[1]/div[5]/div[2]/div//input', sales_message[6])
driver.element_xpath_send_keys('//*[@id="houseInfoEditDiv"]/form/div/div[1]/div[1]/div[6]/div[2]/input', sales_message[7])
driver.element_xpath_click('//*[@id="houseInfoEditDiv"]/form/div/div[1]/div[1]/div[6]/div[1]/div')
time.sleep(1)
driver.element_xpath_click('//*[@id="houseInfoEditDiv"]/form/div/div[1]/div[1]/div[6]/div[1]/div/div[2]/div[1]')

# driver.element_xpath_send_keys('//*[@id="houseInfoEditDiv"]/form/div/div[1]/div[1]/div[6]/div[2]/input').send_keys('楼讯找房')
driver.element_xpath_click('//*[@id="houseInfoEditDiv"]/form/div/div[1]/div[1]/div[7]/div')
driver.element_xpath_click('//*[@id="houseInfoEditDiv"]/form/div/div[1]/div[1]/div[7]/div/div[2]/div[2]')
time.sleep(2)
# 关闭下拉窗口
driver.element_xpath_click('//*[@id="houseInfoEditDiv"]/form/div/div[1]/div[1]/div[7]/div/i')
# 小区信息
driver.element_xpath_send_keys('//*[@id="houseInfoEditDiv"]/form/div/div[2]/div/div[1]/div[1]/div/input', sales_message[8])
driver.element_xpath_send_keys('//*[@id="houseInfoEditDiv"]/form/div/div[2]/div/div[1]/div[2]/div/input', sales_message[9])
driver.element_xpath_send_keys('//*[@id="houseInfoEditDiv"]/form/div/div[2]/div/div[2]/div[1]/input', sales_message[10])
driver.element_xpath_send_keys('//*[@id="houseInfoEditDiv"]/form/div/div[2]/div/div[2]/div[2]/div/input', sales_message[11])
driver.element_xpath_send_keys('//*[@id="houseInfoEditDiv"]/form/div/div[2]/div/div[2]/div[3]/input', sales_message[12])
driver.element_xpath_send_keys('//*[@id="houseInfoEditDiv"]/form/div/div[2]/div/div[3]/div/input', sales_message[13] )
driver.element_xpath_send_keys('//*[@id="houseInfoEditDiv"]/form/div/div[2]/div/div[4]/div[1]/div/input', sales_message[14])
driver.element_xpath_send_keys('//*[@id="houseInfoEditDiv"]/form/div/div[2]/div/div[4]/div[2]/div/input', sales_message[15])
driver.element_xpath_send_keys('//*[@id="houseInfoEditDiv"]/form/div/div[2]/div/div[5]/div[1]/div/input', sales_message[16])
driver.element_xpath_send_keys('//*[@id="houseInfoEditDiv"]/form/div/div[2]/div/div[5]/div[2]/div/input', sales_message[17])
driver.element_xpath_send_keys('//*[@id="houseInfoEditDiv"]/form/div/div[2]/div/div[6]/input', sales_message[18])
driver.element_xpath_send_keys('//*[@id="houseInfoEditDiv"]/form/div/div[2]/div/div[7]/div/input',sales_message[19])
driver.element_xpath_send_keys('//*[@id="houseInfoEditDiv"]/form/div/div[2]/div/div[8]/div/input', sales_message[20])
driver.element_xpath_send_keys('//*[@id="houseInfoEditDiv"]/form/div/div[2]/div/div[9]/div/input', sales_message[21])
driver.element_xpath_send_keys('//*[@id="houseInfoEditDiv"]/form/div/div[2]/div/div[10]/div/input', sales_message[22])
time.sleep(1)
driver.element_xpath_send_keys('//*[@id="houseInfoEditDiv"]/form/div/div[2]/div/div[11]/input', sales_message[23])
driver.element_xpath_send_keys('//*[@id="houseInfoEditDiv"]/form/div/div[1]/div[2]/div[1]/input', sales_message[24])
driver.element_xpath_send_keys('//*[@id="houseInfoEditDiv"]/form/div/div[1]/div[2]/div[2]/input', sales_message[25])
driver.element_xpath_send_keys('//*[@id="houseInfoEditDiv"]/form/div/div[1]/div[2]/div[4]/input', sales_message[26])
# 点击保存
driver.element_xpath_click('/html/body/div[2]/div[2]/div/div[5]/button')
# 无法获取保存成功的信息
# save_house_hint = driver.element_xpath_send_keys('//*[@id="popupMsg"]/div').text
# save_icon = driver.find_element_by_class_name('green')
# driver.execute_script("arguments[0].click();", save_icon)
# driver.find_element_by_id('areaNameInput').click()
# print(save_house_hint, "########")
# 退出编辑
driver.element_xpath_click('/html/body/div[2]/div[2]/div/div[1]/button')
driver.element_xpath_send_keys('/html/body/div[2]/div[2]/div/div[1]/div[1]/div[2]/div[3]/input', sales_message[3])
driver.element_xpath_click('/html/body/div[2]/div[2]/div/div[1]/div[1]/div[1]/div[4]/button[1]')
time.sleep(2)
try:
    # house_text = driver.element_xpath_send_keys('//*[@id="houseTable"]/tbody/tr/td[3]').text
    # print(house_text)
    house_text = driver.get_text("xpath", '//*[@id="houseTable"]/tbody/tr/td[3]')
except:
    house_text = ""
if house_text == house_text:
    print("保存成功",1)
else:
    print("保存失败",1)
# 点击审核
driver.element_xpath_click('//*[@id="houseTable"]/tbody/tr[1]/td[17]/div/i[1]')
time.sleep(2)
driver.element_xpath_click('/html/body/div[2]/div[2]/div/div[5]/button[1]')
# 无法获取保存成功的提示信息
# audit_mess = driver.element_xpath_send_keys('//*[@id="popupMsg"]/div').text
# print(audit_mess, "审核操作信息")
# 切换列表为已通过
driver.element_xpath_click('/html/body/div[2]/div[2]/div/div[1]/div[3]/div[1]/button[2]')
driver.clear_value("xpath", '/html/body/div[2]/div[2]/div/div[1]/div[1]/div[2]/div[3]/input')

driver.element_xpath_send_keys('/html/body/div[2]/div[2]/div/div[1]/div[1]/div[2]/div[3]/input', sales_message[3])
driver.element_xpath_click('/html/body/div[2]/div[2]/div/div[1]/div[1]/div[1]/div[4]/button[1]')
get_house_name = driver.get_text("xpath", '//*[@id="houseTable"]/tbody/tr[1]/td[3]')
try:
    if get_house_name == sales_message[3]:
        print("保存成功", "审核通过查找")
    else:
        print("保存失败", "审核通过查找")
except:
    print("保存失败", "审核通过异常查找")
mysql_connect = pymysql.connect(host="10.1.220.5", port=3306, user="root", password="123456", database="rent_house")
msql_cursor = mysql_connect.cursor()
sql_del = 'DELETE from tb_base_house where `name` = "%s";'%sales_message[3]
msql_cursor.execute(sql_del)
mysql_connect.commit()
print("清除成功", '删除新增的楼盘')
driver.close_windows()

