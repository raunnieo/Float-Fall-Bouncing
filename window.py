import pygame

class Window:
    def __init__(self, screen_mode):
        self.screen_mode = screen_mode
        self.screen = None
    def display_init(self):
        size = pygame.display.get_desktop_sizes()[0]
        if self.screen_mode == 2:
            window_height = size[1]*0.89
            window_width = window_height * 1.77
            size  = (window_width, window_height)
            self.screen = pygame.display.set_mode((window_width, window_height))
        else:
            self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)