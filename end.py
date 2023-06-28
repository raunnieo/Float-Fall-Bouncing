import pygame
import buttons
from sys import exit
def exit_screen(screen):
    clock = pygame.time.Clock()
    scaling = int((1920/pygame.display.get_desktop_sizes()[0][0])*100)
    size = screen.screen.get_size()
    scale_2 = size[0]/1920
    exit_screen = pygame.image.load(f"graphics/{scaling}/exit/exit_display_{screen.screen_mode}.png").convert_alpha()
    cross = pygame.image.load(f"graphics/{scaling}/exit/cross_{screen.screen_mode}.png").convert_alpha()
    yes = pygame.image.load(f"graphics/{scaling}/exit/yes_{screen.screen_mode}.png").convert_alpha()
    cross_button = buttons.Button(1208*scale_2, 235*scale_2, cross, 0)
    yes_button = buttons.Button(847*scale_2, 742*scale_2 , yes, 0)
    screen.screen.blit(exit_screen, (632*scale_2, 222*scale_2))
    while True:
        if yes_button.draw(screen.screen):
            return False
        if cross_button.draw(screen.screen):
            return True
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
        pygame.display.update()
        clock.tick(30)
