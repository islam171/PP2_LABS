import pygame as pg
from pygame.math import Vector2
import sys
from button import Button
from object import Object

pg.init()

screen = pg.display.set_mode((600, 600))
pg.display.set_caption("Paint")
running = True
FPS = 60
clock = pg.time.Clock()

# create game
class Game:
    # color dict
    colors = {
        "black": (0, 0, 0),
        "red": (255, 0, 0),
        "greed": (0, 255, 0),
        "blue": (0, 0, 255),
        "yellow": (255, 255, 0)
    }
    width = 600
    height = 600

    def __init__(self, screen):
        self.screen = screen
        self.objects = []
        self.buttonList = []
        self.currentColor = self.colors.get("black")

        # add Button in List
        idx = 1
        for i in self.colors.values():
            pos = Vector2(idx*25, 20)
            button = Button(self.screen, i, pos)
            self.buttonList.append(button)
            idx += 1

    def update(self):
        # draw elements
        self.drawMenu()
        self.drawButtons()
        self.drawObjects()
        
    # draw Menu in top
    def drawMenu(self):
        pg.draw.rect(self.screen, 'gray', [0,0, 600, 70])

    # draw color selectors 
    def drawButtons(self):
        for i in self.buttonList:
            i.draw()
        
        self.eraser = Button(self.screen, (135, 135, 135), (580, 20))
        self.eraser.draw()

    # draw objects
    def drawObjects(self):
        for i in self.objects:
            i.draw()

    # click checker
    def click(self, pos: Vector2):
        # if click menu, command not work 
        if pos[1] > 70:
            object = Object(screen, self.currentColor, pos)
            self.objects.append(object)
        # check all buttons
        for i in self.buttonList:
            if i.checkClick(pos):
                self.currentColor = i.getColor()
        
        if self.eraser.checkClick(pos):
            self.currentColor = (255, 255 ,255)
        

running = True
game = Game(screen)
draw_on = False

while running:
    screen.fill((255,255,255))
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
  
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1: # left click grows radius
                pos = pg.mouse.get_pos()
                game.click(pos)
            draw_on = True
        if event.type == pg.MOUSEBUTTONUP:
            draw_on = False
        if event.type == pg.MOUSEMOTION:
            if draw_on:
                pos = pg.mouse.get_pos()
                game.click(pos)
            
    game.update()

      
    clock.tick(FPS)
    pg.display.flip()

pg.quit()
sys.exit()