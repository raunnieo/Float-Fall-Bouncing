import pygame
import buttons
from sys import exit

clock = pygame.time.Clock()
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
screen_mode = 1
scaling = int((1920/pygame.display.get_desktop_sizes()[0][0])*100)
screen = display_init(screen_mode)
menu_surface = pygame.image.load('graphics/menu/menu.png').convert()
menu_tab = 3
output = {"IMode":False, "Ball":1, "Scene":0}

def menu(screen):
    global scaling
    global screen_mode
    global menu_tab
    global output
    menu_tab = 3
    #image loading
    about = pygame.image.load(f"graphics/{scaling}/buttons/about_{screen_mode}.png").convert_alpha()
    mode = pygame.image.load(f"graphics/{scaling}/buttons/mode_{screen_mode}.png").convert_alpha()
    object = pygame.image.load(f"graphics/{scaling}/buttons/object_{screen_mode}.png").convert_alpha()
    scene = pygame.image.load(f"graphics/{scaling}/buttons/scene_{screen_mode}.png").convert_alpha()
    start = pygame.image.load(f"graphics/{scaling}/buttons/start_{screen_mode}.png").convert_alpha()
    settings = pygame.image.load(f"graphics/{scaling}/buttons/settings_{screen_mode}.png").convert_alpha()
    football = pygame.image.load(f"graphics/{scaling}/buttons/football_{screen_mode}.png").convert_alpha()
    tennisball = pygame.image.load(f"graphics/{scaling}/buttons/tennisball_{screen_mode}.png").convert_alpha()
    basketball = pygame.image.load(f"graphics/{scaling}/buttons/basketball_{screen_mode}.png").convert_alpha()
    volleyball = pygame.image.load(f"graphics/{scaling}/buttons/volleyball_{screen_mode}.png").convert_alpha()
    moon = pygame.image.load(f"graphics/{scaling}/buttons/moon_{screen_mode}.png").convert_alpha()
    ground = pygame.image.load(f"graphics/{scaling}/buttons/ground_{screen_mode}.png").convert_alpha()
    water = pygame.image.load(f"graphics/{scaling}/buttons/water_{screen_mode}.png").convert_alpha()

    #scale
    size = screen.get_size()
    scale_1 = round(size[0]/1920, 2)
    size = screen.get_size()
    scale_2 = round(size[0]/1920, 2)
    scale = scale_2
    #buttons

    about_button = buttons.Button(332*scale, 808*scale_2, about, 10)
    mode_button = buttons.Button(587*scale, 808*scale_2, mode, 10)
    object_button = buttons.Button(841*scale, 808*scale_2, object, 10)
    scene_button = buttons.Button(1096*scale, 808*scale_2, scene, 10)
    start_button = buttons.Button(1347*scale, 808*scale_2, start, 10)
    settings_button = buttons.Button(1789*scale, 37*scale_2, settings, 10)
    football_button = buttons.Button(242*scale, 197*scale_2, football, 10)
    tennisball_button = buttons.Button(605*scale, 197*scale_2, tennisball, 10)
    basketball_button = buttons.Button(968*scale, 197*scale_2, basketball, 10)
    volleyball_button = buttons.Button(1332*scale, 197*scale_2, volleyball, 10)
    moon_button = buttons.Button(58*scale, 198*scale_2, moon, 10)
    water_button = buttons.Button(675*scale, 198*scale_2, water, 10)
    ground_button = buttons.Button(1292*scale, 198*scale_2, ground, 10)
    flag = True
    about_button.draw(screen)
    mode_button.draw(screen)
    object_button.draw(screen)
    scene_button.draw(screen)
    start_button.draw(screen)
    settings_button.draw(screen)
    while flag:
        screen.blit(menu_surface, (0,0))
        if about_button.draw(screen):
            menu_tab = 1
        if mode_button.draw(screen):
            menu_tab = 2
        if object_button.draw(screen):
            menu_tab = 3
        if scene_button.draw(screen):
            menu_tab = 4
        if start_button.draw(screen):
            flag = False
        if menu_tab == 3:
            if football_button.draw(screen):
                output["Ball"] = 1
            if tennisball_button.draw(screen):
                output["Ball"] = 4
            if basketball_button.draw(screen):
                output["Ball"] = 2
            if volleyball_button.draw(screen):
                output["Ball"] = 3
        if menu_tab == 4:
            if moon_button.draw(screen):
                output["Scene"] = 2
            if water_button.draw(screen):
                output["Scene"] = 1
            if ground_button.draw(screen):
                output["Scene"] = 0
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
            
        pygame.display.update()
    return output
