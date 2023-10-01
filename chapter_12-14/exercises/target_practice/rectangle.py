import pygame
from pygame.sprite import Sprite

class Rectangle(Sprite):

    def __init__(self, tp_game):
        super().__init__()
        self.screen = tp_game.screen
        self.settings = tp_game.settings
        self.screen_rect = tp_game.screen.get_rect()
        self.colour = self.settings.rect_colour

        self.width, self.height = 10, 20

        self.rect = pygame.Rect(0, 0, self.width, self.height)

        self.rect.midright = self.screen_rect.midright

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
    
    def check_edges(self):
        screen_rect = self.screen.get_rect()
        return (self.rect.bottom >= screen_rect.bottom) or (self.rect.top <= 0)
    
    def update(self):
        self.y += self.settings.rect_speed * self.settings.rect_direction
        self.rect.y = self.y
    
    def center_rectangle(self):
        self.rect.midright = self.screen_rect.midright
        self.y = float(self.rect.y)
    
    def draw_rectangle(self):
        pygame.draw.rect(self.screen, self.colour, self.rect)