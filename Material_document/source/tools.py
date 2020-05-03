#   -*- coding:utf-8 -*-
#   @Time   :   2020/  /
#   @Author :   goldsunC
#   @Email  :   2428022854@qq.com
#   @Blog   :   https://blog.csdn.net/weixin_45634606

import pygame
import random
import os
import sys
class Game:
    def __init__(self,state_dict,start_state):
        self.screen = pygame.display.get_surface()  #获取当前设置的显示表面的参考
        self.clock = pygame.time.Clock()  #一个时钟
        self.keys = pygame.key.get_pressed()  #获得当前键盘上所有按钮的状态，是一个布尔值元组序列
        self.state_dict = state_dict
        self.state = self.state_dict[start_state]   #游戏状态

    def update(self):
        #   如果当前状态完成
        if self.state.finished :
            next_state = self.state.next
            self.state.finished = False
            self.state = self.state_dict[next_state]

        #   否则跳到MainMenu的update
        self.state.update(self.screen,self.keys)

    def run(self):
        while True:
            for event in pygame.event.get():
                #如果窗口被叉则屏幕展示结束进程结束
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    sys.exit()
                #如果键盘被按下或者被释放都更新按钮状态
                elif event.type == pygame.KEYDOWN:
                    self.keys = pygame.key.get_pressed()
                elif event.type == pygame.KEYUP:
                    self.keys = pygame.key.get_pressed()
            #更新
            self.update()

            pygame.display.update()
            self.clock.tick(60)
def load_graphics(path,accept=('.jpg','.png','.bmp','.gif')):
    graphics = {}
    for pic in os.listdir(path):
        name,ext = os.path.splitext(pic)
        if ext.lower() in accept:
            img = pygame.image.load(os.path.join(path,pic))
            if img.get_alpha():
                img = img.convert_alpha()
            else:
                img = img.convert()
            graphics[name] = img
    return graphics



    # 调用pygame.Surface()以创建新的图像对象。Surface将被清除为全黑。唯一需要的参数是尺寸。
    # 如果没有其他参数，Surface将以与显示Surface最匹配的格式创建。
    # 可以通过传递位深度或现有Surface来控制像素格式。flags参数是表面附加功能的位掩码。您可以传递这些标志的任意组合：
    # HWSURFACE, creates the image in video memory
    # SRCALPHA, the pixel format will include a per-pixel alpha
    # 这两个标志只是一个请求，可能不适用于所有显示和格式。
    # 高级用户可以将一组位掩码与深度值组合在一起。掩码是一组4个整数，表示像素中的哪些位代表每种颜色。Normal Surfaces不应该需要mask参数。
    # 曲面可以有许多额外的属性，如alpha平面，颜色键，源矩形剪裁。这些函数主要影响Surface如何与其他Surface进行blit。
    # blit例程将尽可能尝试使用硬件加速，否则他们将使用高度优化的软件blitting方法。


#   此方法非常重要
def get_image(sheet,x,y,width,height,colorkey,scale):
    #   创建一个图像对象，是全黑的，等会将抠出的图像放在其上
    image = pygame.Surface((width,height))
    #   X.blit(Y)将Y的图像绘制到X上
    #   sheet是要绘制的图像，dest(0,0)是绘制在X上的位置，(x,y,width,height)即要绘制Y的矩形区域(left,top,width,height)
    image.blit(sheet,(0,0),(x,y,width,height))
    #   抠图，colorkey是底色，会自动将不是colorkey颜色的其余图像抠出来
    image.set_colorkey(colorkey)
    #   将图片放缩成合适比例
    image = pygame.transform.scale(image,(int(width*scale),int(height*scale)))
    return image