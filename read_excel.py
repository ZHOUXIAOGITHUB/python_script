#-*- encoding=utf8 -*-
#Author:
#Time:  2020/6/9 14:32
#File:  read_excel.py


# 1. 打开一个excel文档, class 'openpyxl.workbook.workbook.Workbook'实例化出来的对象
# wb = openpyxl.load_workbook(r'C:\Users\zgh77\Desktop\test.xls')
# print(wb, type(wb))
#
# import csv
# with open('test.csv', 'r', encoding="utf8") as f:
#      reader = csv.reader(f)
#      print(type(reader))
#
#      for row in reader:
#          print(row)

import xlrd
table = xlrd.open_workbook("test.xls", "rb")
print(table)









