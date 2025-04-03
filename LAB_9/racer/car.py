import pygame as pg

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