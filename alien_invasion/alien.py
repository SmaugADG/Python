import pygame
from pygame.sprite import Sprite
class Alien(Sprite):
    '''表示单个外星人的类'''
    def __init__(self,ai_game):
        '''初始化外星人并设置其位置'''
        super().__init__()
        self.screen=ai_game.screen
        self.settings=ai_game.settings

        #加载外星人图像并设置其rect值
        self.image=pygame.image.load('images/alien.bmp')
        self.rect=self.image.get_rect()

        #设置外星人位置
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height
        self.x=float(self.rect.x)

    def check_edges(self):
        '''如果外星人位于屏幕边缘及返回True'''
        screen_ract=self.screen.get_rect()
        if self.rect.right>=screen_ract.right or self.rect.left<=0:
            return True


    def update(self):
        '''向右移动外星人'''
        self.x +=(self.settings.alien_speed*
                  self.settings.fleet_direction)
        self.rect.x=self.x



