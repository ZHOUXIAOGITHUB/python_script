#-*- encoding=utf8 -*-
#Author:
#Time:  2020/7/3 15:50
#File:  my_car.py
# 导入类
from study_3.car import Car
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23
my_new_car.red_odomter()
# 导入整个模块也是需要一个类一个类的调用
