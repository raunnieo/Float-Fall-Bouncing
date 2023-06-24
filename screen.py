import pygame
from sys import exit
pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((800, 800), pygame.RESIZABLE)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.VIDEORESIZE:
            screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
    print(screen.get_size())
    pygame.display.update()
    clock.tick(50)