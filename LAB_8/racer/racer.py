import pygame as pg
import sys
import random
import time


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
        self.screen = screen
        self.image = pg.image.load(image)
        self.rect = self.image.get_rect(center=(self.screen.get_size()[0]/2, self.screen.get_size()[1]/2))
        
    def draw(self):
        self.screen.blit(self.image, self.rect)

class Enemy(Car):
    def __init__(self, screen, image):
        super().__init__(screen, image)
        self.rect.bottom = 0
        self.image = pg.transform.rotate(self.image, 180)
    
    def forward(self, func):
        self.rect.move_ip(0, self.speed)
        if(self.rect.top > self.screen.get_size()[1]):
            self.spawn()
            func()
    
    def spawn(self):
        self.rect.bottom = 0
        self.rect.center = (random.randint(50,350), 0) 

class Player(Car):
    def __init__(self, screen, image):
        super().__init__(screen, image)
        self.speed = 5

    def right(self):
        self.rect.move_ip(self.speed, 0)

    def left(self):
        self.rect.move_ip(-self.speed, 0)




player = Player(screen,  "car.png")
enemy = Enemy(screen, "enemy.png")

enemies = pg.sprite.Group()
enemies.add(enemy)
all_sprites = pg.sprite.Group()
all_sprites.add(player)
all_sprites.add(enemy)

coin = 0

def addCoin():
    global coin
    coin += 1


while running:
    screen.fill((255, 255, 255))
    player.draw()
    enemy.draw()
    scores = font_small.render(str(coin), True,(0,0,0))
    screen.blit(scores, (10, 10))

    pressed = pg.key.get_pressed()

    if pressed[pg.K_RIGHT]:
        player.right()
    if pressed[pg.K_LEFT]:
        player.left()
    
    enemy.forward(addCoin)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

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