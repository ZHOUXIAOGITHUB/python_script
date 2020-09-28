#-*- encoding=utf8 -*-
#Author:
#Time:  2020/7/3 15:08
#File:  electric_car.py
# 继承
"""
2.7中继承父类的方法
class Car(object):
 def __init__(self, make, model, year):
 --snip--
class ElectricCar(Car):
 def __init__(self, make, model, year):
 super(ElectricCar, self).__init__(make, model, year)
 """
# init需要优先完成父类的所有属性值
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

#讲实例用作属性
class Battery():
    """一次模拟的简单实验"""
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

class ElectricCar(Car):
    """电动车的独到之处"""
    def __init__(self, make, model, year):
        """初始化父类的属性"""
        super().__init__(make, model, year)
        self.battery_size = 70
        self.battery = Battery() # 把class Battery 类实例化存在变量battery中

    # 重写父类(父类中有同名的方法，且不能满足现在所需要的功能，然后重新写入，调用也是调用重写的)
    def fill_gas_tank(self):
            print("ddd")

    # 给子类定义属性和方法
    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
# 此类调用中battery可有可无，因为在实例ElectricCar自动运行下面代码，调用的batter存储的是实例类Battery




