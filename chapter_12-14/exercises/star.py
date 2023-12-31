import pygame
from pygame.sprite import Sprite

class Star(Sprite):

    def __init__(self, s_game):
        super().__init__()
        self.screen = s_game.screen

        self.image = pygame.image.load('images/star.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)