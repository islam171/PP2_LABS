import pygame as pg
import sys
from button import Button

pg.init()

screen = pg.display.set_mode((600, 600))
pg.display.set_caption("Paint")
running = True
FPS = 60
clock = pg.time.Clock()

# create game
class Game:
    # color dict
    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    yellow = (255, 255, 0)

    width = 600
    height = 600

    def __init__(self, screen):
        self.screen = screen
        self.currentColor = self.black # current color
        self.brushScale = 5 # scale of brush
        self.brush = "circle" # figure of brush
        # add Button in List
        self.buttonList = [
            Button(30, 15, 20, 20, "", self.black, self.set_black, self.screen),
            Button(60, 15, 20, 20, "", self.blue, self.set_blue, self.screen),
            Button(90, 15, 20, 20, "", self.red, self.set_red, self.screen),
            Button(120, 15, 20, 20, "", self.green, self.set_green, self.screen),
            Button(150, 15, 20, 20, "", self.yellow, self.set_yellow, self.screen),
            Button(180, 15, 50, 20, "rect", self.black, self.changeBrushRect, self.screen),
            Button(240, 15, 50, 20, "circle", self.black, self.changeBrushCircle, self.screen),
            Button(550, 15, 20, 20, "", self.white, self.set_white, self.screen) #eraser
        ]
        
    # change color
    def set_black(self):
        self.currentColor = self.black
    def set_blue(self):
        self.currentColor = self.blue
    def set_green(self):
        self.currentColor = self.green
    def set_red(self):
        self.currentColor = self.red
    def set_yellow(self):
        self.currentColor = self.yellow
    def set_white(self):
        self.currentColor = self.white

    # change figure of brush
    def changeBrushRect(self):
        self.brush = "rect"
    def changeBrushCircle(self):
        self.brush = "circle"

    # change scale of brush
    def increaseBrushScale(self):
        if self.brushScale < 30:
            self.brushScale += 5
    def decreaseBrushScale(self):
        if self.brushScale > 5:
            self.brushScale -= 5

    def update(self):
        # draw elements
        self.drawMenu()
        self.drawButtons()
        
    # draw Menu in top
    def drawMenu(self):
        pg.draw.rect(self.screen, 'gray', [0,0, self.screen.get_size()[0], 50])

    # draw color selectors 
    def drawButtons(self):
        for i in self.buttonList:
            i.draw()   

    # draw rect or circle when user click on the board
    def draw(self, mouse_x, mouse_y):
        if self.brush == "rect":
            pg.draw.rect(self.screen, self.currentColor, (mouse_x, mouse_y, self.brushScale, self.brushScale))   
        else: 
            pg.draw.circle(self.screen, self.currentColor, (mouse_x, mouse_y), self.brushScale)   

running = True
game = Game(screen)
draw_on = False

screen.fill((255,255,255))
while running:
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        # if mouse is pressed then draw
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1: # left click 
                draw_on = True
        # if mouse is not pressed then stop drawing
        if event.type == pg.MOUSEBUTTONUP:
            if event.button == 1: # left click
                draw_on = False

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_KP_PLUS:
                game.increaseBrushScale()
            if event.key == pg.K_KP_MINUS:
                game.decreaseBrushScale()

        for button in game.buttonList:
            button.check_action(event)

        if draw_on:
            mouse_x, mouse_y = pg.mouse.get_pos()
            if mouse_y > 50:
                game.draw(mouse_x, mouse_y)
            
    game.update()

      
    clock.tick(FPS)
    pg.display.flip()

pg.quit()
sys.exit()