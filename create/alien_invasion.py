#-*- encoding=utf8 -*-
#Author:
#Time:  2020/7/9 11:08
#File:  alien_invasion.py
import sys

import pygame
from create.settings import Settings
from create.ship import Ship


def run_game():
    """初始游戏，创建游戏对象"""
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_with, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # 创建一艘飞船
    ship = Ship(screen)
    # 设置背景颜色
    # bg_color = (230, 230, 230)
    #开始游戏的主循环
    while True:
        #监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
    # 让绘制的屏幕可见
        screen.fill(ai_settings.bg_color)  # 调用背景墙把颜色填满
        ship.blitme()  # blitme 愉快的
        pygame.display.flip()

run_game()
