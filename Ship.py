# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 21:13:52 2020

 ---- WhiteSnake ----
"""
import pygame
import os,sys
from Bullet import bullets
WIDTH = 1200
HEIGHT = 800
border=50

class Ship(pygame.sprite.Sprite):
    
    """
    The class Ship is used to create the spaceship
    https://www.101computing.net/pygame-how-to-control-your-sprite/
    """

    move = 5

    def __init__(self): 
        super().__init__()
        #self.image=pygame.image.load(os.path.join(sys.path[0],"spaceship.bmp")).convert_alpha()
        self.image=pygame.image.load("spaceship.bmp")
        self.rect=self.image.get_rect()
     
    #methods to move the spaceship
    def move_Forward(self):
        if self.rect.x>=WIDTH-border:
            self.rect.x=WIDTH-border
        else:
            self.rect.x+=self.move
            
    def move_Backwards(self):
        if self.rect.x<=0:
            self.rect.x=0
        else:
            self.rect.x-=self.move
            
    def move_Up(self):
        if self.rect.y<=0:
            self.rect.y=0
        else:
            self.rect.y-=self.move
            
    def move_Down(self):
        if self.rect.y>=HEIGHT-border:
            self.rect.y=HEIGHT-border
        else:
            self.rect.y+=self.move
            
    def shoot(self):
        return bullets(self.rect.x,self.rect.y)