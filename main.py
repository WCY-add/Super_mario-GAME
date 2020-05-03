#   -*- coding:utf-8 -*-
#   @Time   :   2020/  /
#   @Author :   goldsunC
#   @Email  :   2428022854@qq.com
#   @Blog   :   https://blog.csdn.net/weixin_45634606

import pygame
from source import tools
from source.states import main_menu,load_screen,level


def main():
    state_dict = {
        'main_menu':main_menu.MainMenu(),
        'load_screen':load_screen.LoadScreen(),
        'level':level.Level()
    }
    game = tools.Game(state_dict,'main_menu')
    game.run()

if __name__ == '__main__':
    main()