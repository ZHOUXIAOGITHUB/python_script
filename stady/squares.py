#-*- encoding=utf8 -*-
#Author:
#Time:  2020/6/29 10:24
#File:  squares.py
squares = [value **2 for value in range(1, 11)]
print(squares, min(squares),
        sum(squares),
        max(squares))
number = [value for value in range(1, 21)]
print(number)
number_1 = [value for value in range(1, 10000000)]
# for num in number_1:
#     print(num)
print(sum(number_1))
number_list = [value for value in range(1, 20, 2)]
for num in number_list:
    print(num)
number_list_1 = [value for value in range(3, 30, 3)]
for num_1 in number_list_1:
    print('\n1',num_1)
number_list_2 = [value ** 3 for value in range(1, 10)]
list_1 = []
for i in number_list_2:
    print(i)
    list_1.append(i)
print(list_1)

