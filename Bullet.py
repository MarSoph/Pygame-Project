# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 15:18:17 2020

@author: Sofokleous
"""
import pygame
WIDTH = 1200

class bullets(pygame.sprite.Sprite):
    vel=10 #velocity
    global WIDTH
    
    def __init__(self,x,y):
        super().__init__()
        self.image=pygame.image.load("C:/Users/Sofokleous/OneDrive/Έγγραφα/GitHub/Pygame-Project/bullettt.jpg").convert_alpha()
        self.rect=self.image.get_rect(center=(x+59,y+27))
        
    def update(self):
        self.rect.x+=self.vel
        #self.rect.y=self.rect.y
        if self.rect.x>=WIDTH+100:
            self.kill
        
        
        
        