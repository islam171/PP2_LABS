import pygame

pygame.init()
screen = pygame.display.set_mode((300, 300))
clock = pygame.time.Clock()

surface = pygame.Surface((100, 100), pygame.SRCALPHA)
x, y = 150, 150
radius = 25

running = True
while running:

    pressed = pygame.key.get_pressed()
   

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           running = False     

        if pressed[pygame.K_DOWN]: y +=20
        if pressed[pygame.K_UP]: y -= 20
        if pressed[pygame.K_LEFT]: x -= 20
        if pressed[pygame.K_RIGHT]: x +=20

    if(x >= screen.get_size()[0] - radius): x = screen.get_size()[0] - radius
    if(x <= radius): x = radius
    if(y >= screen.get_size()[1] - radius): y = screen.get_size()[0] - radius
    if(y <= radius): y = radius

    screen.fill("white")
    pygame.draw.circle(screen, "red", (x, y), radius)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()