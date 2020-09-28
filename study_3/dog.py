#-*- encoding=utf8 -*-
#Author:
#Time:  2020/7/3 11:39
#File:  dog.py
# 创建类
# 首字母大写的被定义成类，函数和方法的是以小写命名的
class Dog():
    # 类中的函数称之为方法，所有的函数都适用方法
    # __init__是特殊的方法，每次调用类的时候都会运行方法，前后的__是和普通的方法区别，避免命名冲突单独的init就是普通的方法
    # init方法中self形参是必须存在的（Python调用这个__init__()方法来创建Dog实例时，将自动传入实参self。每个与类相关联的方法
    # 调用都自动传递实参self，它是一个指向实例本身的引用，让实例能够访问类中的属性和方法）
    def __init__(self, name, age):
        """初始化属性那么和age"""
        self.name = name # 带有self的变量可以供类下所有的方法调用（全局变量）
        self.age = age

    def sit(self):
        """模拟狗狗下命令蹲下"""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """模拟狗狗被下命的时候打滚"""
        print(self.age.title() + " rolling over!")

my_dog = Dog('willie', "6") # 讲Dog类实例化
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()
my_dog.roll_over()

