import pygame as pg
from car import Car

class Player(Car):
    def __init__(self, screen):
        super().__init__(screen,  "car.png")
        self.speed = 5
    # move right player
    def right(self):
        if(self.rect.x+self.size[0] < self.screen.get_size()[0]):
            self.rect.move_ip(self.speed, 0)
    # move right player
    def left(self):
        if(self.rect.x > 0):
            self.rect.move_ip(-self.speed, 0)