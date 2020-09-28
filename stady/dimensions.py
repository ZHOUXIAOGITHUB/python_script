#-*- encoding=utf8 -*-
#Author:
#Time:  2020/6/29 11:21
#File:  dimensions.py
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
# dimensions[0] = 250   TypeError: 'tuple' object does not support item assignment,元组不能被修改
# print(dimensions)
for dimension in dimensions:
    print(dimension)
#不可以改变元组，我们可以重新给元组赋值
dimensions = (400, 100)
print(dimensions)
#缩进四个空格等于一个缩进

#控制行长，通常代码行长控制在79个，注释行长控制在72个
