import pygame as pg

pg.init()

screen = pg.display.set_mode((401, 401))
pg.display.set_caption("Snake")
running = True
FPS = 5
clock = pg.time.Clock()

class Ceil(pg.sprite.Sprite):

    size = 20
    color = (0, 0, 0)

    def __init__(self,screen, x, y):
        super().__init__()
        self.screen = screen
        self.x = x
        self.y = y
        self.rect = pg.Rect(x*self.size+1, y*self.size+1, self.size-1, self.size-1)

    def draw(self):
        pg.draw.rect(self.screen, self.color, self.rect)

    def select(self):
        self.color = (0, 255, 0)

class Player(pg.sprite.Sprite):

    speedX = 0
    speedY = 0

    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y

    def right(self):
        self.speedX = 1
        self.speedY = 0
    def left(self):
        self.speedX = -1
        self.speedY = 0
    def down(self):
        self.speedX = 0
        self.speedY = 1
    def up(self):
        self.speedX = 0
        self.speedY = -1

    def update(self):
        self.x += self.speedX
        self.y += self.speedY

running = True
player = Player(0,0)

while running:

    screen.fill((255,255,255))
  
    # Drawing Field
    listCeil = []
    for i in range(0,20):
        for j in range(0, 20):
            ceil = Ceil(screen, i, j)
            listCeil.append(ceil)

    for ceil in listCeil:
        if(ceil.x == player.x and ceil.y == player.y):
            ceil.select()
        ceil.draw()
    

    pressed = pg.key.get_pressed()
    if pressed[pg.K_RIGHT]:
        player.right()
    if pressed[pg.K_LEFT]:
        player.left()
    if pressed[pg.K_UP]:
        player.up()
    if pressed[pg.K_DOWN]:
        player.down()
       
    player.update()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        
    clock.tick(FPS)
    pg.display.update()

pg.quit()