#-*- encoding=utf8 -*-
#Author:
#Time:  2020/6/29 15:04
#File:  user.py
#遍历字典
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi'
}
for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)
#遍历字典时不按照储存关系，只按照键值对的关系
#favourite_language.py
favourite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}
for name, language in favourite_language.items():
    print(name.title() + "'s favourite language is "
          + language.title() + ".")
#遍历字典中所有的建
for name in favourite_language.keys():
    print(name.title())
#遍历字典默认遍历字典的建
for name in favourite_language:
    print(name.title())
#置顶键打印出值
favourite_language_1 = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}
friends = ['phil', 'jen']
for name in favourite_language_1.keys():
    print(name.title())
    if name in friends:
        print(" Hi " + name.title() +
              ", I see your favourite language is " +
              favourite_language_1[name].title() + "!")

if 'erin' not in favourite_language_1.keys():
    print("Erin, please talk our poll!")
#使用sorted()获取指定顺序键,按照字母排序进行输出
print("#" * 55)
favourite_language_2 = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}
for name in sorted(favourite_language_2.keys()):
    print(name.title() + ", Thank you for taking the poll.")
#遍历字典中所有的值将后缀的keys（）换成values（）
print("#" * 55)
favourite_language_2 = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}
for language in favourite_language_2.values():
    print(language.title())

