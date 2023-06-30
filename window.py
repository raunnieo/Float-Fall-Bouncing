#Importing modules
import pygame

class Window:
    def __init__(self, screen_mode):
        """
        Initializes a Window object with the specified screen mode.

        Args:
            screen_mode (int): The screen mode for the window.
                               2 - Windowed mode
                               Other values - Fullscreen mode
        """
        self.screen_mode = screen_mode
        self.screen = None
    
    def display_init(self):
        """
        Initializes the display based on the specified screen mode.
        """
        # Get the size of the desktop
        size = pygame.display.get_desktop_sizes()[0]
        
        if self.screen_mode == 2:
            # Calculate the window size for windowed mode
            window_width = size[0] * 0.9
            window_height = window_width * 0.5625
            size = (window_width, window_height)
            
            # Set the display mode to the calculated window size
            self.screen = pygame.display.set_mode((window_width, window_height))
        else:
            # Set the display mode to fullscreen
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
