# Importing modules
import pygame
import buttons
from sys import exit

# Screen Setup
menu_tab = 3  # Setting default tab
output = {"IMode": False, "Ball": 1, "Scene": 0}

def menu(screen, scaling):
    global menu_tab
    global output

    # Load menu surface
    menu_surface = pygame.image.load(f'graphics/{scaling}/menu/menu_{screen.screen_mode}.png').convert()

    # Set the initial menu tab
    menu_tab = 3

    # Load button images
    about = pygame.image.load(f"graphics/{scaling}/buttons/about_{screen.screen_mode}.png").convert_alpha()
    mode = pygame.image.load(f"graphics/{scaling}/buttons/mode_{screen.screen_mode}.png").convert_alpha()
    object = pygame.image.load(f"graphics/{scaling}/buttons/object_{screen.screen_mode}.png").convert_alpha()
    scene = pygame.image.load(f"graphics/{scaling}/buttons/scene_{screen.screen_mode}.png").convert_alpha()
    start = pygame.image.load(f"graphics/{scaling}/buttons/start_{screen.screen_mode}.png").convert_alpha()
    settings = pygame.image.load(f"graphics/{scaling}/buttons/settings_{screen.screen_mode}.png").convert_alpha()
    football = pygame.image.load(f"graphics/{scaling}/buttons/football_{screen.screen_mode}.png").convert_alpha()
    tennisball = pygame.image.load(f"graphics/{scaling}/buttons/tennisball_{screen.screen_mode}.png").convert_alpha()
    basketball = pygame.image.load(f"graphics/{scaling}/buttons/basketball_{screen.screen_mode}.png").convert_alpha()
    volleyball = pygame.image.load(f"graphics/{scaling}/buttons/volleyball_{screen.screen_mode}.png").convert_alpha()
    moon = pygame.image.load(f"graphics/{scaling}/buttons/moon_{screen.screen_mode}.png").convert_alpha()
    ground = pygame.image.load(f"graphics/{scaling}/buttons/ground_{screen.screen_mode}.png").convert_alpha()
    water = pygame.image.load(f"graphics/{scaling}/buttons/water_{screen.screen_mode}.png").convert_alpha()
    aboutmess = pygame.image.load(f"graphics/{scaling}/buttons/aboutmess_{screen.screen_mode}.png").convert_alpha()
    normal = pygame.image.load(f"graphics/{scaling}/buttons/normal_{screen.screen_mode}.png").convert_alpha()
    interactive = pygame.image.load(f"graphics/{scaling}/buttons/interactive_{screen.screen_mode}.png").convert_alpha()

    # Scale
    size = screen.screen.get_size()
    scale_1 = round(size[0] / 1920, 2)
    size = screen.screen.get_size()
    scale_2 = round(size[0] / 1920, 2)
    scale = scale_2

    # Create button objects
    about_button = buttons.Button(332 * scale, 808 * scale_2, about, 10)
    mode_button = buttons.Button(587 * scale, 808 * scale_2, mode, 10)
    object_button = buttons.Button(841 * scale, 808 * scale_2, object, 10)
    scene_button = buttons.Button(1096 * scale, 808 * scale_2, scene, 10)
    start_button = buttons.Button(1347 * scale, 808 * scale_2, start, 10)
    settings_button = buttons.Button(1789 * scale, 37 * scale_2, settings, 10)
    football_button = buttons.Button(242 * scale, 197 * scale_2, football, 10)
    tennisball_button = buttons.Button(605 * scale, 197 * scale_2, tennisball, 10)
    basketball_button = buttons.Button(968 * scale, 197 * scale_2, basketball, 10)
    volleyball_button = buttons.Button(1332 * scale, 197 * scale_2, volleyball, 10)
    moon_button = buttons.Button(58 * scale, 198 * scale_2, moon, 10)
    water_button = buttons.Button(675 * scale, 198 * scale_2, water, 10)
    ground_button = buttons.Button(1292 * scale, 198 * scale_2, ground, 10)
    aboutmess_button = buttons.Button(343 * scale, 129 * scale_2, aboutmess, 0)
    normal_button = buttons.Button(384 * scale, 198 * scale_2, normal, 10)
    interactive_button = buttons.Button(982 * scale, 198 * scale_2, interactive, 10)


    # Draw the buttons on the screen
    about_button.draw(screen.screen)
    mode_button.draw(screen.screen)
    object_button.draw(screen.screen)
    scene_button.draw(screen.screen)
    start_button.draw(screen.screen)
    settings_button.draw(screen.screen)

    # Create dictionaries to map buttons to their respective tabs
    menu_dict = {1: about_button, 2: mode_button, 3: object_button, 4: scene_button}
    object_dict = {1: football_button, 2: basketball_button, 3: volleyball_button, 4: tennisball_button}
    scene_dict = {0: ground_button, 1: water_button, 2: moon_button}
    mode_dict = {True: interactive_button, False: normal_button}

    flag = True
    while flag:
        def_buttons = [menu_dict[menu_tab], scene_dict[output["Scene"]], object_dict[output["Ball"]], mode_dict[output["IMode"]]]

        # Move the buttons up if they were already selected
        for i in def_buttons:
            if not i.clicked:
                i.always_up = True
                i.clicked = True
                i.rect.top -= 10

        screen.screen.blit(menu_surface, (0, 0))  # Draw the menu surface

        # Check if buttons are clicked and update the menu tab accordingly
        if about_button.draw(screen.screen):
            menu_dict[menu_tab].always_up = False
            menu_tab = 1
        if mode_button.draw(screen.screen):
            menu_dict[menu_tab].always_up = False
            menu_tab = 2
        if object_button.draw(screen.screen):
            menu_dict[menu_tab].always_up = False
            menu_tab = 3
        if scene_button.draw(screen.screen):
            menu_dict[menu_tab].always_up = False
            menu_tab = 4
        if start_button.draw(screen.screen):
            flag = False

        # Draw the specific elements based on the current menu tab
        if menu_tab == 1:
            aboutmess_button.draw(screen.screen)
            
        if menu_tab == 2:
            if normal_button.draw(screen.screen):
                mode_dict[output["IMode"]].always_up = False
                output["IMode"] = False
            if interactive_button.draw(screen.screen):
                mode_dict[output["IMode"]].always_up = False
                output["IMode"] = True

        if menu_tab == 3:
            if football_button.draw(screen.screen):
                object_dict[output["Ball"]].always_up = False
                output["Ball"] = 1
            if tennisball_button.draw(screen.screen):
                object_dict[output["Ball"]].always_up = False
                output["Ball"] = 4
            if basketball_button.draw(screen.screen):
                object_dict[output["Ball"]].always_up = False
                output["Ball"] = 2
            if volleyball_button.draw(screen.screen):
                object_dict[output["Ball"]].always_up = False
                output["Ball"] = 3

        if menu_tab == 4:
            if moon_button.draw(screen.screen):
                scene_dict[output["Scene"]].always_up = False
                output["Scene"] = 2
            if water_button.draw(screen.screen):
                scene_dict[output["Scene"]].always_up = False
                output["Scene"] = 1
            if ground_button.draw(screen.screen):
                scene_dict[output["Scene"]].always_up = False
                output["Scene"] = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:
                    # Switching screen modes on pressing 'f'
                    if screen.screen_mode == 1:
                        screen.screen_mode = 2
                    else:
                        screen.screen_mode = 1
                    screen.display_init()
                    flag = False
                    break
                if event.key == pygame.K_ESCAPE: # If escape is pressed the menu loops stops
                    flag = False
                    break

        pygame.display.update()

    # Returning output 
    return output
