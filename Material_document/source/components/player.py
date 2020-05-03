#   -*- coding:utf-8 -*-
#   @Time   :   2020/  /
#   @Author :   goldsunC
#   @Email  :   2428022854@qq.com
#   @Blog   :   https://blog.csdn.net/weixin_45634606

import pygame
from  .. import tools,setup
from  .. import  constants as C
import json
import os

class Player(pygame.sprite.Sprite):
    def __init__(self,name):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.load_data()

        self.setup_states()
        self.setup_velocities()
        self.setup_timers()
        self.load_images()
    def load_data(self):
        file_name = self.name + '.json'
        file_path = os.path.join('Material_document\\source\\data\\player',file_name)
        with open(file_path) as f:
            self.player_data = json.load(f)

    def setup_states(self):
        #主角状态
        self.state = 'walk'

        self.face_right = True
        self.dead = False
        self.big = False

    def setup_velocities(self):
        #关于速度的一些数值
        self.x_vel = 0
        self.y_vel = 0

    def setup_timers(self):
        self.walking_timer = 0
        self.transition_timer = 0

    def load_images(self):
        sheet = setup.GRAPHICS['mario_bros']
        frame_rects = self.player_data['image_frames']

        self.right_small_normal_frames = []
        self.right_big_normal_frames = []
        self.right_big_fire_frames = []
        self.left_small_normal_frames =[]
        self.left_big_normal_frames = []
        self.left_big_fire_frames = []

        self.small_normal_frames = [self.right_small_normal_frames,self.left_small_normal_frames]
        self.big_normal_frames = [self.right_big_normal_frames,self.left_big_normal_frames]
        self.big_fire_frames = [self.right_big_fire_frames,self.left_big_fire_frames]

        self.all_frames = [
            self.right_small_normal_frames,
            self.right_big_normal_frames,
            self.right_big_fire_frames,
            self.left_small_normal_frames,
            self.left_big_normal_frames,
            self.left_big_fire_frames,
        ]

        self.right_frames = self.right_small_normal_frames
        self.left_frames = self.left_small_normal_frames

        for group,group_frame_rects in frame_rects.items():
            for frame_rect in group_frame_rects:
                right_image = tools.get_image(sheet,frame_rect['x'],frame_rect['y'],
                                              frame_rect['width'],frame_rect['height'],(0,0,0),C.PLAYER_MUTI)
                left_image = pygame.transform.flip(right_image,True,False)
                if group == 'right_small_normal':
                    self.right_small_normal_frames.append(right_image)
                    self.left_small_normal_frames.append(left_image)
                if group == 'right_big_normal':
                    self.right_big_normal_frames.append(right_image)
                    self.left_big_normal_frames.append(left_image)
                if group == 'right_big_fire':
                    self.right_big_fire_frames.append(right_image)
                    self.left_big_fire_frames.append(left_image)



        self.frame_index = 0
        self.frames = self.right_frames
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect()
    def update(self,keys):
        self.current_time = pygame.time.get_ticks()
        if keys[pygame.K_RIGHT]:
            self.x_vel = 5
            self.y_vel = 0
            self.frames = self.right_frames
        if keys[pygame.K_LEFT]:
            self.state = 'walk'
            self.x_vel = -5
            self.y_vel = 0
            self.frames = self.left_frames
        if keys[pygame.K_SPACE]:
            self.state = 'jump'
            self.y_vel = -5
        if self.state == 'walk':
            if self.current_time - self.walking_timer > 100:
                self.walking_timer = self.current_time
                self.frame_index += 1
                self.frame_index %= 4
        if self.state == 'jump':
            self.frame_index = 4
        self.image = self.frames[self.frame_index]