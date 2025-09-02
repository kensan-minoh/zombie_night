import pygame
import random
from pygame.math import Vector2

class Game:
    def __init__(self):
        self.music = pygame.mixer.music.load('sounds/game_sound.wav')
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(-1)

        tile_map = [
            
        ]





# initialize pygame
pygame.init()

# set display surface
WINDOW_WIDTH = 1526
WINDOW_HEIGHT = 1024
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Zombie Night')

# background
background_image = pygame.image.load('images/background.png')



# set clock and FPS
clock = pygame.time.Clock()
FPS =60

my_game = Game()
# main game loop
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    # fill the background
    display_surface.blit(background_image, (0, 0))


    # update the display
    pygame.display.update()


    # tick the clock
    clock.tick(FPS)

# end the game
pygame.quit()

    


