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
#from Bullet import bullets
from enemy import Enemy
pygame.font.init()
#from pygame.math import Vector2

WIDTH = 1200
HEIGHT = 800
FRAMERATE=50
bg_color = pygame.Color("grey")
fg_color = pygame.Color("black")
goimg = pygame.image.load("gameoverscreen (2).jpg")
myfont = pygame.font.SysFont('Comic Sans MS', 30)

x_startpos=0
y_startpos=HEIGHT/2
life=3

score=0 ## are we keeping this?
# running = True  
u = pygame.K_UP
d = pygame.K_DOWN
l = pygame.K_LEFT
r = pygame.K_RIGHT


pygame.init() #to initialise the pygame
pygame.mixer.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("WRITE SOMETHING HERE")
pygame.mixer.music.load("Ramadan.wav")
pygame.mixer.Channel(0).play(pygame.mixer.Sound("Ramadan.wav"))    
pygame.mixer.music.play(-1)
backim=pygame.image.load("wallpaper1.bmp")

jefe = pygame.image.load("eljefe.png") # New
chef = pygame.image.load("derchef.png") # New
dirkeys = pygame.image.load("dir.png") # New
bar = pygame.image.load("bar.png") # New

font = pygame.font.SysFont('freesansbold.tiff', 50)
lifedisp=font.render('Lives: '+str(life), True, (255,0,0))



spriteslist=pygame.sprite.Group() #to initialise a list of all the sprites
obst_spritelist=pygame.sprite.Group() #initialise a different list for all the obstacles
bulls_spritelist=pygame.sprite.Group() #initialise a different list for all the bullets
enemies = pygame.sprite.Group() # list of enemy sprites

#to create 10 objects called obst from class obstacles
for i in range(10):
    obst=obstacles()
    obst.rect.x=random.randint(WIDTH/5,WIDTH-obst.ob_w)  #random x,y position for each obstacle at each time
    obst.rect.y=random.randint(0,HEIGHT-obst.ob_h)
    spriteslist.add(obst) #add each obst on the list of sprites
    obst_spritelist.add(obst) #add each obst on the obstacle list
    enemy = Enemy("enemy.png",obst.rect.center,enemies)
    spriteslist.add(enemy)

#to create the object ship from class Ship
ship=Ship()
ship.rect.x=0 #start at position 0,height/2
ship.rect.y=HEIGHT/2
spriteslist.add(ship) 

click = False # New

myFont = pygame.font.SysFont(pygame.font.get_default_font(),40) # New

def show(text) :
    surf = myFont.render(text,False,bg_color,pygame.Color("White"))
    screen.blit(surf,(0,0))

    

def mainmen():
    global click
    while True:
        # show("Game Name")
        x,y = pygame.mouse.get_pos()
        button_1 = pygame.Rect(-100 + WIDTH/2, -50 + HEIGHT/2, 200, 50)
        button_2 = pygame.Rect(-100 + WIDTH/2, 50 + HEIGHT/2, 200, 50)

        click = False
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
            if e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == 1:
                    click = True

        if button_1.collidepoint((x,y)):
            if click:
                game() 

        if button_2.collidepoint((x,y)):
            if click:
                guide() 

        pygame.display.update()
        screen.fill(bg_color) #flling the screen
        screen.blit(backim,(0,0))
        pygame.draw.rect(screen, pygame.Color("red"), button_1)
        #draw_text('options', font, pygame.Color("white"), button_1, 20, 20)
        pygame.draw.rect(screen, pygame.Color("red"), button_2)
        #draw_text('options', font, pygame.Color("white"), button_2, 20, 20)
        surf1 = font.render('Play Now', True, pygame.Color("white"))
        screen.blit(surf1,(-80 + WIDTH/2, -40 + HEIGHT/2, 200, 50))
        surf2 = font.render('Guide', True, pygame.Color("white"))
        screen.blit(surf2,(-60 + WIDTH/2, 60 + HEIGHT/2, 200, 50))
        screen.blit(jefe,(0,0))
        screen.blit(chef,(WIDTH - chef.get_width(),0))
        clock.tick(FRAMERATE)

