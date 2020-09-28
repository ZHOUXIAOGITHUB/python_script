#-*- encoding=utf8 -*-
#Author:
#Time:  2020/6/29 16:42
#File:  pizza.py
#字典中储存列表
pizza = {
    'crust': 'thick',
    'toppings': ['mushroom', 'extra cheese']
}
#概述所点的pizza
print("You ordered a " + pizza['crust'] + "-curs pizza " +
      "with the following toppings:")
#遍历topping值（列表）
for topping in pizza["toppings"]:
    print("\t" + topping)
#favourite_language.py
print('333' * 99)
favourite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell']
}
for name, languages in favourite_languages.items():
    print("\n" + name.title() + "'s favourite_language are:")
    for language in languages: #获取的指是一个列表，再次遍历每个列表
        print("\t" + language.title())
