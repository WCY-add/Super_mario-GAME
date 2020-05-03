#   -*- coding:utf-8 -*-
#   @Time   :   2020/  /
#   @Author :   goldsunC
#   @Email  :   2428022854@qq.com
#   @Blog   :   https://blog.csdn.net/weixin_45634606
from  .. import setup
from  .. import tools
from  .. import constants as C
import pygame
from  ..components import info

class MainMenu:
    def __init__(self):
        self.setup_background() #   设置屏幕背景
        self.setup_player() #   放马里奥
        self.setup_cursor() #   放金币
        self.info = info.Info('main_menu')  #   放各种信息
        self.finished = False
        self.next = 'load_screen'   #下一步就是加载界面

    def setup_background(self):
        #   设置背景图
        self.background = setup.GRAPHICS['level_1']

        #   background.get_rect()得到背景图区域:(left,top,width,height)
        #   前两个构成区域左上角在屏幕的坐标，而后两个是区域的宽和高
        self.background_rect = self.background.get_rect()
        #   transform.scale方法用来将图片按比例放缩
        self.background = pygame.transform.scale(self.background,(int(self.background_rect.width*C.BG_MULTI),
                                                                  int(self.background_rect.height*C.BG_MULTI)))
        #   此为设置的屏幕的区域
        self.viewport = setup.SCREEN.get_rect()
        #   这是开始菜单的一部分，将所用图像抠出
        self.caption = tools.get_image(setup.GRAPHICS['title_screen'],1,60,176,88,(255,0,220),C.BG_MULTI)

    def setup_player(self):
        #   抠出的马里奥图像
        self.player_image = tools.get_image(setup.GRAPHICS['mario_bros'],178,32,12,16,(0,0,0),C.PLAYER_MUTI)


#   cursor是游标、光标的意思
    def setup_cursor(self):
        #   sprite.Sprite是一个精灵对象，这是用来管理开始菜单中闪烁的金币
        self.cursor = pygame.sprite.Sprite()
        #   给金币对象设置抠出的金币图像
        self.cursor.image = tools.get_image(setup.GRAPHICS['item_objects'],24,160,8,8,(0,0,0),C.PLAYER_MUTI)
        #   得到金币的区域参数,主要是用来得到宽和高，因为图像位置肯定是(0,0)
        rect = self.cursor.image.get_rect()
        #   设置位置
        rect.x,rect.y = (220,360)
        #   更新
        self.cursor.rect = rect

        self.cursor.state = '1P'  #状态

    def update_cursor(self,keys):
        if keys[pygame.K_UP]:
            self.cursor.state = '1P'
            self.cursor.rect.y = 360
        elif keys[pygame.K_DOWN]:
            self.cursor.state = '2P'
            self.cursor.rect.y = 405
        elif keys[pygame.K_RETURN]:
            #   按下回车代表当前状态完成
            if self.cursor.state == '1P':
                self.finished = True
            elif self.cursor.state == '2P':
                self.finished = True

    def update(self,surface,keys):
        #   先更新按钮触发的状态改变
        self.update_cursor(keys)
        #   新绘图以更新，
        surface.blit(self.background,self.viewport)
        surface.blit(self.caption,(170,100))
        surface.blit(self.player_image,(110,490))
        surface.blit(self.cursor.image,self.cursor.rect)

        self.info.update()  #此处游标仅指金币对象
        self.info.draw(surface)