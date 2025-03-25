import pygame as pg
from pygame.math import Vector2


class Button:
    def __init__(self,screen, color, pos: Vector2):
        self.color = color
        self.screen = screen
        self.surface = pg.surface.Surface((20,20))
        self.surface.fill(self.color)
        self.rect = self.surface.get_rect(center=(pos))

    def draw(self):
        self.screen.blit(self.surface, self.rect)

    def checkClick(self, pos):
        return self.rect.collidepoint(pos)
    
    def getColor(self):
        return self.color
   