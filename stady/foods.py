#-*- encoding=utf8 -*-
#Author:
#Time:  2020/6/29 10:52
#File:  foods.py
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print('My favourite foods are:')
print(my_foods)
print('\nMy friend\'s foods are:')
print(friend_foods)
my_foods.append('cannoli')
friend_foods.append('ice cream')
print('My favourite foods are:')
print(my_foods)
print('\nMy friend\'s foods are:')
print(friend_foods)
#不用切片赋值则被赋值的对象已经完全代替现在，此时两个对象绑定一起，都是时时更新的，而且前赋值则独立两个列表
my_foods_1 = ['pizza', 'falafel', 'carrot cake']
friend_foods_1 = my_foods_1
my_foods_1.append('cannoli')
print(my_foods_1, '#'*3)
my_foods_1.append('ice cream')
print('My favourite foods are:')
print(my_foods_1, "*"*10)
print('\nMy friend\'s foods are:')
print(friend_foods_1)
print('The first three item in the list are:', my_foods_1[0:3])
print('The first three item in the list are:', my_foods_1[1:4])
print('The first three item in the list are:', my_foods_1[-4:-1])
my_pizza = ['boluopizza', 'applepizza', 'bananapizza']
friend_pizza = my_pizza[:]
friend_pizza.append("shipizza")
for pizza in my_pizza:
    print('My favourite pizza is ' + pizza)
for pizzas in friend_pizza:
    print("My friend's favourite is " + pizzas)

