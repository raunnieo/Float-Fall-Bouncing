# Importing modules
import pygame
from sys import exit 
import random

# Initialize the clock for controlling the frame rate
clock = pygame.time.Clock()

# List of loader values
loader = [1, 9, 27, 5, 0] # Bar speed controller

def load_screen(screen, scaling):
    """
    Displays a series of loading screens before the game starts.

    Args:
        screen (pygame.Surface): The screen to display the loading screens on.
        scaling (int): The scaling factor for adjusting image sizes.

    Returns:
        bool: True if the loading screens should continue, False if they should stop.
    """
    # Load the background image for the loading screen
    load_bg = pygame.image.load(f"graphics/{scaling}/load/loadBG_{screen.screen_mode}.png").convert()

    # Fill the screen with black for 1 sec
    screen.screen.fill("Black")
    clock.tick(1)

    # Blit the loading screen background onto the screen
    screen.screen.blit(load_bg, (0,0))
    pygame.display.update()
    clock.tick(5)

    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                # Switch screen mode (fullscreen or windowed) when "f" key is pressed
                if screen.screen_mode == 1:
                    screen.screen_mode = 2
                else:
                    screen.screen_mode = 1
                screen.display_init()
                load_bg = pygame.image.load(f"graphics/{scaling}/load/loadBG_{screen.screen_mode}.png").convert()
    return False

# Global variable for tracking the position of the loading bar
x = 0

def loading(screen, scaling):
    """
    Displays a loading animation on the screen.

    Args:
        screen (pygame.Surface): The screen to display the loading animation on.
        scaling (int): The scaling factor for adjusting image sizes.

    Returns:
        bool: True if the loading animation should continue, False if it should stop.
    """
    global x
    global loader

    # Load the images for the loading animation
    load_bg = pygame.image.load(f"graphics/{scaling}/load/loadBG_{screen.screen_mode}.png").convert()
    loadbar = pygame.image.load(f"graphics/{scaling}/load/loadbar_{screen.screen_mode}.png").convert_alpha()
    barRect = loadbar.get_rect(topright=(x, 0))
    loadScreen = pygame.image.load(f"graphics/{scaling}/load/load_{screen.screen_mode}.png").convert_alpha()

    # Update the loader value based on the position of the loading bar
    if barRect.right > 1133:
        loader[4] = loader[3]
    elif barRect.right > 378:
        loader[4] = loader[2]
    elif barRect.right > 315:
        loader[4] = loader[1]
    elif barRect.right > 126:
        loader[4] = loader[0]
    else:
        loader[4] = 100

    # Move the loading bar to the right
    if barRect.right <= screen.screen.get_width():
        barRect.right += loader[4]
        x = barRect.right
    else:
        return False

    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                # Switch screen mode (fullscreen or windowed) when "f" key is pressed
                # All the assets are reloaded if the screen switches mode
                if screen.screen_mode == 1:
                    screen.screen_mode = 2
                else:
                    screen.screen_mode = 1
                screen.display_init()
                loadbar = pygame.image.load(f"graphics/{scaling}/load/loadbar_{screen.screen_mode}.png").convert_alpha()
                loadScreen = pygame.image.load(f"graphics/{scaling}/load/load_{screen.screen_mode}.png").convert_alpha()
                load_bg = pygame.image.load(f"graphics/{scaling}/load/loadBG_{screen.screen_mode}.png").convert()
                screen.screen.blit(load_bg, (0, 0))

    # Blit the loading bar and screen onto the screen
    screen.screen.blit(loadbar, barRect.topleft)
    screen.screen.blit(loadScreen, (0, 0))
    pygame.display.update()
    clock.tick(100)
    return True
