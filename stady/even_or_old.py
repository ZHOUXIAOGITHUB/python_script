#-*- encoding=utf8 -*-
#Author:
#Time:  2020/6/30 9:34
#File:  even_or_old.py
#求模运算符（%），直接返回余数
mun = 5 % 3
print(mun) #返回的是2
#可以用求模运算符来判断一个数是奇数还是偶数 通过判断返回数字是否为0
number = input("Enter a number, and I tell you if it's even or old:")
number = int(number)
if number % 2 == 0:
    print("\nThe number " + str(number) + " is even.")#此处number是int类型，要想拼接必须转为str类型
else:
    print("\nThe number " + str(number) + " is old.")
message = "Please tell me do you like what's antomobile: "
print(input(message))
message_1 = input("Please tell me how many of your people:")
message_1 = int(message_1)
if message_1 > 8:
    print('If your beyond ' + str(message_1) + ", There is no empty table.")
else:
    print("There are empty table!")
number = input("Please enter a number, and I tell you if it's multiple of 10: ")
number_1 = int(number)
if number_1 % 10 == 0:
    print("\nThe number " + str(number_1) + " is multiple of 10.")
else:
    print("\nThe number " + str(number_1) + " is  not multiple of 10.")

