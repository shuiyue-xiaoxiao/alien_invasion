import pygame
import sys

"""初始化pygame"""
pygame.init()

"""定义窗口的宽度和高度，然后调用显示窗口方法"""
s = height, width = 1200, 800
screen = pygame.display.set_mode(s)

"""声明窗口背景色颜色，然后加载图片，获取矩形区域"""
color = (0, 0, 0)
load = pygame.image.load("../images/concept_car.bmp")
RA = load.get_rect()
pygame.rect.midbottom = pygame.screen_rect.midbottom()

"""填充窗口颜色，将图片画在窗口上，然后更新全部显示"""
screen.fill(color)
screen.blit(load, RA)
pygame.display.flip()

"""使用while循环语句判断，设置循环保证窗口一直显示"""
while True:
    for event in pygame.event.get():
        """如果单击关闭窗口，则退出此界面"""
        if event.type == pygame.QUIT:
            sys.exit()