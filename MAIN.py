# -*- coding: utf-8 -*-
"""
 ---- WhiteSnake ----
@authors: psxkc1, pcyms6, psxoo4

Main code for the game

By running this code the game starts

"""

import pygame
import random
import os
from obstacles import obstacles
from Ship import Ship
from enemy import Enemy

"""Parameters"""
WIDTH = 1200
HEIGHT = 800
FRAMERATE=50
bg_color = pygame.Color("grey")
fg_color = pygame.Color("black")
objNUMBER=10
x_startpos=0
y_startpos=HEIGHT/2
life=3
WINNING_SCORE=100
score=0 ## are we keeping this?
running = True  
u = pygame.K_UP
d = pygame.K_DOWN
l = pygame.K_LEFT
r = pygame.K_RIGHT

"""----------"""

pygame.init() #to initialise the pygame
pygame.mixer.init()
pygame.font.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("WRITE SOMETHING HERE")
pygame.mixer.music.load("soundpart.wav")
pygame.mixer.Channel(0).play(pygame.mixer.Sound("soundpart.wav"))    
pygame.mixer.music.play(-1)
backim=pygame.image.load("wallpaper1.bmp")
goimg = pygame.image.load("gameoverscreen (2).jpg")

font = pygame.font.SysFont('freesansbold.tiff', 50) 

jefe = pygame.image.load("eljefe.png") # New
chef = pygame.image.load("derchef.png") # New
dirkeys = pygame.image.load("dir.png") # New
bar = pygame.image.load("bar.png") # New

def mainmen():
    """
    This function provides the player with a game menu.
    The interation between it and the other critical functions in this program were inspiried by the youtube tutorial below.

    https://www.youtube.com/watch?v=0RryiSjpJn0
    """
    
    while True:
        x,y = pygame.mouse.get_pos()
        gamebutton = pygame.Rect(-100 + WIDTH/2, -50 + HEIGHT/2, 200, 50)
        guidebutton = pygame.Rect(-100 + WIDTH/2, 50 + HEIGHT/2, 200, 50)

        click = False
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
            if e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == 1:
                    click = True

        if gamebutton.collidepoint((x,y)):
            if click:
                play(objNUMBER=10)

        if guidebutton.collidepoint((x,y)):
            if click:
                guide() 

        pygame.display.update()
        screen.fill(bg_color) #flling the screen
        screen.blit(backim,(0,0))
        pygame.draw.rect(screen, pygame.Color("red"), gamebutton)
        pygame.draw.rect(screen, pygame.Color("red"), guidebutton)
        surf1 = font.render('Play Now', True, pygame.Color("white"))
        screen.blit(surf1,(-80 + WIDTH/2, -40 + HEIGHT/2, 200, 50))
        surf2 = font.render('Guide', True, pygame.Color("white"))
        screen.blit(surf2,(-60 + WIDTH/2, 60 + HEIGHT/2, 200, 50))
        screen.blit(jefe,(0,0))
        screen.blit(chef,(WIDTH - chef.get_width(),0))
        clock.tick(FRAMERATE)

def guide():
    
    #This function Displays a brief guide for the game
    
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

