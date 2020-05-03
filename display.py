#   -*- coding:utf-8 -*-
#   @Time   :   2020/  /
#   @Author :   goldsunC
#   @Email  :   2428022854@qq.com
#   @Blog   :   https://blog.csdn.net/weixin_45634606
import pygame

pygame.init()

#设置宽和高
w,h = 1000,500
pygame.display.set_mode((w,h))  #窗口大小
screen = pygame.display.get_surface()   #画布对象
#画图的背景图
bgpic = pygame.image.load('C:\\Users\\24280\\Desktop\\111.jpg')
bgpic = pygame.transform.scale(bgpic,(w,h)) #转换图片大小
# 另一张图
mario_image = pygame.image.load('C:\\Users\\24280\\Desktop\\me.jpg')
mario_image = pygame.transform.scale(mario_image,(50,50))

#一个精灵对象
mario = pygame.sprite.Sprite()
#给精灵对象设置显示图片
mario.image = mario_image
#rect是对象的一些参数
mario.rect = mario.image.get_rect()
#x代表横坐标，y代表纵坐标
mario.rect.x,mario.rect.y = int(w/2),int(h/2)
#组群
player_group = pygame.sprite.Group()
player_group.add(mario) #加入精灵



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_DOWN]:
                mario.rect.y +=10
            if keys[pygame.K_UP]:
                mario.rect.y -=10
            if keys[pygame.K_LEFT]:
                mario.rect.x -=10
            if keys[pygame.K_RIGHT]:
                mario.rect.x +=10
    #给屏幕加上画布
    screen.blit(bgpic,(0,0))
    #把精灵画到屏幕
    player_group.draw(screen)
    pygame.display.update()