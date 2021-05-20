# #-*- encoding=utf8 -*-
# #Author:
# #Time:  2021/4/14 10:34
# #File:  test.py
# # import yaml
# # with open("login_password", "r+", encoding="utf-8") as ya_user:
# #     ya_value = yaml.load(ya_user, Loader=yaml.FullLoader)
# # print(ya_value["admin"]["username"])
#
# # text = ActionChains(driver).move_to_element(P_xpath).perform()
# # text1 = ActionChains(driver).double_click(P_xpath).perform()
#
# # class PythonHelpApi ():
# #
# #     #定义一个读取excle表格的方法
# #     def ReadExcle(self,Sheet_Name,x,y):
# #         #插入读取权限
# #         import xlrd
# #         #excle表格的路径赋予变量ExclePath
# #         ExcelPath = "E:\\louxun\\python_script\\boss\Program\\数据导出.xlsx"
# #         #打开excle赋予变量OpenFile
# #         OpenFile=xlrd.open_workbook(ExcelPath)
# #         #传sheet页和行和列的值,并返回excle表的sheet页和行和列的值
# #         return OpenFile.sheet_by_name(Sheet_Name).cell_value(x,y)
# import pymysql
#
#
# class RagPageIndex():
#     def __init__(self):
#         self.Mysql_Connect = pymysql.connect(host="10.1.220.5", port=3306, user="root", password="12346",
#                                              database="rent_house")
#         self.Mysql_Cursor = self.Mysql_Connect.cursor()
#         self.userName = input("请输入用户名：")
#         self.pwd = input("请输入密码：")
#
#     def select_sql(self):
#         S_sql = "select * from reguserName"
#         self.Mysql_Cursor.execute(S_sql)
#         dataALl = self.Mysql_Cursor.fetchall()
#         a = []
#         for i in dataALl:
#             a.append(i[0])
#         print(a)
#         return a
#
#     def Mysql_Insert(self):
#
#         Insert_Sql = "insert into reguserName values('%s','%s')" % (self.userName, self.pwd)
#         self.Mysql_Cursor.execute(Insert_Sql)
#         self.Mysql_Connect.commit()
#
#     # 校验用户名
#     def checkUser(self):
#         if len(self.userName.replace(" ", "")) == 0:
#             return 1  # 用户名不能为空
#         elif " " in self.userName:
#             return 0  # 用户名不能包含非法字符
#
#         elif 6 > len(self.userName) or len(self.userName) > 18:
#             return 2  # 请输入6-18位的用户名
#         else:
#
#             if self.userName in self.select_sql():
#                 return 3  # 重复\
#
#     def checkPwd(self):
#         if len(self.pwd.replace(" ", "")) == 0:
#             return 4  # 密码不能为空
#         elif " " in self.pwd:
#             return 5  # 密码不能包空格
#         elif 6 > len(self.pwd) or 18 < len(self.pwd):
#             return 6  # 密码不符合范围区间
#
#     def regTest(self):
#         # 校验用户名合法性
#         code = self.checkUser()
#         if code == 1:
#             print("用户名不能为空")
#         elif code == 0:
#             print("用户名不能包含非法字符")
#         elif code == 2:
#             print("请输入6-18位的用户名")
#         elif code == 3:
#             print("用户名重复，请重新输入！")
#         else:
#             print("√")
#             if self.checkPwd() == 4:
#                 print("密码不能为空")
#             elif self.checkPwd() == 5:
#                 print("密码不能包空格")
#             elif self.checkPwd() == 6:
#                 print("密码不符合范围区间")
#             else:
#                 self.Mysql_Insert()
#                 print("注册成功！")
#
#
# RagPageIndex().regTest()
# #
import pymysql
house_name = '测试楼盘0005'

mysql_connect = pymysql.connect(host="10.1.220.5", port=3306, user="root", password="123456", database="rent_house")
msql_cursor = mysql_connect.cursor()
sql_del = 'DELETE from tb_base_house where `name` = "%s";'%house_name
msql_cursor.execute(sql_del)
mysql_connect.commit()



