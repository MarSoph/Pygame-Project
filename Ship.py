# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 21:13:52 2020

@author: Sofokleous
"""
import pygame
from Bullet import bullets
WIDTH = 1200
HEIGHT = 800
bg_color = pygame.Color("grey")
fg_color = pygame.Color("black")
border=50

class Ship(pygame.sprite.Sprite):
    
    global screen, bg_color, bg_image
    move = 5

    def __init__(self): 
        super().__init__()
        #self.image=pygame.Surface([x,y])
        #self.image.fill(bg_color)
        #self.image.set_colorkey(bg_color)
        self.image=pygame.image.load("C:/Users\Sofokleous\OneDrive\Έγγραφα\GitHub\Pygame-Project\spaceship.bmp").convert_alpha()
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