#-*- encoding=utf8 -*-
#Author:
#Time:  2020/6/30 10:46
#File:  cities.py
#使用break退出循环
prompt = "\nPlease enter the name of city you have visited: "
prompt += "\n(enter 'quit' when you are finished.)"
#以while true不断循环知道遇到break终止
while True:
    city = input(prompt)
    if city == "quit":
        break
    else:
        print("I'd love to go to " + city.title() + "!")
#任何情况下都可以使用break结束for循环或者字典循环

