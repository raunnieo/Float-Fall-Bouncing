import pygame
from sys import exit 
import random

def display_init(screen_mode):
    size = pygame.display.get_desktop_sizes()[0]
    if screen_mode == 2:
        window_height = size[1]*0.89
        window_width = window_height * 1.77
        size  = (window_width, window_height)
        screen = pygame.display.set_mode((window_width, window_height))
        return screen
    else:
        screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        return screen

pygame.init()

clock = pygame.time.Clock()

#Screen Setup
screen_mode = 2
scaling = int((1920/pygame.display.get_desktop_sizes()[0][0])*100)
screen = display_init(screen_mode)

loader = [1, 9, 27, 5, 0]

load_bg = pygame.image.load(f"graphics/{scaling}/load/loadBG_{screen_mode}.png").convert()

def load_screen(screen):
    global scaling
    global screen_mode
    global load_bg
    screen.fill("Black")
    clock.tick(1)
    """
    Displays a series of loading screens before the game starts.

    Args:
        screen (pygame.Surface): The screen to display the loading screens on.

    Returns:
        bool: True if the loading screens should continue, False if they should stop.
    """
    screen.blit(load_bg, (0,0))
    pygame.display.update()
    clock.tick(5)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                if screen_mode == 1:
                    screen_mode = 2
                else:
                    screen_mode = 1
                screen = display_init(screen_mode)
                load_bg = pygame.image.load(f"graphics/{scaling}/load/loadBG_{screen_mode}.png").convert()
    return False

loadbar = pygame.image.load(f"graphics/{scaling}/load/loadbar_{screen_mode}.png").convert_alpha()
barRect = loadbar.get_rect(topright = (0,0))
loadScreen = pygame.image.load(f"graphics/{scaling}/load/load_{screen_mode}.png").convert_alpha()
def loading(screen):
    """
    Displays a loading animation on the screen.

    Args:
        screen (pygame.Surface): The screen to display the loading animation on.

    Returns:
        bool: True if the loading animation should continue, False if it should stop.
    """
    global loader
    global loadbar
    global loadScreen
    global load_bg
    global scaling
    global screen_mode

    if barRect.right>1133:
        loader[4]=loader[3]
    elif barRect.right>378:
        loader[4]=loader[2]
    elif barRect.right>315:
        loader[4]=loader[1]
    elif barRect.right>126:
        loader[4]=loader[0]
    else:
        loader[4] = 100

    if barRect.right<=screen.get_width():
        barRect.right += loader[4]*0.5
    else:
        return False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                if screen_mode == 1:
                    screen_mode = 2
                else:
                    screen_mode = 1
                screen = display_init(screen_mode)
                loadbar = pygame.image.load(f"graphics/{scaling}/load/loadbar_{screen_mode}.png").convert_alpha()
                loadScreen = pygame.image.load(f"graphics/{scaling}/load/load_{screen_mode}.png").convert_alpha()
                load_bg = pygame.image.load(f"graphics/{scaling}/load/loadBG_{screen_mode}.png").convert()
                screen.blit(load_bg, (0,0))

    # screen.blit(surface, (0,0))
    screen.blit(loadbar, barRect.topleft)
    screen.blit(loadScreen, (0,0))
    pygame.display.update()
    clock.tick(30)
    return True