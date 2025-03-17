import pygame
import datetime

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

bg = pygame.image.load("clock.png")
min_hand = pygame.image.load("min_hand.png")
sec_hand = pygame.image.load("sec_hand.png")

surface = pygame.Surface((800, 600), pygame.SRCALPHA)
rect = surface.get_rect(center=(400, 300))

def secToAngle(sec):
    return int(sec)*6

def correctMinHand(angle):
    return 360-angle-55

def correctSecHand(angle):
    return 360-angle+57

a = 0
running = True
while running:
    pressed = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    x = datetime.datetime.now()

    new_min_hand = pygame.transform.rotate(min_hand, correctMinHand(secToAngle(x.strftime('%M'))))
    min_hand_rect = new_min_hand.get_rect(center=rect.center)

    new_sec_hand = pygame.transform.rotate(sec_hand, correctSecHand(secToAngle(x.strftime('%S'))))
    sec_hand_rect = new_sec_hand.get_rect(center=rect.center)

    screen.blit(bg, (0,0))
    screen.blit(new_min_hand, min_hand_rect)
    screen.blit(new_sec_hand,sec_hand_rect)

    pygame.display.flip()

pygame.quit()