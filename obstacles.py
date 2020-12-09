# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 09:37:51 2020

 ---- WhiteSnake ----
"""
import pygame
WIDTH = 1200
HEIGHT = 800
bg_color = pygame.Color("grey")
fg_color = pygame.Color("black")

class obstacles(pygame.sprite.Sprite): #to create a class of the obstacles

    """
    Class obstacles used to create the obstacles on the screen
    
    The following websites were used as an inspiration in working with sprites
    1.	https://www.pygame.org/docs/tut/SpriteIntro.html
    2.	https://www.101computing.net/creating-sprites-using-pygame/
    3.  https://stackoverflow.com/questions/22108232/pygame-sprite-sprite-classes


    """    
    
    global screen, fg_color,WIDTH,HEIGHT,bg_color
    ob_w=80
    ob_h=40
        
    def __init__(self):
        super().__init__()
        self.image=pygame.Surface([self.ob_w,self.ob_h])
        self.image.fill(bg_color)
        self.image.set_colorkey(bg_color)
        pygame.draw.ellipse(self.image,fg_color,[0,0,self.ob_w,self.ob_h])
        self.rect=self.image.get_rect()
            
    def show(self):
        pygame.draw.ellipse(screen,fg_color,self.posx, self.posy)
        
        
