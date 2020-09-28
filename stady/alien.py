#-*- encoding=utf8 -*-
#Author:
#Time:  2020/6/29 14:49
#File:  alien.py
alien_0 = {'color': 'green', 'point': 5}
#访问字典中的值
print(alien_0['color'])
new_points = alien_0['point']
print('You just earned ' + str(new_points) + " points!")
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
alien_1 = {}
alien_1['color'] = 'green'
alien_1['point'] = 25
print(alien_1)
print("The alien is " + alien_1['color'] + ".")
alien_1['color'] = 'yellow'
print('The alien is now ' + alien_1['color'] + '.')
#删除键值对
del alien_1['point']
print(alien_1)

