# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 23:15:37 2020

@author: ken_c
"""
import pygame


pygame.init()
pygame.mixer.init()
pygame.display.init()

width = 1500
height = 600
u = pygame.K_UP
d = pygame.K_DOWN
l = pygame.K_LEFT
r = pygame.K_RIGHT
space=pygame.K_SPACE
move = 1
screen = pygame.display.set_mode((width,height))
screen.fill(pygame.Color('yellow'))

s_image = pygame.image.load("C:/Users\Sofokleous\OneDrive\Έγγραφα\GitHub\Pygame-Project\spaceship.png")
s_imgx = 50
s_imgy = height//2
x = 1
y = 1
pygame.mixer.music.load("C:/Users\Sofokleous\OneDrive\Έγγραφα\GitHub\Pygame-Project\Moderat - Ramadan.mp3")
pygame.mixer.music.play(-1)

running = True 



class Ship:
    def __init__(self, image):
        self.image = image
    def move(self):
        global s_imgx, s_imgy, running
        while running:
            
                
            for e in pygame.event.get():
                    if e.type==pygame.QUIT:
                        pygame.quit()
                    
            key_input = pygame.key.get_pressed()  
            if key_input[l]:
                s_imgx -= move
            if key_input[u]:
                s_imgy -= move
            if key_input[r]:
                s_imgx += move
            if key_input[d]:
                s_imgy += move
            if s_imgx <= 0:
                s_imgx = 1500
            elif s_imgx >= 1500:
                s_imgx = 0
            if s_imgy <= 0:
                s_imgy = 600
            elif s_imgy >= height:
                s_imgy = 0
            
            screen.fill(pygame.Color('Yellow'))
            screen.blit(s_image, (s_imgx, s_imgy))
            
                
            pygame.display.flip()
            pygame.display.update()
            
            
                    
    
    
    
    

ship = Ship
ship.move(ship)

while True:
    e = pygame.event.poll()
    if e.type == pygame.QUIT:
        break
    pygame.display.update()
    
       
      
pygame.quit()


