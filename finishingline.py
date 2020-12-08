# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 11:33:18 2020

@author: Sofokleous
"""

import pygame

bg_color = pygame.Color("grey")
fg_color = pygame.Color("black")
WIDTH = 1200
HEIGHT = 800

class finishingline(pygame.sprite.Sprite):
    
    
    global screen
    ob_w=80
    ob_h=HEIGHT
    
    def __init__(self):
        super().__init__()
        self.image=pygame.Surface([self.ob_w,self.ob_h])
        self.image.fill(bg_color)
        self.image.set_colorkey(bg_color)
        pygame.draw.line(self.image,fg_color,(WIDTH-50,0),(WIDTH-50,HEIGHT))
        #self.image=pygame.image.load("spaceship.bmp").convert_alpha()
        self.rect=self.image.get_rect()
    