#-*- encoding=utf8 -*-
#Author:
#Time:  2020/8/7 16:07
#File:  ship.py
import pygame
class Ship():
    def __init__(self, screen):
        """初始化飞船的位置"""
        self.screen = screen
        # 加载飞船图想，获取外界矩形
        # self.image = pygame.image.load('images/ship.bmp')
        # self.rect = self.image.get_rect()
        # self.screen_rect = screen.get_rect
        self.image = pygame.image.load('E:\louxun\python_script\create\ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # 将每艘新飞船放到底部
        self.rect.centerx = self.screen_rect.centerx  #centerx ---中央
        self.rect.bottom = self.screen_rect.bottom    #bottom ---底部
    def blitme(self):
        """指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)   # blit  传送块




