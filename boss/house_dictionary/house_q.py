#-*- encoding=utf8 -*-
#Author:
#Time:  2021/4/14 9:41
#File:  house_dictionary.py
import time
from selenium.webdriver.common.keys import Keys
import pymysql
import sys
from house_dictionary.element_operate import Act_On_Same_Browser
sys.path.append('E:\\louxun\\python_script\\boss\\depend_lib')
# 插入yaml存储用户名称和密码
from depend_lib.operate_file import Rend_File
account_number = Rend_File().read_yaml("..//house_dictionary//login_password", "admin")
sales_message = Rend_File().read_csv("..//house_dictionary//house_message.csv")
class Login(Act_On_Same_Browser):
    def login_page(self):
        driver = self.base_driver
        driver.get_url(sales_message[1])
        # 放大窗口
        driver.max_window()
        driver.send_keys("xpath, //*[@id='app']/div/div[1]/div/form/div[2]/div/div/input", account_number["username"])
        driver.send_keys('xpath, //*[@id="app"]/div/div[1]/div/form/div[3]/div/div/input', account_number["password"])
        # 点击登录
        driver.click("class_name, el-button--primary")
        driver.wait()
class Operate_page(Act_On_Same_Browser):
    def select_house_dic(self):
        driver = self.base_driver
        driver.click('xpath, //*[@id="app"]/div/div[1]/div/div[1]/div/ul/div[2]/li/div/span')
        driver.click('xpath, //*[@id="app"]/div/div[1]/div/div[1]/div/ul/div[2]/li/ul/div[1]/a/li/span')
        driver.switch_iframe('xpath, //*[@id = "app"]/div/div[2]/div[2]/iframe')
        time.sleep(3)
        driver.click('xpath, /html/body/div[2]/div[2]/div/div[1]/div[3]/div[2]/button')
        driver.send_keys('xpath, //*[@id="houseInfoEditDiv"]/form/div/div[1]/div[1]/div[1]/div[1]/div[1]/input', sales_message[2])
        time.sleep(5)
        driver.script("id, houseInfo_ztreeCityArea_edit_1_check")
        driver.click('id, areaNameInput')
        time.sleep(3)
        driver.click('id, houseInfo_ztreeAddressArea_edit_1_check')
        driver.send_keys('xpath, //*[@id="houseInfoEditDiv"]/form/div/div[1]/div[1]/div[2]/div[1]/div/div[1]/input', sales_message[3])
        driver.send_keys('xpath, //*[@id="houseInfoEditDiv"]/form/div/div[1]/div[1]/div[2]/div[2]/input', sales_message[4])
        driver.click('class_name, multiple ')
        time.sleep(3)
        driver.script('xpath, //*[@id="houseInfoEditDiv"]/form/div/div[1]/div[1]/div[3]/div[1]/div/div[2]/div[1]')
        driver.click('id, areaNameInput')
        driver.send_keys('xpath, //*[@id="houseInfoEditDiv"]/form/div/div[1]/div[1]/div[3]/div[2]/input', sales_message[5])
        driver.click('xpath, //*[@id="houseInfoEditDiv"]/form/div/div[1]/div[1]/div[4]/div[2]/div/span')
        time.sleep(3)
        driver.send_keys('xpath, //*[@id="baiduMapWin"]/div[2]/div[1]/div/div[1]/input', sales_message[5])
    def add_house(self):
        driver = self.base_driver
        # 点击查询
        driver.click('xpath, //*[@id="baiduMapWin"]/div[2]/div[1]/div/div[2]/button')
        # 引入键盘机制，查询之后退出地图相当于点了确定（此处界面缺陷）
        driver.send_keys('xpath, //*[@id="baiduMapWin"]/div[2]/div[1]/div/div[2]/button', Keys.ESCAPE)
        driver.click('xpath, //*[@id="houseInfoEditDiv"]/form/div/div[1]/div[1]/div[5]/div[1]/div')
        driver.click('xpath, //*[@id="houseInfoEditDiv"]/form/div/div[1]/div[1]/div[5]/div[1]/div/div[2]/div[1]')
        driver.click('xpath, //*[@id="houseInfoEditDiv"]/form/div/div[1]/div[1]/div[5]/div[1]/div/i')
        driver.send_keys('xpath, //*[@id="houseInfoEditDiv"]/form/div/div[1]/div[1]/div[5]/div[2]/div//input', sales_message[6])
        driver.send_keys('xpath, //*[@id="houseInfoEditDiv"]/form/div/div[1]/div[1]/div[6]/div[2]/input', sales_message[7])
        driver.click('xpath, //*[@id="houseInfoEditDiv"]/form/div/div[1]/div[1]/div[6]/div[1]/div')
        time.sleep(1)
        driver.click('xpath, //*[@id="houseInfoEditDiv"]/form/div/div[1]/div[1]/div[6]/div[1]/div/div[2]/div[1]')
        driver.click('xpath, //*[@id="houseInfoEditDiv"]/form/div/div[1]/div[1]/div[7]/div')
        driver.click('xpath, //*[@id="houseInfoEditDiv"]/form/div/div[1]/div[1]/div[7]/div/div[2]/div[2]')
        time.sleep(2)
        # 关闭下拉窗口
        driver.click('xpath, //*[@id="houseInfoEditDiv"]/form/div/div[1]/div[1]/div[7]/div/i')
        # 小区信息
        driver.send_keys('xpath, //*[@id="houseInfoEditDiv"]/form/div/div[2]/div/div[1]/div[1]/div/input', sales_message[8])
        driver.send_keys('xpath, //*[@id="houseInfoEditDiv"]/form/div/div[2]/div/div[1]/div[2]/div/input', sales_message[9])
        driver.send_keys('xpath, //*[@id="houseInfoEditDiv"]/form/div/div[2]/div/div[2]/div[1]/input', sales_message[10])
        driver.send_keys('xpath, //*[@id="houseInfoEditDiv"]/form/div/div[2]/div/div[2]/div[2]/div/input', sales_message[11])
        driver.send_keys('xpath, //*[@id="houseInfoEditDiv"]/form/div/div[2]/div/div[2]/div[3]/input', sales_message[12])
        driver.send_keys('xpath, //*[@id="houseInfoEditDiv"]/form/div/div[2]/div/div[3]/div/input', sales_message[13] )
        driver.send_keys('xpath, //*[@id="houseInfoEditDiv"]/form/div/div[2]/div/div[4]/div[1]/div/input', sales_message[14])
        driver.send_keys('xpath, //*[@id="houseInfoEditDiv"]/form/div/div[2]/div/div[4]/div[2]/div/input', sales_message[15])
        driver.send_keys('xpath, //*[@id="houseInfoEditDiv"]/form/div/div[2]/div/div[5]/div[1]/div/input', sales_message[16])
        driver.send_keys('xpath, //*[@id="houseInfoEditDiv"]/form/div/div[2]/div/div[5]/div[2]/div/input', sales_message[17])
        driver.send_keys('xpath, //*[@id="houseInfoEditDiv"]/form/div/div[2]/div/div[6]/input', sales_message[18])
        driver.send_keys('xpath, //*[@id="houseInfoEditDiv"]/form/div/div[2]/div/div[7]/div/input',sales_message[19])
        driver.send_keys('xpath, //*[@id="houseInfoEditDiv"]/form/div/div[2]/div/div[8]/div/input', sales_message[20])
        driver.send_keys('xpath, //*[@id="houseInfoEditDiv"]/form/div/div[2]/div/div[9]/div/input', sales_message[21])
        driver.send_keys('xpath, //*[@id="houseInfoEditDiv"]/form/div/div[2]/div/div[10]/div/input', sales_message[22])
        time.sleep(1)
        driver.send_keys('xpath, //*[@id="houseInfoEditDiv"]/form/div/div[2]/div/div[11]/input', sales_message[23])
        driver.send_keys('xpath, //*[@id="houseInfoEditDiv"]/form/div/div[1]/div[2]/div[1]/input', sales_message[24])
        driver.send_keys('xpath, //*[@id="houseInfoEditDiv"]/form/div/div[1]/div[2]/div[2]/input', sales_message[25])
        driver.send_keys('xpath, //*[@id="houseInfoEditDiv"]/form/div/div[1]/div[2]/div[4]/input', sales_message[26])
        # 点击保存
        driver.click('xpath, /html/body/div[2]/div[2]/div/div[5]/button')
        # 退出编辑
        driver.click('xpath, /html/body/div[2]/div[2]/div/div[1]/button')
        driver.send_keys('xpath, /html/body/div[2]/div[2]/div/div[1]/div[1]/div[2]/div[3]/input', sales_message[3])
        driver.click('xpath, /html/body/div[2]/div[2]/div/div[1]/div[1]/div[1]/div[4]/button[1]')
        time.sleep(2)
        try:
            house_text = driver.get_text('xpath, //*[@id="houseTable"]/tbody/tr/td[3]')
        except:
            house_text = ""
        if house_text == house_text:
            print("保存成功",1)
        else:
            print("保存失败",1)
        # 点击审核
        driver.click('xpath, //*[@id="houseTable"]/tbody/tr[1]/td[17]/div/i[1]')
        time.sleep(2)
        driver.click('xpath, /html/body/div[2]/div[2]/div/div[5]/button[1]')
        driver.click('xpath, /html/body/div[2]/div[2]/div/div[1]/div[3]/div[1]/button[2]')
        driver.clear_value('xpath, /html/body/div[2]/div[2]/div/div[1]/div[1]/div[2]/div[3]/input')
        driver.send_keys('xpath, /html/body/div[2]/div[2]/div/div[1]/div[1]/div[2]/div[3]/input', sales_message[3])
        driver.click('xpath, /html/body/div[2]/div[2]/div/div[1]/div[1]/div[1]/div[4]/button[1]')
        get_house_name = driver.get_text('xpath, //*[@id="houseTable"]/tbody/tr[1]/td[3]')
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

