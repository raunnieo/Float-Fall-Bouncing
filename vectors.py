import pygame
from sys import exit 
from math import sqrt

pygame.init()

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


clock = pygame.time.Clock()
screen_mode = 1
screen = display_init(screen_mode)
text_font = pygame.font.Font(None ,50)

net_color = "White"

def show_vectors(screen, body):
    """
    Displays the velocity vector of a body on the screen.

    Args:
        screen (pygame.Surface): The screen to display the vector on.
        body (Ball): The body for which to display the vector.
    """
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

    net_surface = text_font.render(f'{round(sqrt((body.v_x**2)+(body.v_y**2)))}', False, 'White')
    net_rect = net_surface.get_rect(center = body.ball_rect.center)

    screen.blit(net_surface, (net_rect.topright[0] + 50, net_rect.topright[1]))
    pygame.draw.line(screen, net_color, (body.ball_rect.center), (body.ball_rect.center[0] - 2*body.v_x,body.ball_rect.center[1] - 2*body.v_y*-1), 3)
