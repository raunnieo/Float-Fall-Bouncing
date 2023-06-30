import pygame
from sys import exit
pygame.init()
clock = pygame.time.Clock()

screen_mode = 2
scale = int((1920/pygame.display.get_desktop_sizes()[0][0])*100)
#true for normal

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
screen = display_init(screen_mode)
ground = pygame.image.load(f"graphics/{scale}/ground/ground_{screen_mode}.png")
while True:
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
                ground = pygame.image.load(f"graphics/{scale}/ground/ground_{screen_mode}.png")
                print(screen.get_size(), screen_mode)
    screen.blit(ground, (0,0))
    pygame.display.update()
    clock.tick(50)
