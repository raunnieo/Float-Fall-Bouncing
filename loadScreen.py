import pygame
from sys import exit 
import random

pygame.init()

clock = pygame.time.Clock()

window_height = 650
window_width = 1259
screen = pygame.display.set_mode((window_width,window_height), pygame.FULLSCREEN)
screen.fill("Black")
clock.tick(1)
loader = [1, 9, 27, 5, 0]

def load_screen(screen):
    """
    Displays a series of loading screens before the game starts.

    Args:
        screen (pygame.Surface): The screen to display the loading screens on.

    Returns:
        bool: True if the loading screens should continue, False if they should stop.
    """
    global window_height
    global window_width
    global resize
    surface  = pygame.image.load('graphics/Scenes/lo1.png').convert()
    screen.blit(surface, (0,0))
    
    clock.tick(5)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    return False

bar = pygame.image.load('graphics/Scenes/lobar.png').convert_alpha()
barRect = bar.get_rect(topright = (0,0))
def loading(screen):
    """
    Displays a loading animation on the screen.

    Args:
        screen (pygame.Surface): The screen to display the loading animation on.

    Returns:
        bool: True if the loading animation should continue, False if it should stop.
    """
    global window_height
    global loader
    bar = pygame.image.load('graphics/Scenes/lobar.png').convert_alpha()
    surface  = pygame.image.load('graphics/Scenes/lo1.png').convert()
    surface2  = pygame.image.load('graphics/Scenes/lo2.png').convert_alpha()


    if barRect.right>1133:
        loader[4]=loader[3]
    elif barRect.right>378:
        loader[4]=loader[2]
    elif barRect.right>315:
        loader[4]=loader[1]
    elif barRect.right>126:
        loader[4]=loader[0]
    else:
        loader[4] = 200

    if barRect.right<=1259:
        barRect.right += 0.5*loader[4]
    else:
        return False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(surface, (0,0))
    screen.blit(bar, barRect.topleft)
    screen.blit(surface2, (0,0))
    pygame.display.update()
    clock.tick(20)
    return True