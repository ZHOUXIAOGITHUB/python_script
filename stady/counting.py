#-*- encoding=utf8 -*-
#Author:
#Time:  2020/7/1 17:26
#File:  counting.py
#counting 跳过某个条件的循环，不是结束整个循环
current_number = 0
while current_number < 10:
    current_number += 1 #等价于current_number = current_number+1
    if current_number % 2 == 0:
        continue
    print(current_number)
#当条件符合if的条件跳过if后面的代码，重新进入循环
#while 必须有终止路径才不至于无限循环
x = 1
while x <= 5:
    print(x)
    x += 1 #此处是关闭无限循环的关键




