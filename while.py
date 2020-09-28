#-*- encoding=utf8 -*-
#Author:
#Time:  2020/6/9 9:49
#File:  while.py
#冒泡排序
# import random
# #定义列表
# list = [11,34,67,4,65,76,5,7]
#
# # for i in range(len(list)-1):
# #     print("---"*10)
# #     print(i+1)
# #     print("---"*10)
# for j in range(len(list)-1):
#     if list [j]>list [j+1]:
#         list[j],list[j+1] = list[j+1], list[j]
#     print(list)
#


# lst = [33, 2, 12, 34, 22, 56, 32, 45, 43]  # 假如有如乱序列表
#
# for i in range(len(lst) - 1):  # 有多少个数比较多少轮
#     print("============================")
#     print("第", (i + 1), "轮：")
#     print("============================")
#     for j in range(len(lst) - i - 1):  # 已经冒泡的不再比较，即最后一轮只比较一次
#         if lst[j] > lst[j + 1]:  # 每次紧挨着的两个比较
#             lst[j], lst[j + 1] = lst[j + 1], lst[j]  # 交换位置
#         print("第", (j + 1), "次：", lst)
#
# # print("最后结果：", lst)
# from lib.Publice_Lib import Publice_Lib
# #调用冒泡排序的方法
#
# list1 = [90, 34, 54, 5, 67]
# t = Publice_Lib().bubble_sort(list1)
list = ["nice", "ugly", "beautiful"]
list.append("cool")
print(list)
list.insert(2,'cool')
print(list)
del list[1]
print(list)
list.remove("cool")
print(list)
list.remove("cool")
print(list)
list = str(list)
print(list[0], type(list))

tea = "jj"
print(type(tea))
if list is str or tea is str :
    print("that good!!!")
else:
    print("it's trrible!!!")