#-*- encoding=utf8 -*-
#Author:
#Time:  2020/6/24 16:04
#File:  bicycles.py
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
# 索引从0开始
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[1])
print(bicycles[3])
# 索引可以从-1开始从最后往前数
print(bicycles[-1])
message = "My first bicycles was a " + bicycles[0].title() + "."
print(message)
names = ['蓓蓓', '周国豪', 'e兰顺', '潘建萍']
print(names[0])
print(names[-1])
print(names[1])
#此处title改首字母为大写，若只有中文不报错页不受影响
print(names[-2].title())
message_1 = names[1]+ "、" + names[0]+"、" + names[2] + ", We are test !"
print(message_1)
vehicle = ["tran", "bus", "bicycle", "plane", "car"]
message_2 = "I don't like " + vehicle[1] + ", Because I get carsick."
print(message_2)
