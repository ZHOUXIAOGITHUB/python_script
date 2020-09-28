#-*- encoding=utf8 -*-
#Author:
#Time:  2020/6/29 16:03
#File:  aliens.py
#嵌套字典列表
alien_0 = {'color': 'green', 'point': 5}
alien_1 = {'color': 'yellow', 'point': 10}
alien_2 = {'color': 'red', 'point': 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)
#创建一个空列表
aliens = []
for alien_number in range(1, 30):
    new_alien = {'color': 'green', 'point': 5, 'speed': 'slow'}
    aliens.append(new_alien)#总共遍历29次，每次遍历的后就把字典new_anlien加入到aliens中
    # aliens.clear()如果添加一个清除动作则每次都是1
#显示前五个外星人
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['point'] = 10
for alien in aliens[0:5]:
    print(alien)
print("...")
#显示创建多少个外星人
print("Total number of aliens: " + str(len(aliens)))



