#   -*- coding:utf-8 -*-
#   @Time   :   2020/  /
#   @Author :   goldsunC
#   @Email  :   2428022854@qq.com
#   @Blog   :   https://blog.csdn.net/weixin_45634606

from  ..components import info
import pygame

class LoadScreen:
    def __init__(self):
        self.finished = False
        self.next = 'level'
        self.timer = 0
        self.info = info.Info('load_screen')

    def update(self,surface,keys):
        self.draw(surface)
        if self.timer == 0:
            self.timer = pygame.time.get_ticks()
        elif pygame.time.get_ticks() - self.timer > 2000:
            self.finished = True
            self.timer = 0

    def draw(self,surface):
        surface.fill((0,0,0))
        self.info.draw(surface)