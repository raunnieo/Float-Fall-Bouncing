import pygame
import buttons
from sys import exit

def exit_screen(screen):
    """
    Displays the exit screen and handles user interaction.

    Args:
        screen (Window): The Window object representing the game screen.

    Returns:
        bool: True if the user selects to exit, False if the user cancels the exit.
    """
    # Initialize clock to control frame rate
    clock = pygame.time.Clock()

    # Calculate scaling factor based on desktop size
    scaling = int((1920 / pygame.display.get_desktop_sizes()[0][0]) * 100)

    # Get the size of the screen
    size = screen.screen.get_size()

    # Calculate scaling factor for adjusting positions and sizes
    scale_2 = size[0] / 1920
    
    # Load exit screen images
    exit_screen = pygame.image.load(f"graphics/{scaling}/exit/exit_display_{screen.screen_mode}.png").convert_alpha()
    cross = pygame.image.load(f"graphics/{scaling}/exit/cross_{screen.screen_mode}.png").convert_alpha()
    yes = pygame.image.load(f"graphics/{scaling}/exit/yes_{screen.screen_mode}.png").convert_alpha()
    
    # Create buttons
    cross_button = buttons.Button(1208 * scale_2, 235 * scale_2, cross, 0)
    yes_button = buttons.Button(847 * scale_2, 742 * scale_2, yes, 0)
    
    # Blit exit screen image to the screen
    screen.screen.blit(exit_screen, (632 * scale_2, 222 * scale_2))
    
    # Main loop for handling user interaction
    while True:
        # Check if the "Yes" button is clicked
        if yes_button.draw(screen.screen):
            return False
        
        # Check if the "Cross" button is clicked
        if cross_button.draw(screen.screen):
            return True
        
        # Handle events
        for event in pygame.event.get():
            # If the user closes the window, quit the game
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        
        # Update the display
        pygame.display.update()
        
        # Control the frame rate
        clock.tick(30)
