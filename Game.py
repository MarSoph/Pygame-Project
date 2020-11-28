# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 20:56:36 2020

@author: Sofokleous
"""

import pygame
import os


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