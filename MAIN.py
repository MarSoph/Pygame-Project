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
WINNING_SCORE=80
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
pygame.mixer.music.load("Moderat - Ramadan.mp3")
pygame.mixer.Channel(0).play(pygame.mixer.Sound("Moderat - Ramadan.mp3"))    
pygame.mixer.music.play(-1)
backim=pygame.image.load("wallpaper1.bmp")
goimg = pygame.image.load("gameoverscreen (2).jpg")

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
    finlinelist=pygame.sprite.Group()
    
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
                WINNING_SCORE+=100+10*(objNUMBER-life) #subtructing the value of life so that\
                                            #if the player lost 1 or 2 lives they can still reach the next level
                play(objNUMBER) #restarting the game with the new number of obstacles

            ship_collisionlist=pygame.sprite.spritecollide(ship,obst_spritelist,False)
            for obstacle in ship_collisionlist: #ship collides with obstacles
                life-=1
                ship.rect.x=x_startpos #starting at position after running into an obstacle
                ship.rect.y=y_startpos
                pygame.mixer.Channel(2).play(pygame.mixer.Sound("zap.mp3"))
                
            ship_encollisionlist=pygame.sprite.spritecollide(ship,enemies,False)
            for en in ship_encollisionlist: #ship collides with enemies
                life-=1
                ship.rect.x=x_startpos #starting at position after running into an obstacle
                ship.rect.y=y_startpos
                pygame.mixer.Channel(2).play(pygame.mixer.Sound("zap.mp3"))
            
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
                        play(objNUMBER)
    
        clock.tick(FRAMERATE)
        
play(objNUMBER) #the game starts by calling the play function 
pygame.quit() 
os._exit(0)