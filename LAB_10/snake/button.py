import pygame as pg

class Button:
    def __init__(self, screen, color, x, y, width, height, text, command):
        self.color = color
        self.screen = screen
        self.width = width
        self.height = height
        self.rect = pg.Rect(x-self.width/2, y-self.height/2, width, height)
        self.font = pg.font.Font(None, 20)
        self.text = text
        self.action = command
        

    def draw(self):
        pg.draw.rect(self.screen, self.color, self.rect, 0)
        self.text_surface = self.font.render(self.text, True, (255, 255 ,255))
        self.screen.blit(self.text_surface, (self.rect.x+self.width/2-self.text_surface.get_width()/2, self.rect.y+self.height/2-self.text_surface.get_height()/2))

    def click(self, event):
        return event.type == pg.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos)
    
    def check_action(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.action()