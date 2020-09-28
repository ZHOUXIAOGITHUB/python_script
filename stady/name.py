#-*- encoding=utf8 -*-
#Author:
#Time:  2020/6/24 11:10
#File:  name.py
name = "ada lovelace"
print(name.title())
#title是一个方法,将首字母大写，方法执行的时候需要带(),括号内可以提供额外的信息完成工作， 例如继承，   .会让执行.后面的操作
#全部改为大写，upper()
print(name.upper())
#改为小写
print(name.lower())
#lower()适用于数据储存，先将所有的数据储存为小写，然后根据大小写要求转换
first_name = "ada"
last_name = "lovelase"
full_name = first_name + " " + last_name
print(full_name)
print("Hello, " + full_name + "!")
print("Hello, " + full_name.title() + "!")
message = "Hello, " + full_name.title() + "!"
print(message)
#非打印字符，空格，制表符\t，换行\n
print("python")
print('\tpython')
# 字符串前面添加换行\n,\n表示在前面添加换行所需要的空格
print("Language: \nPython \nC \nJavaScript")
#\n,\t可以在也同一个字符串中使用,在同一个字符串中使需要先加\n，要不然制表符会被换行给覆盖掉
print("language: \n\tPython \n\tC \n\tJavasript")
print("language: \t\nPython \t\nC \t\nJavasript")
#删除空白，应用输入用户名时不支持空格，rstrip（）
favourite_language = "Python "
print(favourite_language)
favourite_language.rstrip()
# print(favourite_language)
#只支持暂时删除
#永久删除空白，必须将删除的空白保存到变量中
favourite_language = favourite_language.rstrip()
print(favourite_language)
favorite_language = " Python "
#去除开头空格用lstrip
print(favorite_language.lstrip())
#去除尾部空格
print(favorite_language.rstrip())
#去除首尾空格
print(favorite_language.strip())
#只有开头空格的时候只能使用lstrip
favourite_language_1 = " Python_1"
favourite_language_2 = "Python_2    "
print(favourite_language_1.rstrip())
#当只有尾部空格的时候可以使用rstrip和strip
print(favourite_language_2.strip())
li = []
li.pop()


















