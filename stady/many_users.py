#-*- encoding=utf8 -*-
#Author:
#Time:  2020/6/29 17:08
#File:  many_users.py
#字典中嵌套字典，应用场景姓名居住地
users = {
    'aeinstein': {
        'first': 'albert',
        'last': "einstein",
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        "location": 'paris',
    },
}
for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + ' ' + user_info['last']
    location = user_info['location']
    print("\tFull_name: " + full_name)
    print("\tLocation: " + location)
#注意：字典嵌套字典的结构尽量保持一直，否则for循环运行起来比较复杂
