#-*- encoding=utf8 -*-
#Author:
#Time:  2020/6/29 11:41
#File:  cars.py
#if 语句
cars = ['bmw', 'audi', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
        #字母的大小写也回影响判断
        print(car.title() == 'bmw')
    else:
        print(car.title())
        print(car == 'bmw')




