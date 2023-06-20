import pygame
from sys import exit 
import random

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((1000,650))

def load_screen(screen):
    """
    Displays a series of loading screens before the game starts.

    Args:
        screen (pygame.Surface): The screen to display the loading screens on.

    Returns:
        bool: True if the loading screens should continue, False if they should stop.
    """
    for i in range(1, 7):
        surface  = pygame.image.load(f'graphics/Scenes/op{i}.png').convert()
        screen.blit(surface, (0,0))
        t = 5
        if i == 5:
            t = 1
        
        clock.tick(t)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_k:
                    return False
    return True

bar = pygame.image.load('graphics/Scenes/lobar.png').convert_alpha()
barRect = bar.get_rect(topright = (200,0))

def loading(screen):
    """
    Displays a loading animation on the screen.

    Args:
        screen (pygame.Surface): The screen to display the loading animation on.

    Returns:
        bool: True if the loading animation should continue, False if it should stop.
    """
    surface  = pygame.image.load('graphics/Scenes/lo1.png').convert()
    surface2  = pygame.image.load('graphics/Scenes/lo2.png').convert_alpha()

    screen.blit(bar, barRect.topleft)
    screen.blit(surface2, (0,0))

    if barRect.right <= 1000:
        barRect.right += random.randint(0, 30)
    else:
        return False
    
    clock.tick(5)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.update()
    return True