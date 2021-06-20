import pygame
import sys

"""初始化pygame"""
pygame.init()
"""初始化一个显示窗口"""
screen = pygame.display.set_mode((1200, 800))
"""定义一个背景颜色"""
bg_color = (0, 0, 255)
"""填充背景颜色"""
screen.fill(bg_color)


"""执行死循环保持窗口不关闭"""
while True:
    """遍历所有事件"""
    for event in pygame.event.get():
        """如果单击关闭窗口，则退出此界面"""
        if event.type == pygame.QUIT:
            sys.exit()