def play(objNUMBER):
    """
    the main function of the game. Creates the obstacles and enemies using the create_objects function\
        which takes as an argument the objNUMBER (the number of the obstacles that will be created by running the play function)\
            which is also the argument of the play function

    Returns the following objects and lists using the function create_object():
    spriteslist :list of all the sprites
    obst_spritelist : list for all the obstacles
    bulls_spritelist : list for all the bullets
    enemies : list of enemy sprites
    obst : the obstacles(black holes), an object of class obstacles
    
    the ship object is also created using this function
    
    It also contains the show function which is used to show text on the screen,\
        and the while loop which contains the logic of the game

    """
    global life,score,WINNING_SCORE
    spriteslist=pygame.sprite.Group() #to initialise a list of all the sprites
    obst_spritelist=pygame.sprite.Group() #initialise a different list for all the obstacles
    bulls_spritelist=pygame.sprite.Group() #initialise a different list for all the bullets
    enemies = pygame.sprite.Group() # list of enemy sprites
    
    def create_objects(objNUMBER): 
        #to create 10 objects called obst from class obstacles
        for i in range(objNUMBER):
            obst=obstacles()
            obst.rect.x=random.randint(WIDTH/5,WIDTH-obst.ob_w)  #random x,y position for each obstacle at each time
            obst.rect.y=random.randint(0,HEIGHT-obst.ob_h)
            spriteslist.add(obst) #add each obst on the list of sprites
            obst_spritelist.add(obst) #add each obst on the obstacle list
            enemy = Enemy("enemy.png",obst.rect.center,enemies)
            spriteslist.add(enemy)
        
        return spriteslist,obst_spritelist,bulls_spritelist,enemies,obst
        
    #to create the object ship from class Ship
    ship=Ship()
    ship.rect.x=0 #start at position 0,height/2
    ship.rect.y=HEIGHT/2
    spriteslist.add(ship) 
    
    def show(text) :
        """
        displace the text, which takes as an argument, on the screen
        """
        font = pygame.font.SysFont('freesansbold.tiff', 50)
        lifedisp=font.render(text, True, (255,0,0))
        screen.blit(lifedisp, (0,0)) 
    
    create_objects(objNUMBER) #calling the function to create the objects and lists
    
    while running:  #main while loop of the game
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
                elif e.type == pygame.QUIT:
                    pygame.quit()
                    os._exit(0)
          
            keys=pygame.key.get_pressed()
            if keys[u]:
                ship.move_Up()
            if keys[d]:
                ship.move_Down()
            if keys[l]:
                ship.move_Backwards()
            if keys[r]:
                ship.move_Forward()
            
            if score==WINNING_SCORE: 
                """
                If the score reaches the WINNING_SCORE value the difficulty of the game increases\
                    by restarting the game with 10 more obstacles.
                The value of the life stays the same but the score increases by 100.
                Therefore, the WIINNING_SCORE increases too
                """
                score+=100
                objNUMBER+=10
                WINNING_SCORE+=100+10*(objNUMBER-3) #subtructing 3 so that\
                                            #it will be slighly easier to reach the next level of difficulty
                play(objNUMBER) #restarting the game with the new number of obstacles

            ship_collisionlist=pygame.sprite.spritecollide(ship,obst_spritelist,False)
            for obstacle in ship_collisionlist: #ship collides with obstacles
                life-=1
                ship.rect.x=x_startpos #starting at position after running into an obstacle
                ship.rect.y=y_startpos
                pygame.mixer.Channel(2).play(pygame.mixer.Sound("zap.wav"))
                
            ship_encollisionlist=pygame.sprite.spritecollide(ship,enemies,False)
            for en in ship_encollisionlist: #ship collides with enemies
                life-=1
                ship.rect.x=x_startpos #starting at position after running into an obstacle
                ship.rect.y=y_startpos
                pygame.mixer.Channel(2).play(pygame.mixer.Sound("zap.wav"))
            
            #checking if a bullet is collided with an enemy and removes both the bullet and the enemy from the sprites list        
            bull_en_gcollisionlist=pygame.sprite.groupcollide(bulls_spritelist, enemies, True, True)
            for i in bull_en_gcollisionlist:
                score+=10
        
            #checking if a bullet is collided with an obstacle and removes the bullet from the sprites list        
            bull_obst_gcollisionlist=pygame.sprite.groupcollide(bulls_spritelist, obst_spritelist, True, False)
        
            #game logic here    
            screen.fill(bg_color) #flling the screen
            screen.blit(backim,(0,0))
            spriteslist.update()
            
            spriteslist.draw(screen) #draws all the sprites
            
            #display lives and score on screen
            show('Lives: '+str(life) + " score: " +str(score))
            pygame.display.flip() #to update the screen

        elif life == 0:
            screen.blit(goimg, (0,0)) #to show the gameover picture on the screen
            pygame.display.flip()
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit()
                    os._exit(0)
                elif e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_RETURN:
                        life = 3
                        score=0
                        WINNING_SCORE=100
                        mainmen()
    
        clock.tick(FRAMERATE)
        
mainmen() 
pygame.quit() 
os._exit(0)