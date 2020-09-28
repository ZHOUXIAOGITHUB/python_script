#-*- encoding=utf8 -*-
#Author:
#Time:  2020/7/3 10:14
#File:  pizza.py
#传任意数量的参数
# def make_pizza(*toppings):
#     """打印顾客点的所有配料"""
#     print(toppings)
# make_pizza('pepperoni')
# make_pizza('mushrooms', 'green peppers', 'extra cheese')

# 位置实参和任意数量参数
def make_pizza(size, *toppings):  # 第一个形参取第一个实参，后面的所有参数传任意参数
    print("\nMaking a " + str(size) + "-inch pizza with the following topping: ")
    for topping in toppings:
        print("- " + topping)
# make_pizza_1(16, 'pepperoni')
# make_pizza_1(12, 'mushrooms', 'green peppers', 'extra cheese')