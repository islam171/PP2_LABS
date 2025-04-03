import pygame as pg
from car import Car
import random

class Coin(pg.sprite.Sprite):

    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.speed = 5
        self.pos = (0, 0)
        self.size = (20, 20)
        # load image
        self.image = pg.image.load("coin.png")
        self.image = pg.transform.scale(self.image, self.size)
        # get rect
        self.rect = self.image.get_rect()

    def forward(self):
        self.rect.move_ip(0, self.speed)

    def spawn(self):
        self.rect.bottom = 0
        self.rect.center = (random.randint(50,350), 0) 

    def draw(self):
        # draw Car 
        self.screen.blit(self.image, self.rect)

    def get__top(self):
        return self.rect.top