# Importing modules
import pygame
from sys import exit 
from math import sqrt

clock = pygame.time.Clock()
def show_vectors(screen, body):
    font = pygame.font.Font("graphics/font/AGENCYB.TTF", 50)
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

    net_surface = font.render(f'{round(sqrt((body.v_x**2)+(body.v_y**2)))}', False, 'White')
    net_rect = net_surface.get_rect(center = body.ball_rect.center)

    screen.screen.blit(net_surface, (net_rect.topright[0] + 50, net_rect.topright[1]))
    pygame.draw.line(screen.screen, 'White', (body.ball_rect.center), (body.ball_rect.center[0] - 2*body.v_x,body.ball_rect.center[1] - 2*body.v_y*-1), 3)
