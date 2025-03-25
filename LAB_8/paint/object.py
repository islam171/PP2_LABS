import pygame as pg


class Object:
    def __init__(self, screen, color, pos):
        self.color = color
        self.pos = pos
        self.screen = screen
        self.surface = pg.surface.Surface((20, 20))
        self.surface.fill(self.color)
        self.surfaceRect = self.surface.get_rect(center=self.pos)
            
    def draw(self):        
        self.screen.blit(self.surface, self.surfaceRect)