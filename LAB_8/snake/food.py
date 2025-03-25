import pygame as pg
from pygame.math import Vector2

class Food():

    size = 20

    def __init__(self, screen):
        self.screen = screen
        self.x = 0
        self.y = 0
        # create surface and paint red
        self.image = pg.Surface((self.size, self.size))
        self.image.fill((255, 0, 0))
        
    # set position of food
    def spawn(self, x, y):
        self.x = x
        self.y = y
        self.rect = self.image.get_rect(topleft=(self.x*self.size, self.y*self.size))

    # draw food
    def draw(self):
        self.screen.blit(self.image, self.rect)

    # get position of food to check eating
    def getPos(self):
        pos = Vector2(self.x, self.y)
        return pos
