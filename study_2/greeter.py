#-*- encoding=utf8 -*-
#Author:
#Time:  2020/7/2 14:30
#File:  greeter.py
#定义函数
def greet_user(): #定义的函数一定要有括号
    """显示简单问候语"""
    print("hello!")    #函数体，电泳函数所需要执行的代码
greet_user()   #调用函数只需指定函数名称和括号中必要的信息
#向函数传递信息
def greet_users_1(username):
    print("Hello, " + username.title() + "!")
greet_users_1("jrie")   #此处调用必须要给括号的参数赋值
def greet_users_2(username_1):
    print("haha")
greet_users_2("xx")#此处函数的参数没有调用也是需要传递信息给函数

#实参和形参pets.py
def descirbe_prt(anmile_type, pet_name):
    """显示宠物信息"""
    print("\nI have a " + anmile_type.title() + ".")
    print("My " + anmile_type + "'s name is " + pet_name.title() + ".")
#调用函数
descirbe_prt("shadiao", "erha")#在函数调用中实参"shadiao", "erha"存储在形参anmile_type, pet_name中
#在函数体中通过形参anmile_type, pet_name来展示宠物信息

# 可以根据函数需要多次调用函数 ，确保函数参数顺序传递的时候不能出错
descirbe_prt("英短", "猫猫")
descirbe_prt("英", "沟谷偶")
#可以使用关键字参数就不用注意顺序了
descirbe_prt(pet_name="erhan", anmile_type="shagou")
#默认值
def descirbe_prt_1(pet_name, anmile_type="dog" ):
    print("\nI have a " + anmile_type.title() + ".")
    print("My " + anmile_type + "'s name is " + pet_name.title() + ".")
descirbe_prt_1("shadiao")
#填写默认值时有默认值的要放在后面,调用函数的时候，有默认值的就不用传参数了
#等效函数
descirbe_prt_1(pet_name="erhan", anmile_type="shagou") #当有形参的时候你再次指定传入函数，则以实际传入的函数为准
descirbe_prt_1(pet_name="拉布拉多")
descirbe_prt_1("英", "沟谷偶") #此时不使用关键字传参，一样可以传递进去

