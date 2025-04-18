import pygame as pg
from pygame.math import Vector2

# part of body of Snake
class Block():

    size = 20
    color = (0, 255, 0)

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.pos = Vector2(self.x, self.y)
        # create surface
        self.image = pg.Surface((self.size, self.size))
        self.image.fill(self.color)
        # rect with position multiply by size of ceil
        self.rect = self.image.get_rect(topleft = (self.pos.x*self.size, self.pos.y*self.size))

    # change position
    def move(self, vector: Vector2):
        self.pos = vector