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
        self.state = 'stand'

        self.face_right = True
        self.dead = False
        self.big = False

    def setup_velocities(self):
        #关于速度的一些数值
        speed = self.player_data['speed']
        self.x_vel = 0
        self.y_vel = 0

        #   vel = velocity速度
        #   accel = accelorate加速
        #   turn = turnover转身
        self.max_walk_vel = speed['max_walk_speed']
        self.max_run_vel = speed['max_run_speed']
        self.max_y_vel = speed['max_y_velocity']
        self.jump_vel = speed['jump_velocity']
        self.walk_accel = speed['walk_accel']
        self.run_accel = speed['run_accel']
        self.turn_accel = speed['turn_accel']#急刹车转身时加速度
        self.gravity = C.GRAVITY

        self.max_x_vel = self.max_walk_vel
        self.x_accel = self.walk_accel


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
        self.handle_states(keys)

    def handle_states(self,keys):
        if self.state == 'stand':
            self.stand(keys)
        elif self.state == 'walk':
            self.walk(keys)
        elif self.state == 'jump':
            self.jump(keys)
        elif self.state == 'basketball':
            self.play_basketball(keys)

        if self.face_right:
            self.image = self.right_frames[self.frame_index]
        else:
            self.image = self.left_frames[self.frame_index]


    def stand(self,keys):
        self.frame_index = 0
        self.x_vel = 0
        self.y_vel = 0
        if keys[pygame.K_RIGHT]:
            self.face_right = True
            self.state = 'walk'
        elif keys[pygame.K_LEFT]:
            self.face_right = False
            self.state = 'walk'
    def walk(self,keys):
        self.max_x_vel = self.max_walk_vel
        self.x_accel = self.walk_accel
        if self.current_time - self.walking_timer > 100:
            if self.frame_index < 3:
                self.frame_index += 1
            else:
                self.frame_index = 1
            self.walking_timer = self.current_time
        if keys[pygame.K_RIGHT]:
            self.face_right = True
            if self.x_vel < 0 :
                self.frame_index = 5
                self.x_accel = self.turn_accel
            self.x_vel = self.calc_vel(self.x_vel,self.x_accel,self.max_x_vel,True)
        elif keys[pygame.K_LEFT]:
            self.face_right = False
            if self.x_vel > 0:
                self.frame_index = 5
                self.x_accel = self.turn_accel
            self.x_vel = self.calc_vel(self.x_vel,self.x_accel,self.max_x_vel,False)
        else:
            if self.face_right:
                self.x_vel -= self.x_accel
                if self.x_vel < 0:
                    self.x_vel = 0
                    self.state = 'stand'
            else:
                self.x_vel += self.x_accel
                if self.x_vel > 0 :
                    self.x_vel = 0
                    self.state = 'stand'
    def jump(self,keys):
        pass
    def play_basketball(self,keys):
        pass
    def calc_vel(self,vel,accel,max_vel,is_positive=True):
        if is_positive:
            return min(vel+accel,max_vel)
        else:
            return max(vel-accel,-max_vel)







