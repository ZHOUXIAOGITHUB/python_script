#-*- encoding=utf8 -*-
#Author:
#Time:  2020/7/2 15:22
#File:  formatted_name.py
#返回指（返回简单的值）
def get_formatted_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name = first_name + " " + last_name  #讲函数复杂的组成写入函数体中从而简化代码
    return full_name
musician = get_formatted_name("jimi", 'hedrix')
print(musician)
#让参数可供选择
def get_formatted_name_1(first_name, last_name, middle_name=" "): #可以给默认参数一个空值，需要的时候传参，不需要的时候就不传
    full_name = first_name + middle_name + last_name
    return full_name
musician = get_formatted_name_1("jimi", 'hedrix')
print(musician)

#返回字典
#函数结合while循环使用
