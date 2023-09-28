import pygame
from pygame.sprite import Sprite

class Raindrop(Sprite):
    
    def __init__(self, rain_game):
        super().__init__()
        self.screen = rain_game.screen
        self.settings = rain_game.settings

        self.image = pygame.image.load('images/raindrop.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
    
    def update(self):
        self.y += self.settings.raindrop_drop_speed
        self.rect.y = self.y

    def check_disappeared(self):
        screen_rect = self.screen.get_rect()
        return self.rect.top >= screen_rect.bottom