import pygame.font

class Button:
    """A class to build buttons for the game."""

    def __init__(self, ss_game, msg):
        """Initialise button attributes."""
        self.screen = ss_game.screen
        self.screen_rect = self.screen.get_rect()

        # Set the dimensions and properties of the button.
        self.width, self.height = 200, 50
        self.button_colour = (0, 150, 0)
        self.text_colour = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Build the button's rect object and center it
        self.rect = pygame.Rect(0, 0, self.width, self.height)

        # Render difficulty and play buttons
        if msg == 'Play':
            self.button_colour = (0, 150, 0)
            self.rect.center = self.screen_rect.center
        elif msg == 'Easy':
            self.button_colour = (0, 0, 150)
            self.rect.bottomleft = self.screen_rect.bottomleft
        elif msg == 'Normal':
            self.button_colour = (150, 150, 0)
            self.rect.midbottom = self.screen_rect.midbottom
        elif msg == 'Hard':
            self.button_colour = (150, 0, 0)
            self.rect.bottomright = self.screen_rect.bottomright
        
        self._prep_msg(msg)
    
    def _prep_msg(self, msg):
        """Turn msg into a rendered image and center text on the button."""
        self.msg_image = self.font.render(msg, True, self.text_colour,
                                          self.button_colour)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
    
    def draw_button(self):
        """Draw blank button then draw message."""
        self.screen.fill(self.button_colour, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)