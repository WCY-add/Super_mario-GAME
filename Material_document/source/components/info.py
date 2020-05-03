#   -*- coding:utf-8 -*-
#   @Time   :   2020/  /
#   @Author :   goldsunC
#   @Email  :   2428022854@qq.com
#   @Blog   :   https://blog.csdn.net/weixin_45634606
import pygame
from .. import constants as C
from . import coin
from  .. import setup,tools
pygame.font.init()

class Info:
    def __init__(self,state):
        self.state = state
        self.create_state_labels()  #   state_labels是菜单界面的静态信息
        self.create_info_labels()   #   info_labels是贯穿全局且可能会变得动态信息
        self.flash_coin = coin.FlashingCoin()   #   这就是唯一得那个小金币

    def create_state_labels(self):
        self.state_labels = []
        #   菜单界面
        if self.state == 'main_menu':
            #   将需要的字体标签对象增加至列表时是和一个元组组合成一个新元组一起增加，元组是该标签将在的位置
            self.state_labels.append((self.create_label('1  PLAYER  GAME'), (272, 360)))
            self.state_labels.append((self.create_label('2  PLAYER  GAME'), (272, 405)))
            self.state_labels.append((self.create_label('TOP - '), (290, 465)))
            self.state_labels.append((self.create_label('000000'), (400, 465)))
        #   加载界面
        elif self.state == 'load_screen':
            self.state_labels.append((self.create_label('WORLD'),(280,200)))
            self.state_labels.append((self.create_label('1 - 1'),(430,200)))
            self.state_labels.append((self.create_label('X    3'),(380,280)))
            self.player_image = tools.get_image(setup.GRAPHICS['mario_bros'],178,32,12,16,(0,0,0),C.BG_MULTI)

    def create_info_labels(self):
        self.info_labels = []
        self.info_labels.append((self.create_label('MARIO'),(75,30)))
        self.info_labels.append((self.create_label('WORLD'), (450, 30)))
        self.info_labels.append((self.create_label('TIME'), (625,30)))
        self.info_labels.append((self.create_label('000000'), (75, 55)))
        self.info_labels.append((self.create_label('x00'), (300, 55)))
        self.info_labels.append((self.create_label('1 - 1'), (480, 55)))

    #   创建字体对象，设置相关属性，最终返回字体图像对象
    def create_label(self,label,size=40,width_scale = 1.25,height_scale = 1):
        #   新创建字体对象，设置字体样式
        font = pygame.font.SysFont(C.FONT,size)
        #   字体图片，label即标签也就是字体内容，第二个参数试了0和1发现置1是字体更完整，最后为颜色
        label_image = font.render(label,1,(255,255,255))
        #   得到字体图像的区域,主要也还是宽和高，位置还是(0，0)
        rect = label_image.get_rect()
        #   放缩
        label_image = pygame.transform.scale(label_image,(int(rect.width * width_scale),
                                                              int(rect.height * height_scale)))
        return label_image

    def update(self):
        self.flash_coin.update()

    def draw(self,surface):
        for label in self.state_labels:
            surface.blit(label[0],label[1])
        for label in self.info_labels:
            surface.blit(label[0],label[1])
        surface.blit(self.flash_coin.image,self.flash_coin.rect)

        if self.state == 'load_screen':
            surface.blit(self.player_image,(300,270))