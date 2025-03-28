import pygame as pg
import sys
import time
import os
from player import Player
from coin import Coin
from enemy import Enemy

# change direction to open file 
os.chdir(os.path.dirname(os.path.abspath(__file__)))

pg.init()
screen = pg.display.set_mode((400, 600))
pg.display.set_caption("Racer")
running = True
FPS = 60
clock = pg.time.Clock()
pg.mixer.init()
pg.mixer.music.load('background.wav')
pg.mixer.music.play()

# add font
font = pg.font.SysFont("Verdana", 60)
font_coin = pg.font.SysFont("Verdana", 20)
# text game over
game_over = font.render("Game Over", True, (0,0,0))
game_over_rect = game_over.get_rect(center=(screen.get_size()[0]/2, screen.get_size()[1]/2))
# background
background = pg.image.load("AnimatedStreet.png")
    

player = Player(screen)
enemy = Enemy(screen)
coin = Coin(screen)

# add enemy in group
enemies = pg.sprite.Group()
enemies.add(enemy)

# add enemy in group
coins = pg.sprite.Group()
coins.add(coin)
# add all object in common group
all_sprites = pg.sprite.Group()
all_sprites.add(player)
all_sprites.add(enemy)
all_sprites.add(coin)

points = 0

while running:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    # draw background
    screen.blit(background, (0,0))
    player.draw()
    enemy.draw()
    coin.draw()
    # draw score
    scores = font_coin.render(str(points), True,(0,0,0))
    screen.blit(scores, (screen.get_size()[0]-30, 10))

    pressed = pg.key.get_pressed()
    # track pressing button
    if pressed[pg.K_RIGHT]:
        player.right()
    if pressed[pg.K_LEFT]:
        player.left()
    
    enemy.forward()
    coin.forward()
    # if enemy or coin reach end of road then spawn again
    if(enemy.get__top() > screen.get_size()[1]):
        enemy.spawn()
    if(coin.get__top() > screen.get_size()[1]):
        coin.spawn()
            
    # if coin touch with player then game over
    if pg.sprite.spritecollideany(player, coins):
        points += 1
        coin.spawn()

    # if enemy touch with player then game over
    if pg.sprite.spritecollideany(player, enemies):
        screen.fill((255,0,0))
        screen.blit(game_over, game_over_rect)
        pg.mixer.Sound('crash.wav').play()
        pg.mixer.music.stop()
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