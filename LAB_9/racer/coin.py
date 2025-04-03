import pygame as pg
import random

class Coin(pg.sprite.Sprite):

    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.speed = 5
        self.pos = (0, 0)
        self.size = (20, 20)
        self.weight = 1
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
        self.weight = random.randint(1,5) 

    def draw(self):
        # draw 
        self.screen.blit(self.image, self.rect)

    def get__top(self):
        return self.rect.top
    
    def get__weight(self):
        return self.weight