#-*- encoding=utf8 -*-
#Author:
#Time:  2020/7/2 14:16
#File:  confirmed_users.py
#使用whill处理列表和字典
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    confirmed_users.append(current_user)
    print(confirmed_users)
#循环while以内的部分
#删除含有特殊元素值的列表
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
while "cat" in pets:
    pets.remove("cat")
print(pets)