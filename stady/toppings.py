#-*- encoding=utf8 -*-
#Author:
#Time:  2020/6/29 12:45
#File:  toppings.py
#检查是否相等
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print('Hold the anchovies')
age = 18
#File:  magic_number.py
answer = 17
if answer != 42:
    print('That is not correct answer, Please try again!')
#检查特定值是否包含在内 用in
requested_toppings = ['mushrooms', 'onions', 'pineapple']
tt = 'mushrooms' in requested_toppings
print(tt)
print('persionion' in requested_toppings)
#检查特定指是否在列表中banned_user.py
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(user.title() + ', you can post a response if you wish.')
#布尔表达式通常记录条件
game_active = True
can_edit = False

car = 'byd'
print('Is car == "byd", I predict True.')
print(car == 'byd')
print("\nIs car =='bm', I predict False.")
print(car == 'bm')

#condition_tests.py
#检查俩个字符串是否相等
print("#" * 99)
bus = 'Public'
plane = 'Nice'
print(car == plane)
print(car != plane)
#lower 判断
print(bus.lower() == "public")
print(plane.lower() == "Nice")
print(3 < 5)
print(3 <= 5)
print(3 > 5)
print(3 != 5)
print(3 >= 5)
print(4 < 5 and 3 < 5)
print(3 < 5 or 4 > 5)
list_1 = [1, 8, 0, 7]
print(1 in list_1, "99")
print(3 in list_1, "98")
print(3 not in list_1, "97")
print(1 not in list_1, "96")

