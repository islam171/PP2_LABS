import pygame as pg
from pygame.math import Vector2
import random
import sys
from food import Food
from player import Player

pg.init()

screen = pg.display.set_mode((400, 400))
pg.display.set_caption("Snake")
running = True
FPS = 60
clock = pg.time.Clock()


class Game:

    ceil__size = 20
    ceil__number = 20
    points = 0
    level = 1
    level__points = points
    speed = 1

    def __init__(self, screen):
        self.screen = screen
        
        # create player and food
        self.player = Player(self.screen)
        self.food = Food(self.screen)

        # put food on random position
        self.spawnFood()

        # create text object for score and level
        self.score__text = pg.font.Font(None, 20)
        self.level__text = pg.font.Font(None, 20)

    def move(self):
        self.player.move()
            
    def check__food(self):
        # if position of head of player is equal to position of food  
        if self.player.getHeadPos() == self.food.getPos():
            # add point and grow player and spawn food on new position 
            self.add__points()
            self.player.grow()
            self.spawnFood()
            # if level points is greater than 4 then increase level 
            if(self.level__points >= 4):
                self.add__level()
                self.level__points = 0

    # draw all elements
    def update(self):
        self.player.draw()
        self.food.draw()
        self.check__fail()
        self.check__food()
        self.time_next = self.score__text.render(f"Score: {self.points} points", True, (255, 100 ,0))
        self.level_next = self.score__text.render(f"Level: {self.level}", True, (255, 100 ,0))
        screen.blit(self.time_next, (10, 10))
        screen.blit(self.level_next, (330, 10))
    
    def check__fail(self):
        self.player.checkBiteItself()
        if self.player.getFail():
            self.game__over()
        # if head position of player touch borders then game over 
        if (not 0 <= self.player.getHeadPos().x < self.ceil__number) or (not 0 <= self.player.getHeadPos().y < self.ceil__number):
              self.game__over()

    # add points
    def add__points(self):
        self.points += 1 
        self.level__points += 1

    # add level
    def add__level(self):
        self.level += 1
        self.speed += 1

    # close program
    def game__over(self):
        pg.quit()
        sys.exit()


    def spawnFood(self):  
        while True:
            # generate random position
            x = random.randint(0, self.ceil__number-1)
            y = random.randint(0, self.ceil__number-1)
            pos = Vector2(x, y)
            # if position (x, y) is not equal to position of player then exit cycle  
            if not self.player.checkPos(pos):
                break

        self.food.spawn(x, y)


running = True
game = Game(screen)


last_time = pg.time.get_ticks()
interval = 200

while running:
    current_time = pg.time.get_ticks()
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    if current_time - last_time >= 200-(50*game.speed):
        game.move()
        last_time = current_time  # сбрасываем таймер
  
    
    screen.fill((255,255,255))
    game.update()
    
    pressed = pg.key.get_pressed()
    if pressed[pg.K_RIGHT]:
        game.player.right()
    if pressed[pg.K_LEFT]:
        game.player.left()
    if pressed[pg.K_UP]:
        game.player.up()
    if pressed[pg.K_DOWN]:
        game.player.down()
             
       
    clock.tick(FPS)
    pg.display.update()

pg.quit()
sys.exit()