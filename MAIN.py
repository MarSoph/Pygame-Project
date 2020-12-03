# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 20:50:31 2020

Main code for the game

@author: Sofokleous
"""

import pygame
import random
import os
from obstacles import obstacles
from Ship import Ship
from Bullet import bullets

WIDTH = 1200
HEIGHT = 800
FRAMERATE=50
bg_color = pygame.Color("grey")
fg_color = pygame.Color("black")

x_startpos=0
y_startpos=HEIGHT/2
life=3
score=0
running = True 
u = pygame.K_UP
d = pygame.K_DOWN
l = pygame.K_LEFT
r = pygame.K_RIGHT

pygame.init() #to initialise the pygame
pygame.mixer.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("WRITE SOMETHING HERE")
pygame.mixer.music.load("C:/Users\Sofokleous\OneDrive\Έγγραφα\GitHub\Pygame-Project\Moderat - Ramadan.mp3")
pygame.mixer.music.play(-1)
image = pygame.image.load("C:/Users\Sofokleous\OneDrive\Έγγραφα\GitHub\Pygame-Project\spaceship.bmp")
backim=pygame.image.load("C:/Users\Sofokleous\OneDrive\Έγγραφα\GitHub\Pygame-Project\wallpaper1.bmp")

spriteslist=pygame.sprite.Group() #to initialise a list of all the sprites
obst_spritelist=pygame.sprite.Group() #initialise a different list for all the obstacles
bulls_spritelist=pygame.sprite.Group() #initialise a different list for all the bullets

#to create 10 objects called obst from class obstacles
for i in range(10):
    obst=obstacles()
    obst.rect.x=random.randint(WIDTH/5,WIDTH-obst.ob_w)  #random x,y position for each obstacle at each time
    obst.rect.y=random.randint(0,HEIGHT-obst.ob_h)
    spriteslist.add(obst) #add each obst on the list of sprites
    obst_spritelist.add(obst) #add each obst on the obstacle list

#to create the object ship from class Ship
ship=Ship()
ship.rect.x=0 #start at position 0,height/2
ship.rect.y=HEIGHT/2
spriteslist.add(ship) 

def show(text) :
    myFont = pygame.font.SysFont(pygame.font.get_default_font(),40)
    surf = myFont.render(text,False,bg_color,pygame.Color("White"))
    screen.blit(surf,(0,0))

while running:
    #need to write the instractions here 
    #show(F"lives = {lives} , points = {points}")
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running=False
        #elif e.type == pygame.K_SPACE :
         #   bul=ship.shoot()
          #  bulls_spritelist.add(bul)
           # spriteslist.add(bul) 
        
            
    keys=pygame.key.get_pressed()
    if keys[u]:
        ship.move_Up()
    elif keys[d]:
        ship.move_Down()
    elif keys[l]:
        ship.move_Backwards()
    elif keys[r]:
        ship.move_Forward()
    elif keys[pygame.K_SPACE]:
        bul=ship.shoot()
        bul.rect.x<=WIDTH
        #bul.position()
        bulls_spritelist.add(bul)
        #spriteslist.add(bul)
        #bulls_spritelist.update()
        
        
         
    ship_collisionlist=pygame.sprite.spritecollide(ship,obst_spritelist,False)
    for obstacle in ship_collisionlist:
        life-=1
        show(f"You have {life} left") #not a good idea
        #running=False
        ship.rect.x=x_startpos #starting at position after running into an obstacle
        ship.rect.y=y_startpos
    
    #game logic here
    #spriteslist.update()
    #bulls_spritelist.update()
    #obst_spritelist.update()
    
    screen.fill(bg_color) #flling the screen
    screen.blit(backim,(0,0))
    bulls_spritelist.update()
    obst_spritelist.update()
    
    spriteslist.draw(screen) #draws all the sprites
    bulls_spritelist.draw(screen)
   
    pygame.display.flip() #to update the screen

    clock.tick(FRAMERATE)

pygame.quit() 
os._exit(0)