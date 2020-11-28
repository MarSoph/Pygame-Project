# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 09:37:51 2020

@author: Sofokleous
"""

class obstacles: #to create a class of the obstacles    
    
    global screen, fg_color
    RADIUS_OBST=20
    MINP_OBST=500

        
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.radius=self.RADIUS_OBST
        self.centre=(x,y)
    
    def show(self):
        pygame.draw.circle(screen, fg_color, self.centre, self.radius)
        
    