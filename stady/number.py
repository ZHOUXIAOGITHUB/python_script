#-*- encoding=utf8 -*-
#Author:
#Time:  2020/6/28 16:37
#File:  number.py
#range生成数字
for value in range(1,5):
    print(value)
numbers = list(range(1,6))
print(numbers)
even_number = list(range(2, 10, 2))
print(even_number)
squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
    print(squares)





