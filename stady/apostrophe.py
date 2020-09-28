#-*- encoding=utf8 -*-
#Author:
#Time:  2020/6/24 14:27
#File:  apostrophe.py
#单引号和撇号的使用语法错误，单引号和撇号之间被认为是字符串，后面的视为代码，意思不可以三个单引号同时使用
message = "One of the Python's strengths is its drives commuity. "
print(message)
#python无法翻译三个单引号的字符串,可以通过添加转义符来完成表达，转义符有r或者\,三个单引号时r就不适用了
message = 'One of the Python\'s strengths is its drivers commuity. '
print(message)
message = r'One of the Python\'s strengths is its drivers commuty. '
print(message)
#python多数小数位置显示异常
# >>> 0.2 + 0.1
# 0.30000000000000004
# >>> 3 * 0.1
# 0.30000000000000004
# >>> 3 * 0.2
# 0.6000000000000001
# >>> 3 *0.3
# 0.8999999999999999
#其他的可以正常运算，无需担心

