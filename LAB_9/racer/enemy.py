import pygame as pg
from car import Car
import random

class Enemy(Car):

    def __init__(self, screen):
        super().__init__(screen, "enemy.png")
        # create rect on the top scene
        self.rect.bottom = 0
        self.image = pg.transform.rotate(self.image, 180)
    
    def forward(self):
        self.rect.move_ip(0, self.speed)

    def get__top(self):
        return self.rect.top
    
    # increase speed of enemy
    def increaseSpeed(self):
        self.speed += 1 
    
    def spawn(self):
        # just change place of object
        self.rect.bottom = 0
        self.rect.center = (random.randint(50,350), 0) 