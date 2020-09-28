#-*- encoding=utf8 -*-
#Author:
#Time:  2020/6/24 14:52
#File:  brithday.py
#int 类型的不可以和字符串拼接，需要转化数据类型
age = 23 #age = "23" 也是可以的
age = str(age)
message = "Happy " + age +"rd Brithday! "
print(message)
print(2 * 4)
print(4 + 4)
print(4 / 0.5)
print(10 - 2)
number = 9
message_1 = "My favourite numeber is " + str(number) +", Because " + str(number) +"th sounds like nice. "
print(message_1)

