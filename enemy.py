#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 ---- WhiteSnake ----
"""

import pygame
import os,sys
from pygame.math import Vector2
from random import randint

class Enemy(pygame.sprite.Sprite):
    """
    Class Enemy is used to create the enemy and define it's movement.
    The stackoverflow post below which describes orbital movement was utlized as inspiration.
    
    https://stackoverflow.com/questions/53639671/making-an-object-move-in-an-orbit-when-i-have-the-x-and-y-coordinates
    """

    def __init__(self,picture,pos,*group):
        super().__init__(*group)
        self.image=pygame.image.load(picture)
        self.rect = self.image.get_rect()
        self.pos = Vector2(pos)
        self.offset = Vector2(randint(50,100), 0)
        self.angle = 0
        
    def update(self):
        self.angle -= randint(0,10)
        self.rect.center = self.pos + self.offset.rotate(self.angle)


    
    