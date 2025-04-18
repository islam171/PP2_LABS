import pygame as pg
from pygame.math import Vector2
import random
import sys
from food import Food
from player import Player
from inputBox import InputBox
import psycopg2
from button import Button

DB_HOST = "localhost"
DB_NAME = "snake"
DB_USER = "postgres"
PASSWORD = "2149pyKab!@"

try:
    conn = psycopg2.connect(host=DB_HOST, dbname=DB_NAME, user=DB_USER, password=PASSWORD, port="5432")
    cur = conn.cursor()
except (psycopg2.DatabaseError) as error:
    print(error)

pg.init()

screen = pg.display.set_mode((400, 400))
pg.display.set_caption("Snake")
running = True
FPS = 60
clock = pg.time.Clock()


class Game:

    ceil__size = 20
    ceil__number = 20
    center_x = center_y = ceil__number/2*ceil__size
    points = 0
    level = 1
    level__points = points
    speed = 1
    interval = 200
    status = "Init"

    isLogin = False
    user_id = ''
    user_info_text = ''
    user_info_font = pg.font.Font(None, 20)

    def __init__(self, screen):
        self.screen = screen
        
        # create player and food
        self.player = Player(self.screen)
        self.food = Food(self.screen)
        # init Buttons
        self.inputBox = InputBox(self.center_x, 50)
        self.playButton = Button(self.screen, (255, 0, 0), self.center_x, self.center_y+50, 100, 40, "Play", self.play) 
        self.saveButton = Button(self.screen, (255, 0, 0), self.center_x, self.center_y, 100, 40, "Save and exit", self.game__quit)
        self.restartButton = Button(self.screen, (255, 0, 0), self.center_x, self.center_y+50, 100, 40, "Restart", self.restart)
            
        # create text object for score and level
        self.score__text = pg.font.Font(None, 20)
        self.level__text = pg.font.Font(None, 20)

    # ======== process of game ========
    def play(self):
        if self.isLogin: 
            self.status = "Play"
            self.last_time_food  = self.last_time_move = self.current_time = pg.time.get_ticks()
            self.spawnFood()

    def pause(self):
        self.status = "Pause"

    # close program
    def game__over(self):
        self.status = "Pause"

    def game__quit(self):
        self.save()
        pg.quit()
        sys.exit()

    def restart(self):
        self.save()
        self.last_time_food  = self.last_time_move = self.current_time = pg.time.get_ticks()
        self.level = 0
        self.level__points = 0
        self.points = 0
        self.speed = 1
        self.player = Player(self.screen)
        self.food = Food(self.screen)
        self.spawnFood()
        self.status = "Play"   
    # ======= process of game ===========


    # draw all elements
    def update(self, events, pressed):
        if self.status == "Play":
            self.current_time = pg.time.get_ticks()
            self.player.draw()
            self.food.draw()
            self.check__fail()
            self.check__food()
            self.points_text = self.score__text.render(f"Score: {self.points} points", True, (255, 100 ,0))
            self.level_text = self.score__text.render(f"Level: {self.level}", True, (255, 100 ,0))
            self.screen.blit(self.points_text, (10, 10))
            self.screen.blit(self.level_text, (330, 10))
            # move snake
            self.move()
            # check time of food respawn 
            self.respawnFood()

            #Check key down
            if pressed[pg.K_RIGHT]:
               game.player.right()
            if pressed[pg.K_LEFT]:
                game.player.left()
            if pressed[pg.K_UP]:
                game.player.up()
            if pressed[pg.K_DOWN]:
                game.player.down()
            if pressed[pg.K_ESCAPE]:
                game.pause()   
             
        elif self.status == "Init":
            # draw inputbox and button for play
            self.inputBox.Render(self.screen)
            self.playButton.draw()

            # info of user
            user_info_surface = self.user_info_font.render(self.user_info_text, True, (255, 100 ,0))
            self.screen.blit(user_info_surface, (self.center_x-user_info_surface.get_width()/2, 100))

            for event in events:
                self.playButton.check_action(event)
                if event.type == pg.MOUSEBUTTONDOWN:
                    self.inputBox.toggleActive(event)
                if event.type == pg.KEYDOWN:
                    if self.inputBox.get__status():
                        if event.key == pg.K_RETURN:
                            self.login(self.inputBox.text)
                        elif event.key == pg.K_BACKSPACE:
                            self.inputBox.delete()
                        else:
                            self.inputBox.enter__text(event.unicode)                  

        elif self.status == "Pause":
            for event in events:
                self.saveButton.check_action(event)
                self.restartButton.check_action(event)
            self.saveButton.draw()
            self.restartButton.draw()

    # ======= checking =======
            
    def check__food(self):
        # if position of head of player is equal to position of food  
        if self.player.getHeadPos() == self.food.getPos():
            # add point and grow player and spawn food on new position 
            self.add__points(self.food.getWeight())
            self.player.grow()
            self.spawnFood()
            # if level points is greater than 5 then increase level 
            if(self.level__points >= 5):
                self.add__level()
                self.level__points = 0
 
    def check__fail(self):
        self.player.checkBiteItself()
        if self.player.getFail():
            self.game__over()
        # if head position of player touch borders then game over 
        if (not 0 <= self.player.getHeadPos().x < self.ceil__number) or (not 0 <= self.player.getHeadPos().y < self.ceil__number):
              self.game__over()

    # ====== checking ======

    # ====== FEATURES ======
    # add points
    def add__points(self, point):
        self.points += point 
        self.level__points += point

    # add level
    def add__level(self):
        self.level += 1
        self.speed += 1
    
    def move(self):
        # every interval move snake on one element 
        # when speed increase interval decrease
        if self.current_time - self.last_time_move >= 200 - game.speed*10:
            self.player.move()
            self.last_time_move = self.current_time 
  
    def spawnFood(self):  
        while True:
            # generate random position
            x = random.randint(0, self.ceil__number-1)
            y = random.randint(0, self.ceil__number-1)
            # add weight food
            weight = random.randint(1, 5)
            pos = Vector2(x, y)
            # if position (x, y) is not equal to position of player then exit cycle  
            if not self.player.checkPos(pos):
                break

        self.food.spawn(x, y, weight)
        self.last_time_food = self.current_time

    def respawnFood(self):
        if self.current_time - self.last_time_food >= 5000-self.speed*100:
            self.spawnFood()         
            self.last_time_food = self.current_time

    # ======= SQL LOGIC =======

    def save(self):
        # save result of user
        cur.execute("insert into user_score (user_id, level, score) values (%s, %s, %s)", [self.user_id, self.level, self.points])
        conn.commit()

    def login(self, name):
        # getting user by name 
        cur.execute("select * from users where name = %s", [name])
        res = cur.fetchone()
        
        # if user does no exits create new user
        if(res is None):
            # create user
            cur.execute('''insert into users (name) values (%s)''', [name])
            conn.commit()
            # get user Id
            cur.execute("select * from users where name = %s", [name])
            res = cur.fetchone()
            level = 1
            score = 0
            user_id = res[0]
        else:
            id = res[0]
            # check score of user 
            cur.execute("select * from user_score where user_id = %s order by score desc", [id])
            res = cur.fetchone()
            if(res is None):
                level = 1
                score = 0
                user_id = id
            else:
                level = res[3]
                score = res[2]
                user_id = res[1]

        self.user_info_text = f"Username: {name}, level: {level}, score: {score}" 
        self.user_id = user_id
        self.isLogin = True

game = Game(screen)

running = True

while running:
    events = []
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        events.append(event)
          
    screen.fill((255,255,255))
    pressed = pg.key.get_pressed()
    game.update(events, pressed)  
        
       
    clock.tick(FPS)
    pg.display.update()

pg.quit()
sys.exit()