# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 20:56:36 2020

@author: Sofokleous
"""

import pygame
import os
from classes import obstacles

WIDTH = 1200
HEIGHT = 800
FRAMERATE=50

life=0
score=0



pygame.init() #to initialise the pygame

clock = pygame.time.Clock()

screen = pygame.display.set_mode((WIDTH,HEIGHT))

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

pygame.display.flip()


while True:
    #need to write the instractions here 
    #show(F"lives = {lives} , points = {points}")
    e = pygame.event.poll()
    if e.type == pygame.QUIT:
        break
    
pygame.display.flip()
clock.tick(FRAMERATE)

pygame.quit() 
os._exit(0)