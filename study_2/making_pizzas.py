#-*- encoding=utf8 -*-
#Author:
#Time:  2020/7/3 11:19
#File:  making_pizzas.py
# 导入模块
from study_2 import pizza
#此处不可以直接导入，需要加一个路径
pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
# 可以在导入的时候用as 命名为别名
from study_2 import greet_user as cc
cc.greet_user("shabi")

# 导入模块中所有的函数 *
from study_2 import *
# 形参等号两遍边不可以有空格
# 关键字参数等号两边不可以有空格

