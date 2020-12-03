# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 21:13:52 2020

@author: Sofokleous
"""
import pygame
WIDTH = 1200
HEIGHT = 800
bg_color = pygame.Color("grey")
fg_color = pygame.Color("black")
border=50

class Ship(pygame.sprite.Sprite):
    
    global screen, bg_color, bg_image
    move = 5

    def __init__(self,x,y): 
        super().__init__()
        self.image=pygame.Surface([x,y])
        self.image.fill(bg_color)
        self.image.set_colorkey(bg_color)
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
        
    """
    def show(self,colour):
        global screen
        pygame.draw.circle(screen, colour, (self.s_imgx+self.im_width/2,self.s_imgy+self.im_width/2),5*self.im_width/8)
        
    def move_m(self):
        
        new_x=self.s_imgx
        new_y=self.s_imgy
        self.show(bg_color)
        self.s_imgx=new_x
        self.s_imgy=new_y
            
            key_input = pygame.key.get_pressed()
            if key_input[self.l]:
                new_x=self.s_imgx - self.move
            elif key_input[self.u]:
                new_y=self.s_imgy - self.move
            elif key_input[self.r]:
                new_x=self.s_imgx + self.move
            elif key_input[self.d]:
               new_y= self.s_imgy + self.move
            elif self.s_imgx <= 0:
               new_x = 0
            elif self.s_imgx >= self.WIDTH:
                new_x = self.WIDTH-self.im_width
            elif self.s_imgy <= 0:
                new_y = self.im_height
            elif self.s_imgy >= self.HEIGHT:
                new_y = self.HEIGHT-self.im_height
           
            
            #screen.blit(self.image, (self.s_imgx, self.s_imgy))
            #pygame.display.flip()
            #pygame.display.update()
     """
    