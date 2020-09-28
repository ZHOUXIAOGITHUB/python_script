#-*- encoding=utf8 -*-
#Author:
#Time:  2020/6/30 9:08
#File:  parrot.py
#函数input的工作原理
"""
message = input("Tell me something, and I will repeat it back to you:")
print(message)
name = input("Please enter your name: ")
print("Hello , " + name + "!")
#提示超过一行的时候可以将提示存在变量中进行调用
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name?" #此处 prompt +=....     ==    prompt = prompt + .....   注意+=之间没有空格
name = input(prompt)
print("\nHello, " + name + "!")
"""
#求模运算符（%），直接返回余数
mun = 5 % 3
print(mun) #返回的是2