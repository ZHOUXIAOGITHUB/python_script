#-*- encoding=utf8 -*-
#Author:
#Time:  2020/6/9 15:30
#File:  mulyiplication_table.py


# for x in range(1,10):
#    for y in range(1,x+1):
#       print("{}*{}={}".format(x,y,y*x), end="    ")
#
#    print()

# i = 0
# for i in range(0,9):
#     i += 1
#     for j in range(i,10):
#         print("%d*%d=%2d" % (i, j, i * j), end=" ")
#     print("")

# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print("%dx%d=%d\t" % (i, j, i * j), end="")
#     print("")
# from lib.Publice_Lib import Publice_Lib
# # t = Publice_Lib().Mulyiplication_Table_For()
# t = Publice_Lib().Mulyiplication_Table_While()




# i = 1
# while i<= 9:
#     j = 1
#     while j <= i:
#         sum = j*i
#         print("%dx%d=%2d"%(j,i,sum),end=("\t"))
#         j += 1
#     print()
#     i += 1

# def shout(word="UU"):
#     return word.capitalize() +"..."
# print (shout())
#
# t = shout()
# print(t)
# del shout
# # print(shout)
# print(t)


def talk():
    # 你可以在"talk"里定义另一个函数 ...
    def whisper(word="yes"):
        return word.lower() + "..."

    # 让我们用用它!

    print  (whisper())

talk()


