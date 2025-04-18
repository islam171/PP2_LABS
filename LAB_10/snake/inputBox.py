import pygame as pg

class InputBox():
    def __init__(self, x, y):
        self.width = 140
        self.height = 32
        self.rect = pg.Rect(x-self.width/2, y-self.height/2, self.width, self.height)
        self.color_inactive = pg.Color('lightskyblue3')
        self.color_active = pg.Color('dodgerblue2')
        self.font = pg.font.Font(None, 32)
        self.color = self.color_inactive
        self.active = False
        self.text = ''
       

    def toggleActive(self, event):
        if self.rect.collidepoint(event.pos):
            self.active = True
            self.color = self.color_active
        else:
            self.active = False
            self.color = self.color_inactive
    
    def clear(self):
        self.text = ''

    def delete(self):
        self.text = self.text[:-1]

    def enter__text(self, text):
        self.text += text

    def get__pos(self, event):
        return 
    
    def get__status(self):
        return self.active

    def Render(self, screen):
        self.txt_surface = self.font.render(self.text, True, self.color)
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the input_box rect.
        pg.draw.rect(screen, self.color, self.rect, 2)
