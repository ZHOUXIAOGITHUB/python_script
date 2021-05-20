# #-*- encoding=utf8 -*-
# #Author:
# #Time:  2021/4/14 17:51
# #File:  kaoqinbiao.py
# import xlrd
# #
# # ExcelPath = "数据导出.xlsx"
# # # 打开excle赋予变量OpenFile
# # OpenFile = xlrd.open_workbook(ExcelPath)
# 传sheet页和行和列的值,并返回excle表的sheet页和行和列的值
from ast import literal_eval

import parameterized as parameterized
import xlwt
from house_dictionary.test import PythonHelpApi
    # 创建一个workbook 设置编码
workbook = xlwt.Workbook(encoding='utf-8')
    # 创建一个worksheet
worksheet = workbook.add_sheet('kao_qin')
for i in range(1,35):
    tt = PythonHelpApi().ReadExcle("Sheet0",i,1)
    global false, null, true
    false = null = true = ''
    # print(type(tt),tt)
    tt1 = eval(tt)
    # print(tt,type(tt))
    # print(type(tt1), tt1)
    print(tt1[0]["value"])
    print(tt1[1]["value"])
    print(tt1[2]["value"])
    list = []
    list.append(tt1[0]["value"])
    list.append(tt1[1]["value"])
    list.append(tt1[2]["value"])

    # 写入excel
    # 参数对应 行, 列, 值
    worksheet.write(i, 0, label=list)
# 保存
workbook.save('Excel_kao_qin.xls')

import json
# from ast import literal_eval
#
# wu ='[{"ju":"oo"}]'
# print(type(wu), wu)
#
#
#
#
# wu1 = literal_eval(wu)
# print(wu1,type(wu1))



# target_list = json.loads(wu)
# print(type(target_list))
# print(target_list)