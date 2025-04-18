import pygame as pg
from pygame.math import Vector2
from block import Block

class Player():

    isFail = False

    def __init__(self, screen):
        self.screen = screen
        # list for block
        # block is part of body of Snake 
        self.body = []
        self.direction = Vector2(0,1)
        # add block in body
        for i in range(0,3):
            block = Block(0, i)
            self.body.insert(0, block)
        
    def move(self):
        # remove last element, then add new block to the begin
        # position of new Block = position of first element + direction 
        copy_body = self.body[:-1]
        block = Block(*(self.getHeadPos()+self.direction))
        copy_body.insert(0, block)
        self.body = copy_body

    # change direction
    def right(self):
        if(self.direction.x != -1):
            self.direction = Vector2(1,0)
    def left(self):
        if(self.direction.x != 1):
           self.direction = Vector2(-1,0)
    def up(self):
        if(self.direction.y != 1):
            self.direction = Vector2(0,-1)
    def down(self):
        if(self.direction.y != -1):
            self.direction = Vector2(0,1)
        
    # add new block to the begin without removing the last element
    def grow(self):
        copy_body = self.body
        block = Block(*(self.body[len(self.body)-1].pos))
        copy_body.append(block)
        self.body = copy_body

    # draw body of Snake
    def draw(self):
        for i in self.body:
            self.screen.blit(i.image, i.rect)

    # if Snake bites itself then fail
    def checkBiteItself(self):
        for i in self.body[1:]:
            if i.pos.x == self.body[0].pos.x and i.pos.y == self.body[0].pos.y:
                self.isFail = True
                
    # get properties isFail to check fail conditions
    def getFail(self):
        return self.isFail
    
    # get position of first block of Snake 
    def getHeadPos(self):
        return self.body[0].pos
    
    # check position body of Snake for spawn food
    def checkPos(self, pos: Vector2):
        for i in self.body:
            if pos.x == i.pos.x and pos.y == i.pos.y:
                return True
        return False
