#-*- encoding=utf8 -*-
#Author:
#Time:  2020/7/3 14:41
#File:  car.py
# 汇总汽车的类
class Car():

    def __init__(self, make, model, year):
        """初始描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回整洁的描述信息"""
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title() # 返回long_name

    # 给属性指定默认值
    def red_odomter(self):
        """打印一条支出骑车里程的消息"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    # 通过方法修改属性的值,调用此函数的后传的参数储存在全局变量参数中
    def update_odometer(self, mileage):
        """此处加一判断所传入的参数不能比原来变量小"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer")

    # 讲里程表读数增加指定量
    def increment_odometer(self, miles):
        self.odometer_reading += miles
my_new_car = Car("ai", "a4", "2016")
# my_new_car.odometer_reading = 23
# 直接修改属性值,原init中的odometer_reading = 0被odometer_reading = 23给覆盖
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(23)
my_new_car.red_odomter()








