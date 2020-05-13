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
import os
import json
class Level:
    def __init__(self):
        self.finished = False
        self.next = None
        self.info = info.Info('level')
        self.load_map_data()
        self.setup_background()
        self.setup_start_position()
        self.setup_player()

    def load_map_data(self):
        file_name = 'level_1.json'
        file_path = os.path.join('D:\\练习专用\\py超级玛丽\\Material_document\\source\\data\\maps',file_name)
        with open(file_path) as f:
            self.map_data = json.load(f)

    def setup_background(self):
        self.image_name = self.map_data['image_name']
        self.background = setup.GRAPHICS[self.image_name]
        rect = self.background.get_rect()
        self.background = pygame.transform.scale(self.background,(int(rect.width * C.BG_MULTI),
                                                                  int(rect.height * C.BG_MULTI)))
        self.background_rect = self.background.get_rect()
        self.game_window = setup.SCREEN.get_rect()
        self.game_ground = pygame.Surface((self.background_rect.width,self.background_rect.height))

    def setup_start_position(self):
        self.position = []
        for data in self.map_data['maps']:
            self.position.append((data['start_x'],data['end_x'],data['player_x'],data['player_y']))
        self.start_x ,self.end_x , self.player_x , self.player_y = self.position[0]

    def setup_player(self):
        self.player = player.Player('mario')
        self.player.rect.x = self.game_window.x + self.player_x
        self.player.rect.bottom = self.player_y

    def update(self,surface,keys):
        self.player.update(keys)
        self.update_player_position()
        self.update_game_window()
        self.draw(surface)

    def update_player_position(self):
        self.player.rect.x += self.player.x_vel
        if self.player.rect.x < self.start_x:
            self.player.rect.x = self.start_x
        elif self.player.rect.right > self.end_x:
            self.player.rect.right = self.end_x
        self.player.rect.y += self.player.y_vel

    def update_game_window(self):
        third = self.game_window.x + self.game_window.width / 3
        if self.player.x_vel > 0 and self.player.rect.centerx > third and self.game_window.right < self.end_x:
            self.game_window.x += self.player.x_vel
            self.start_x = self.game_window.x

    def draw(self,surface):
        self.game_ground.blit(self.background,self.game_window,self.game_window)
        self.game_ground.blit(self.player.image,self.player.rect)
        surface.blit(self.game_ground,(0,0),self.game_window)
        self.info.draw(surface)