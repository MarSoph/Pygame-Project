#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 18:10:32 2020

@author: olumide
"""

import pygame
import os,sys
from pygame.math import Vector2
from random import randint

class Enemy(pygame.sprite.Sprite):
    def __init__(self,picture,pos,*group):
        super().__init__(*group)
        #self.image = pygame.image.load(os.path.join(sys.path[0],picture))
        self.image=pygame.image.load(picture)
        self.rect = self.image.get_rect()
        self.pos = Vector2(pos)
        self.offset = Vector2(randint(50,100), 0)
        self.angle = 0

    def update(self):
        self.angle -= randint(0,10)
        # Add the rotated offset vector to the pos vector to get the rect.center.
        self.rect.center = self.pos + self.offset.rotate(self.angle)




    """
    docstring
    """
    