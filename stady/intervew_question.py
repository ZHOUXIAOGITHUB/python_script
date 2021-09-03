#-*- encoding=utf8 -*-
#Author:
#Time:  2021/5/19 10:24
#File:  intervew_question.py

""""
- python
  - 怎么给dict字典新增一个元素
  - tuple元组是否可以修改
  - 有没有用过python装饰器
  - 如果有一个list，怎么去做去重
  - 除了set还有其他方法吗
  - 除了遍历数组以外还有其他方法吗
  - 这两个方法去重之后，顺序还是一样吗
  - 目前有一个list，给一个长度n，怎么去做分割
  - 是否需要加判断（判断n的长度是否大于目前list长度）
  - 有没有用过pytest
  - ui自动化怎么做的
    - 关键字封装+数据驱动
    - iframe怎么操作
  - 如果导入一个包的时候出错会是什么原因
    - 文件层级问题、环境变量问题
    - 怎么解决？ 使用os库，把对应要导入的文件目录放到path里
  - 如果一个类要调用其他一个函数里面的变量怎么操作
- 数据库
  - 口述sql怎么写
- 测试
  - 自动化跟功能测试的比例
  - 测试流程是怎样的
  - 怎么判断bug是前端还是后端的
- devops
  - 有没有用过docker跟k8s
    - docker怎么查看日志
  - liunx 常用操作有哪些
    - 如果liunx服务器的一堆配置文件中，找到对应某个配置怎么操作
    - 如果要批量修改配置怎么写
    - liunx 怎么挂载硬盘
    - liunx 怎么看系统盘跟数据盘
    - 怎么查看日志
    - 服务器如果硬盘满了，怎么分析问题原因
    - 怎么查看服务器资源
    - top是动态查看资源情况的，那怎么固定查看
"""
# - 怎么给dict字典新增一个元素
"""
dict = {"name": "唐三", "age": "22", "property": "昊天锤"}
dict["property1"] = "蓝银草"
"""
# print(dict)
# - tuple元组是否可以修改
# ---元组不可被修改
# - 有没有用过python装饰器
# 代码块1
"""
import time
from timeit import timeit
@timeit
def func_0():
    time.sleep(2)
# 代码块2
def func_1():
    time.sleep(2)
func_0 = timeit(func_0)
"""
# - 如果有一个list，怎么去做去重
# 1.遍历不会改变顺序
"""
list = [2, 3, 3, 0, 6, 9, 9]
list1 = []
for i in list:
    if i not in list1:
        list1.append(i)
list = list1
print(list)
"""

# 2.使用set, 调用list函数，会改变排序
"""
list1 = [2, 3, 3, 0, 6, 9, 9]
list1 = list(set(list1))
print(list1)
"""
# 使用itertools.grouby ,先排序后去重
"""
import itertools
list2 = [1, 4, 3, 3, 4, 2, 3, 4, 5, 6, 1]
list_null = []
list2.sort()
# print(list2)
num_list = itertools.groupby(list2)
for k, g in num_list:
    list_null.append(k)
list2 = list_null
print(list2)
"""
# - 目前有一个list，给一个长度n，怎么去做分割,
# 不用判断n的长度，超出列表长度后面分割的为空列表
"""
list2 = [1, 4, 3, 3, 4, 2, 3, 4, 5, 6, 1]
print(list2[90:])
"""
# - 有没有用过pytest  ----pytest代替selenium做接口自动化
# - ui自动化怎么做的
#     - 关键字封装+数据驱动
#     - iframe怎么操作   ----先通过元素定位到该位置，然后再使用switch_iframe 去切换
# - 如果导入一个包的时候出错会是什么原因-----环境没有安装该依赖包
# - 数据库
#   - 口述sql怎么写-----简单查询 select * from 表 where 条件

