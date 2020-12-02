# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 20:56:36 2020

@author: Sofokleous
"""

import pygame
import os
from classes import obstacles
#from classes import Ship

class Ship:
    
    global screen, bg_color, bg_image
    move = 1
    WIDTH=1200
    HEIGHT = 800
    u = pygame.K_UP
    d = pygame.K_DOWN
    l = pygame.K_LEFT
    r = pygame.K_RIGHT
    space=pygame.K_SPACE

    def __init__(self,s_imgx,s_imgy,image):
        self.image = image
        self.s_imgx=s_imgx
        self.s_imgy=s_imgy
        self.running=True
        self.im_width=image.get_width()
        self.im_height=image.get_height()
        
    def show(self,colour):
        global screen
        pygame.draw.circle(screen, colour, (self.s_imgx+self.im_width/2,self.s_imgy+self.im_width/2),5*self.im_width/8)
        
    def move_m(self):
        
        while self.running:
            for e in pygame.event.get():
                if e.type==pygame.QUIT:
                    pygame.quit()
            new_x=self.s_imgx
            new_y=self.s_imgy
            
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
           
            self.show(bg_color)
            self.s_imgx=new_x
            self.s_imgy=new_y
            screen.blit(self.image, (self.s_imgx, self.s_imgy))
            pygame.display.flip()
            pygame.display.update()


WIDTH = 1200
HEIGHT = 800
FRAMERATE=50
move = 1

life=3
score=0

pygame.init() #to initialise the pygame
pygame.mixer.init()
#pygame.display.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.mixer.music.load("C:/Users\Sofokleous\OneDrive\Έγγραφα\GitHub\Pygame-Project\Moderat - Ramadan.mp3")
pygame.mixer.music.play(-1)
image = pygame.image.load("C:/Users\Sofokleous\OneDrive\Έγγραφα\GitHub\Pygame-Project\spaceship.bmp")
#bg_image=pygame.image.load("C:/Users\Sofokleous\OneDrive\Έγγραφα\GitHub\Pygame-Project\spaceship.bmp")
image.convert()
#running = True 

# Fill the background
bg_color = pygame.Color("grey")
fg_color = pygame.Color("black")

screen.fill(bg_color)

#create a list of objects from class obstacles
obst=[obstacles(5*WIDTH/12,HEIGHT/8),obstacles(6*WIDTH/12,3*HEIGHT/8),\
      obstacles(6*WIDTH/12,7*HEIGHT/8),obstacles(7*WIDTH/12,5*HEIGHT/8),\
          obstacles(8*WIDTH/12,2*HEIGHT/8),obstacles(9*WIDTH/12,6*HEIGHT/8),\
              obstacles(10*WIDTH/12,4*HEIGHT/8),obstacles(11*WIDTH/12,2*HEIGHT/8)]
    
for i in range(len(obst)):
    pygame.draw.circle(screen, fg_color, obst[i].centre, obst[i].radius)
ship = Ship(50,HEIGHT//2,image)
ship.move_m()
#pygame.display.update()

#pygame.display.flip()

while True:
    #pygame.event.get()
    #need to write the instractions here 
    #show(F"lives = {lives} , points = {points}")
    for event in pygame.event.get():
        e = pygame.event.poll()
        if event.type == pygame.QUIT:
            break
        elif event.type == pygame.MOUSEBUTTONDOWN :
            running = True
    #bg_image.fill(bg_color)
    #screen.blit(bg_color,(ship.s_imgx,ship.s_imgy))
    #
            #screen.blit(ship.image, (ship.s_imgx, ship.s_imgy))
        pygame.display.flip()
        pygame.display.update()
    
#pygame.display.flip()
    clock.tick(FRAMERATE)

pygame.quit() 
os._exit(0)