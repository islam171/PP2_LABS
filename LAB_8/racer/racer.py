import pygame as pg
import sys
import random
import time
import os


pg.init()
screen = pg.display.set_mode((400, 600))
pg.display.set_caption("Racer")
running = True
FPS = 60
clock = pg.time.Clock()

font = pg.font.SysFont("Verdana", 60)
font_small = pg.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, (0,0,0))
game_over_rect = game_over.get_rect(center=(screen.get_size()[0]/2, screen.get_size()[1]/2))

class Car(pg.sprite.Sprite):

    speed = 5

    def __init__(self, screen, image):
        super().__init__()
        self.size = (40, 50)
        self.screen = screen
        self.image = pg.image.load(image)
        self.image = pg.transform.scale(self.image, self.size)
        # get rect
        self.rect = self.image.get_rect(center=(self.screen.get_size()[0]/2, self.screen.get_size()[1]-100))
        
    def draw(self):
        # draw Car 
        self.screen.blit(self.image, self.rect)

class Enemy(Car):

    def __init__(self, screen, image):
        super().__init__(screen, image)
        # create rect on the top scene
        self.rect.bottom = 0
        self.image = pg.transform.rotate(self.image, 180)
    
    def forward(self):
        self.rect.move_ip(0, self.speed)

    def get__top(self):
        return self.rect.top
    
    def spawn(self):
        # just change place of object
        self.rect.bottom = 0
        self.rect.center = (random.randint(50,350), 0) 

class Player(Car):
    def __init__(self, screen, image):
        super().__init__(screen, image)
        self.speed = 5
    # move right player
    def right(self):
        if(self.rect.x+self.size[0] < self.screen.get_size()[0]):
            self.rect.move_ip(self.speed, 0)
    # move right player
    def left(self):
        if(self.rect.x > 0):
            self.rect.move_ip(-self.speed, 0)

# change direction to open file 
os.chdir(os.path.dirname(os.path.abspath(__file__)))

player = Player(screen,  "car.png")
enemy = Enemy(screen, "enemy.png")

# add enemy in group
enemies = pg.sprite.Group()
enemies.add(enemy)
# add all object in common group
all_sprites = pg.sprite.Group()
all_sprites.add(player)
all_sprites.add(enemy)

coin = 0

while running:
    # draw background
    screen.fill((255, 255, 255))
    player.draw()
    enemy.draw()
    # draw score
    scores = font_small.render(str(coin), True,(0,0,0))
    screen.blit(scores, (10, 10))

    pressed = pg.key.get_pressed()
    # track pressing button
    if pressed[pg.K_RIGHT]:
        player.right()
    if pressed[pg.K_LEFT]:
        player.left()
    
    enemy.forward()
    if(enemy.get__top() > screen.get_size()[1]):
        enemy.spawn()
        coin += 1
            
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # if enemy touch with player then game over
    if pg.sprite.spritecollideany(player, enemies):
        screen.fill((255,0,0))
        screen.blit(game_over, game_over_rect)
        pg.display.update()
        for entity in all_sprites:
            entity.kill() 
        time.sleep(2)
        pg.quit()
        sys.exit()

    
    pg.display.update()
    clock.tick(FPS)

pg.quit()
sys.exit()