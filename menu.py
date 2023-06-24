import pygame
from sys import exit

pygame.init()

clock = pygame.time.Clock()

window_height = 793
window_width = 1410
screen = pygame.display.set_mode((window_width, window_height), pygame.RESIZABLE)
menu_surface = pygame.image.load('graphics\menu\menu.png').convert()

esc = False

def menu(screen):
    output = {"Ball":1}
    flag = True
    while flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    output["Ball"] = 1
                elif event.key == pygame.K_2:
                    output["Ball"] = 2
                elif event.key == pygame.K_3:
                    output["Ball"] = 3
                elif event.key == pygame.K_4:
                    output["Ball"] = 4
                if event.key == pygame.K_ESCAPE:
                    flag = False
                    break
                    
                    
        screen.blit(menu_surface, (0,0))
        pygame.display.update()
    return output
