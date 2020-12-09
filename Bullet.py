# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 15:18:17 2020

 ---- WhiteSnake ----
"""
import pygame
WIDTH = 1200

class bullets(pygame.sprite.Sprite):
    
    """
    The following websites were used as an inspiration for the mechanism of the bullets
    https://www.youtube.com/watch?v=JmpA7TU_0Ms
    https://stackoverflow.com/questions/21567250/how-to-create-bullets-in-pygame
    """
    vel=10 #velocity
    dim_x=59
    dim_y=27
    global WIDTH
    
    def __init__(self,x,y):
        super().__init__()
        self.image=pygame.image.load("bullettt.jpg").convert_alpha()
        self.rect=self.image.get_rect(center=(x+self.dim_x,y+self.dim_y))
        
    def update(self):
        self.rect.x+=self.vel
        #self.rect.y=self.rect.y
        if self.rect.x>=WIDTH+100: #remove the sprite bullet if it goes beyond the width of the screen+100
            self.kill              #so that the game does not slow down in time
        
        
        
        