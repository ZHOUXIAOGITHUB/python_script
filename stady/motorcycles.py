#-*- encoding=utf8 -*-
#Author:
#Time:  2020/6/28 9:24
#File:  motorcycles.py
#修改列表元素
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)

#在列表中添加元素,append在列表尾部添加
motorcycles_1 = ['honda', 'yamaha', 'suzuki']
print('1',motorcycles_1)
motorcycles_1.append('ducati')
motorcycles_2 = []
motorcycles_2.append('honda')
motorcycles_2.append('yamaha')
motorcycles_2.append('suzuki')
print('2',motorcycles_2)

#insert在列表任何位置添加元素
motorcycles_3 = ['honda', 'yamaha', 'suzuki']
motorcycles_3.insert(1, 'ducati')
print('3', motorcycles_3)

#del 删除列表指定位置的元素
motorcycles_4 = ['honda', 'yamaha', 'suzuki']
del motorcycles_4[0]
print('4', motorcycles_4)

#用法pop删除尾部元素
motorcycles_5 = ['honda', 'yamaha', 'suzuki']
popped_motorcycles = motorcycles_5.pop()
print('5', motorcycles_5)

#popped_motorcycles = 所删除的元素  - * - 应用场景 购买日期最后的删除，例如过保的手机
print('popped', popped_motorcycles)
motorcycles_6 = ['honda', 'yamaha', 'suzuki']
popped_woned = motorcycles_6.pop()
print('The last motorcycle I was woned a ' + popped_woned.title() + ".")

#pop(index)可以删除指定元素, 被删除的元素还可以使用，而del 元素无法被使用
motorcycles_7 = ['honda', 'yamaha', 'suzuki']
popped_7 = motorcycles_7.pop(0)
print('7', motorcycles_7)
print(popped_7)
print('The first motorcycle I woned was a ' + popped_7.title() + '.')

#删除元素的值用remove（），在知道列表中存在的值的情况下,删除第一个括号中的元素
motorcycles_8 = ['honda', 'yamaha', 'suzuki', 'honda']
motorcycles_8.remove('honda')
motorcycles_8.remove('honda')
print('8', motorcycles_8)

#可以将值储存在变量中，删除后方便后面引用
motorcycles_value = 'honda'
motorcycles_9 = ['honda', 'yamaha', 'suzuki', 'honda']
motorcycles_9.remove(motorcycles_value)
print('9', motorcycles_9)
# \n表示在前面空一行
print('\nA ' + motorcycles_value.title() + " is too expensive for me.")

#晚宴练习
dinner_list = ['小胖', '老魁', '毛豆', '毛玲']
print('I will invite ' + dinner_list[0] + ' join dinner today.')
print('I will invite ' + dinner_list[1] + ' join dinner today.')
first_num = dinner_list[1]
dinner_list[1] = '吕梦'
print(first_num + ' will work overtime tonight, so I will invite ' + dinner_list[1] + ".")
print('I will invite ' + dinner_list[1] + ' join dinner today.')
for i in dinner_list:
    print('I will invite ' + i + ' join dinner today.')
dinner_list.insert(0, 'zhouzhou')
dinner_list.insert(2, "老魁")
dinner_list.append("小老魁")
print(dinner_list)
for j in dinner_list:
    print('I will invite ' + j + ' join dinner today.')
dinner_list.pop(0)
dinner_list.pop(0)
dinner_list.pop(0)
dinner_list.pop(0)
dinner_list.pop(0)
print(dinner_list)
print(dinner_list[0] + ' on the dinner_list.')
print(dinner_list[1] + ' on the dinner_list.')
# del dinner_list           del后面不加索引删除的是整个表结构
# # print(dinner_list)
del dinner_list[0]
del dinner_list[0]
print(dinner_list)

#reverse()颠倒列表排序，可永久更改列表顺序，再次使用reverse可更改为原来的顺序
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)

#确定列表长度len(),判断列表元素个数
cars_1 = ['bmw', 'audi', 'toyota', 'subaru']
tt = len(cars_1)
print(tt)

#sorted()实现列表中的元素按照字母顺序排序,暂时改变并不改变源列表数据,需要讲新改变的赋值给原来的列表
city = ['haerbin', 'qinghai', 'lijiang', 'yunnan', 'beijing']
print(city)
city = sorted(city)
print(city)
city.reverse()
print(city)

#使用sort()，直接对原列表进行排序
city_1 = ['haerbin', 'qinghai', 'lijiang', 'yunnan', 'beijing']
print('1', city_1)
city_1.sort()
print('1', city_1)

#上述函数小练习
fruits = ['apple', 'watermelon', 'tangerine', 'banana', 'pear', 'orange']
print(fruits)
fruits[2] = 'peach'
print(fruits)
fruits.append('tangerine')
print(fruits, '3')
fruits.insert(4, 'grape')
print(fruits, '4')
del fruits[2]
print(fruits, '5')
fruits.pop()
print(fruits, '6')
fruits.pop(-2)
print(fruits, '7')
fruits.remove('apple')
print(fruits, '8')



















