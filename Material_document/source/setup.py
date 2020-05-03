#   -*- coding:utf-8 -*-
#   @Time   :   2020/  /
#   @Author :   goldsunC
#   @Email  :   2428022854@qq.com
#   @Blog   :   https://blog.csdn.net/weixin_45634606
import pygame

from . import constants as C
from . import tools

pygame.init()
SCREEN = pygame.display.set_mode((C.SCREEN_W,C.SCREEN_H))

GRAPHICS = tools.load_graphics('D:\\练习专用\\py超级玛丽\\Material_document\\resources\\graphics')