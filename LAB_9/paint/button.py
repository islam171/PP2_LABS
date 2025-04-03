import pygame as pg


class Button:
    def __init__(self, x, y, width, height, text, color, action, screen):
        self.rect = pg.Rect(x, y, width, height)
        self.color = color
        self.action = action
        self.text = text
        self.screen = screen

    def draw(self):
        pg.draw.rect(self.screen, self.color, self.rect)
        font = pg.font.Font(None, 16)
        text_surface = font.render(self.text, True, (255, 255, 255))
        self.screen.blit(text_surface, (self.rect.x+self.rect.h/4, self.rect.y+self.rect.h/4))
    
    def check_action(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.action()