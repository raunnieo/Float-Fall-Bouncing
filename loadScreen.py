import pygame
from sys import exit 
import random

pygame.init()

clock = pygame.time.Clock()

window_height = 650
window_width = 1259
screen = pygame.display.set_mode((window_width,window_height), pygame.RESIZABLE)

resize = [False, 0, 0]

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
        
    if resize[0] == True:
            surface= pygame.transform.scale_by(surface, resize[1]/resize[2])
    screen.blit(surface, (0,0))
    
    clock.tick(5)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.VIDEORESIZE:
            resize[1]=event.h
            resize[2]=window_height
            window_height = event.h
            window_width = event.w
            resize[0] = not resize[0]

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_k:
                return False
    return True

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
    bar = pygame.image.load('graphics/Scenes/lobar.png').convert_alpha()
    surface  = pygame.image.load('graphics/Scenes/lo1.png').convert()
    surface2  = pygame.image.load('graphics/Scenes/lo2.png').convert_alpha()
    if resize[0] == True:
        surface  = pygame.transform.scale_by(surface, resize[1]/resize[2])
        surface2 = pygame.transform.scale_by(surface2, resize[1]/resize[2])
        bar = pygame.transform.scale_by(bar, resize[1]/resize[2])

    if barRect.right <= 1259:
        barRect.right += random.randint(0,10)
    else:
        return False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.VIDEORESIZE:
            resize[1]=event.h
            resize[2]=window_height
            window_height = event.h
            window_width = event.w
            resize[0] = not resize[0]

            # screen = pygame.display.set_mode((window_width, window_height), pygame.RESIZABLE)
    screen.blit(surface, (0,0))
    screen.blit(bar, barRect.topleft)
    screen.blit(surface2, (0,0))
    pygame.display.update()
    clock.tick(20)
    return True