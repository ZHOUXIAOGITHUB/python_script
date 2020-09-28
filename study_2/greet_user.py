#-*- encoding=utf8 -*-
#Author:
#Time:  2020/7/2 15:39
#File:  greet_user.py
#可以吧参数定义成列表传递进去
def greet_user(names):
    for name in names:
        msg = "Hello, " + name.title() + '!'
        print(msg)
user_name = ['hannah', 'ty', 'margo'] #传递列表
greet_user(user_name)
username = {"huahua": "jj"}#字典默认循环键
greet_user(username)