import pygame

_RED = (255, 0, 0)
_GREEN = (0, 255, 0)
_YELLOW = (255, 255, 0)
_BLUE = (0, 0, 255)

class Player:

    isPlay = False
    songs = ["Kay-Figo-Kanyelele", "Counting Stars"]
    current_music_index = 0

    def __init__(self):
        pygame.mixer.init()

    def run(self):
        self.play(self.songs[0])

    def play(self, music_name):
        self.isPlay = True
        pygame.mixer.music.load(f"./{music_name}.mp3")
        pygame.mixer.music.play()

    def getSongsLen(self):
        return len(self.songs) 

    def toggle(self):
        if(self.isPlay):
            self.isPlay = False
            pygame.mixer.music.pause()
        else:
            self.isPlay = True
            pygame.mixer.music.unpause()

    def next_song(self):
        if(self.current_music_index+1 < self.getSongsLen()):
            self.current_music_index += 1
            self.play(self.songs[self.current_music_index])

    def previous_song(self):
        if(self.current_music_index >= 1):
            self.current_music_index -= 1
            self.play(self.songs[self.current_music_index])
        
        
pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
player = Player()
player.run()



class Button:
    def __init__(self, screen,color, x, y, width, height):
        self.color = color
        self.screen = screen
        self.width = width
        self.height = height
        self.rect = pygame.Rect(x+self.screen.get_size()[0]/2-width/2, y+self.screen.get_size()[1]/2-height/2, width, height)
        

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect, 0)

    def click(self, event):
        return event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos)


running = True
while running:

    pressed = pygame.key.get_pressed()
    PlayButton = Button(screen, _GREEN, 0, 0, 50, 50)
    prevButton = Button(screen, _RED, -70, 0, 50, 50)
    nextButton = Button(screen, _BLUE, 70, 0, 50, 50)
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           running = False     

        if pressed[pygame.K_SPACE] or PlayButton.click(event): player.toggle()
        if pressed[pygame.K_LEFT] or prevButton.click(event): player.previous_song()
        if pressed[pygame.K_RIGHT] or nextButton.click(event): player.next_song()


    screen.fill(_YELLOW)

    for i in (PlayButton, prevButton, nextButton):
        i.draw()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()