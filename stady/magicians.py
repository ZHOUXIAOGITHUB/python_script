#-*- encoding=utf8 -*-
#Author:
#Time:  2020/6/28 16:08
#File:  magicians.py
#循环遍历
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)
magicians_1 = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ', That was a great trick!')
    print('I can\'t wait see your next trick! ' + magician.title() + '.\n')
print('Thank you, everyone. That was a great magic show!')