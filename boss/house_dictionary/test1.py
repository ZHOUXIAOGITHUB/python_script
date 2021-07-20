#-*- encoding=utf8 -*-
#Author:
#Time:  2021/4/16 10:00
#File:  test1.py
# import time
# #
# # from selenium import webdriver
# # driver = webdriver.Chrome()
# # driver.get('https://www.baidu.com/')
# # driver.maximize_window()
# # time.sleep(3)
# # driver.minimize_window()
# # driver.close()
# from depend_lib.element_lib import Use_Browser
# driver = Use_Browser("Chrome")

# from selenium import webdriver
# driver = webdriver.Chrome()
#
# import os
# from selenium import webdriver
# iedriver = r"E:\louxun\PyCharm\bin\pycharm64.exe"
# os.environ["webdriver.ie.driver"] = iedriver
# driver =  webdriver.Ie(iedriver)

# """
# 读取csv文件格式为列表
# :param filepath: 文件路径
# :return: 返回列表格式
# """
# import csv
# class Read:
#     def read(self, file_path):
#         list = []
#         with open(file_path, mode="r", encoding="GBK") as file:
#             # 读取csv,读取的为每一行储存空间
#             read_file = csv.reader(file)
#             # print(read_file)
#             for i in read_file:  # 遍历所得每一行的数据
#                 i = i[1]
#                 list.append(i)
#         return list
# tt = Read().read("house_message.csv")
# print(type(tt[1]), tt[3])



# from xml.dom import minidom
# xm_file =minidom.parse("elements.xml")
# one_tag = xm_file.documentElement["uu"]
# it = one_tag[0]
# tt = it.getAttribute["uu"]
# # two_tag = one_tag.getElementsByTagName("login")[0]
# # # three_tag = two_tag.getElementsByTagName("username")
# # tt = two_tag.childNodes[0]
# print(tt, type(tt), "ee")

# import  xml.dom.minidom
#
# #打开xml文档
# dom = xml.dom.minidom.parse('elements.xml')
#
# #得到文档元素对象
# root = dom.documentElement
# print(root.nodeName)
# print (root.nodeValue)
# print (root.nodeType)
# print (root.ELEMENT_NODE)

# 定义一个读取Xml文件方法
# def ReadXml(FileName, FirstTage, value1, SecondTage, value2, t_tag, vale3, value_n):
#     # 导入来自xml模块dom下的mindom
#     from xml.dom import minidom
#     # 定义路径并赋予变量XmlPath路径中加文件名，传参
#     XmlPath = "elements.xml"
#     # 定义XmlName变量为打开文件
#     XmlName = minidom.parse(XmlPath)
#     # 获取第一个标签
#     OneTag = XmlName.getElementsByTagName(FirstTage)[value1]
#     # 获取第二个标签
#     TwoTag = XmlName.getElementsByTagName(SecondTage)[value2]
#     # 获取第二个标签的节点值并返回
#     three_tag = XmlName.getElementsByTagName(t_tag)[vale3]
#     return TwoTag.childNodes[value_n].nodeVlaue
# tt = ReadXml("elements.xml", "boss", 0, "login", 0,"username",0, 0)
# print(tt)
# print("{}{}".format("ss", "+uu"))
# import time
#
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.get("http://shenzhen.louxuntest.com/")
# driver.maximize_window()
# driver.execute_script("javascript:alert('欢迎来到楼讯！！！')")
# time.sleep(3)
# driver.switch_to_alert().accept()

import sys
sys.path.append('E:\\louxun\\python_script\\boss\\depend_lib')
print(sys.path)