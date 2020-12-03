# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 09:37:51 2020

@author: Sofokleous
"""
import pygame
#import random
WIDTH = 1200
HEIGHT = 800
bg_color = pygame.Color("grey")
fg_color = pygame.Color("black")

class obstacles(pygame.sprite.Sprite): #to create a class of the obstacles    
    
    global screen, fg_color,WIDTH,HEIGHT,bg_color
    ob_w=80
    ob_h=40
        
    def __init__(self):
        super().__init__()
        self.image=pygame.Surface([self.ob_w,self.ob_h])
        self.image.fill(bg_color)
        self.image.set_colorkey(bg_color)
        pygame.draw.ellipse(self.image,fg_color,[0,0,self.ob_w,self.ob_h])
        #self.image=pygame.image.load("spaceship.bmp").convert_alpha()
        self.rect=self.image.get_rect()
            
    def show(self):
        pygame.draw.ellipse(screen,fg_color,self.posx, self.posy)
        
        
