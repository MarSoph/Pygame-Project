# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 15:18:17 2020

@author: Sofokleous
"""
import pygame


class bullets(pygame.sprite.Sprite):
    vel=100 #velocity
    
    def __init__(self,x,y):
        super().__init__()
        self.image=pygame.image.load("C:/Users/Sofokleous/OneDrive/Έγγραφα/GitHub/Pygame-Project/bullettt.jpg").convert_alpha()
        self.rect=self.image.get_rect(center=(x,y))
        
    def position(self):
        self.rect.x+=self.vel
        #self.rect.y=self.rect.y
        
        
        
        