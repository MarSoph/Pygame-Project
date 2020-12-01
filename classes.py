# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 09:37:51 2020

@author: Sofokleous
"""
import pygame

class obstacles: #to create a class of the obstacles    
    
    global screen, fg_color
    RADIUS_OBST=20
    MINP_OBST=500

        
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.radius=self.RADIUS_OBST
        self.centre=(x,y)
    
    def show(self):
        pygame.draw.circle(screen, fg_color, self.centre, self.radius)
        
        
class Ship:
    
    global screen, bg_color
    move = 1
    WIDTH=1200
    HEIGHT = 800
    u = pygame.K_UP
    d = pygame.K_DOWN
    l = pygame.K_LEFT
    r = pygame.K_RIGHT
    space=pygame.K_SPACE
    #running=True
    #s_image = pygame.image.load("C:/Users\Sofokleous\OneDrive\Έγγραφα\GitHub\Pygame-Project\spaceship.bmp")
    #s_imgx = 50
    #s_imgy = HEIGHT//2

    def __init__(self,s_imgx,s_imgy,image):
        self.image = image
        self.s_imgx=s_imgx
        self.s_imgy=s_imgy
        self.running=True
    #def show(self):
     #   pygame.image.load("C:/Users\Sofokleous\OneDrive\Έγγραφα\GitHub\Pygame-Project\spaceship.bmp")
        
    def move_m(self):
        #global HEIGHT,WIDTH,bg_color,screen
       #while running:
        ##    for e in pygame.event.get():
          #          if e.type==pygame.QUIT:
              #          pygame.quit()
        #if not self.running:
         #   return
        while self.running:
            
            key_input = pygame.key.get_pressed()
                
            
            if key_input[self.l]:
                self.s_imgx -= self.move
            elif key_input[self.u]:
                self.s_imgy -= self.move
            elif key_input[self.r]:
                self.s_imgx += self.move
            elif key_input[self.d]:
                self.s_imgy += self.move
            elif self.s_imgx <= 0:
                self.s_imgx = 0+10
            elif self.s_imgx >= self.WIDTH:
                self.s_imgx = self.WIDTH
            elif self.s_imgy <= 0:
                self.s_imgy = 0+10
            elif self.s_imgy >= self.HEIGHT:
                self.s_imgy = self.HEIGHT
                
            #self.image.fill(bg_color)  
            screen = pygame.display.set_mode((self.WIDTH,self.HEIGHT))
            screen.blit(self.image, (self.s_imgx, self.s_imgy))
            pygame.display.flip()
            pygame.display.update()
        
    