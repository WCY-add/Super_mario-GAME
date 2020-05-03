#   -*- coding:utf-8 -*-
#   @Time   :   2020/  /
#   @Author :   goldsunC
#   @Email  :   2428022854@qq.com
#   @Blog   :   https://blog.csdn.net/weixin_45634606
from  ..components import info
import pygame
from  .. import tools,setup
from  .. import constants as C
from  .. components import player
class Level:
    def __init__(self):
        self.finished = False
        self.next = None
        self.info = info.Info('level')
        self.setup_background()
        self.setup_player()
    def setup_background(self):
        self.background = setup.GRAPHICS['level_1']
        rect = self.background.get_rect()
        self.background = pygame.transform.scale(self.background,(int(rect.width * C.BG_MULTI),
                                                                  int(rect.height * C.BG_MULTI)))
        self.background_rect = self.background.get_rect()

    def setup_player(self):
        self.player = player.Player('mario')
        self.player.rect.x = 300
        self.player.rect.y = 300

    def update(self,surface,keys):
        self.player.update(keys)
        self.update_player_position()
        self.draw(surface)

    def update_player_position(self):
        self.player.rect.x += self.player.x_vel
        self.player.rect.y += self.player.y_vel

    def draw(self,surface):
        surface.blit(self.background,(0,0))
        surface.blit(self.player.image,self.player.rect)
        self.info.draw(surface)