def guide():
    running = True
    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    running = False

        pygame.display.update()
        screen.fill(bg_color) #flling the screen
        screen.blit(backim,(0,0))
        # show("Instructions")
        structdisp1 = font.render('INSTRUCTIONS', True, pygame.Color("red")) #display lives on screen
        screen.blit(structdisp1, (-100 + WIDTH/2,HEIGHT/9))
        structdisp2 = font.render('Join space exterminators Thor and Isaac', True, pygame.Color("white"))
        screen.blit(structdisp2, (-140 + WIDTH/3,HEIGHT/6))
        structdisp3 = font.render('as they purge the Delta Star System of', True, pygame.Color("white"))
        screen.blit(structdisp3, (-130 + WIDTH/3,HEIGHT/4))
        structdisp4 = font.render('a deadly gravity leech infestation', True, pygame.Color("white"))
        screen.blit(structdisp4, (-130 + WIDTH/3,HEIGHT/3))
        structdisp5 = font.render('Control the ship with these buttons', True, pygame.Color("white"))
        screen.blit(structdisp5, (-130 + WIDTH/3,HEIGHT/2))
        screen.blit(dirkeys,(-80 + WIDTH/2,HEIGHT/2 + HEIGHT/20))
        structdisp6 = font.render('Fire Tachyon Torpedos with the spacebar', True, pygame.Color("white"))
        screen.blit(structdisp6, (-150 + WIDTH/3,HEIGHT/2 + HEIGHT/8))
        screen.blit(bar,(-110 + WIDTH/2,HEIGHT/2 + HEIGHT/6))
        structdisp7 = font.render('Press Esc to return to the main menu', True, pygame.Color("white"))
        screen.blit(structdisp7, (-130 + WIDTH/3,HEIGHT/2 + HEIGHT/3))
        screen.blit(jefe,(0,0))
        screen.blit(chef,(WIDTH - chef.get_width(),0))
        clock.tick(FRAMERATE)

        

def game():
    global life
    running = True
    while running: 
        if life != 0:
            #need to write the instractions here 
            show(F"lives = {life} , points = {score}") #IT DOESNT WORK
            for e in pygame.event.get():
                if e.type==pygame.KEYDOWN:
                    if e.key == pygame.K_SPACE:
                        bul=ship.shoot()
                        bulls_spritelist.add(bul)
                        spriteslist.add(bul) 
                        pygame.mixer.Channel(1).play(pygame.mixer.Sound("pew.wav"))
                if e.type == pygame.QUIT:
                    pygame.quit()

                
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        running = False
                        mainmen()

            keys=pygame.key.get_pressed()
            if keys[u]:
                ship.move_Up()
            if keys[d]:
                ship.move_Down()
            if keys[l]:
                ship.move_Backwards()
            if keys[r]:
                ship.move_Forward()
            
            
            
            
            
                
            ship_collisionlist=pygame.sprite.spritecollide(ship,obst_spritelist,False)
            for obstacle in ship_collisionlist: #ship collides with obstacles
                life-=1
                show(f"You have {life} left") #not a good idea #IT DOESNT WORK
                #running=False
                ship.rect.x=x_startpos #starting at position after running into an obstacle
                ship.rect.y=y_startpos
                pygame.mixer.Channel(2).play(pygame.mixer.Sound("zap.wav"))
                
            ship_encollisionlist=pygame.sprite.spritecollide(ship,enemies,False)
            for en in ship_encollisionlist: #ship collides with enemies
                life-=1
                show(f"You have {life} left") #not a good idea #IT DOESNT WORK
                #running=False
                ship.rect.x=x_startpos #starting at position after running into an obstacle
                ship.rect.y=y_startpos
                pygame.mixer.Channel(2).play(pygame.mixer.Sound("zap.wav"))
            
            #checking in a bullet is collided with an enemy and removes both the bullet and the enemy from the sprites list        
            bull_en_gcollisionlist=pygame.sprite.groupcollide(bulls_spritelist, enemies, True, True)
        
            #checking in a bullet is collided with an obstacle and removes the bullet from the sprites list        
            bull_obst_gcollisionlist=pygame.sprite.groupcollide(bulls_spritelist, obst_spritelist, True, False)
            
            #game logic here    
            screen.fill(bg_color) #flling the screen
            screen.blit(backim,(0,0))
            spriteslist.update()
            
            spriteslist.draw(screen) #draws all the sprites
            #obst_spritelist.draw(screen)
            #bulls_spritelist.draw(screen)
            #enemies.draw(screen)
            
            lifedisp=font.render('Lives: '+str(life), True, (255,0,0)) #display lives on screen
            screen.blit(lifedisp, (0,0)) 
            pygame.display.flip() #to update the screen
        
        elif life == 0:
            screen.blit(goimg, (0,0))
            pygame.display.flip()
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit()
                elif e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_RETURN:
                        life = 3

        clock.tick(FRAMERATE)
    

      

mainmen()      
    
# show("Game Over") #IT DOESNT WORK

pygame.quit() 
os._exit(0)