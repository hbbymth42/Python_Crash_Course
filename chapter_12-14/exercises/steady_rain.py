import sys

import pygame
from settings import Settings
from raindrop import Raindrop

class Raindrops:

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width,
                                               self.settings.screen_height))
        pygame.display.set_caption("Raindrops")

        self.raindrops = pygame.sprite.Group()

        self._create_raindrops()
    
    def run(self):
        while True:
            self._check_exit()
            self._update_raindrops()
            self._update_screen()
            self.clock.tick(60)
    
    def _check_exit(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
    
    def _update_raindrops(self):
        self.raindrops.update()

        make_new_raindrops = False
        for raindrop in self.raindrops.copy():
            if raindrop.check_disappeared():
                self.raindrops.remove(raindrop)
                make_new_raindrops = True

        if make_new_raindrops:
            self._create_new_row()

    def _create_raindrops(self):
        raindrop = Raindrop(self)
        raindrop_width, raindrop_height = raindrop.rect.size

        current_x, current_y = raindrop_width, raindrop_height
        while current_y < (self.settings.screen_height - 1 * raindrop_height):
            while current_x < (self.settings.screen_width - 1 * raindrop_width):
                self._create_raindrop(current_x, current_y)
                current_x += 1 * raindrop_width
            
            current_x = raindrop_width
            current_y += 1 * raindrop_height
    
    def _create_raindrop(self, x_position, y_position):
        new_raindrop  = Raindrop(self)
        new_raindrop.y = y_position
        new_raindrop.rect.x = x_position
        new_raindrop.rect.y = y_position
        self.raindrops.add(new_raindrop)
    
    def _create_new_row(self):
        raindrop = Raindrop(self)
        raindrop_width, raindrop_height = raindrop.rect.size

        current_x = raindrop_width
        current_y = -1 * raindrop_height
        while current_x < (self.settings.screen_width - 1 * raindrop_width):
            self._create_raindrop(current_x, current_y)
            current_x += 1 * raindrop_width
    
    def _update_screen(self):
        self.screen.fill(self.settings.bg_colour)
        self.raindrops.draw(self.screen)

        pygame.display.flip()
    
if __name__ == '__main__':
    rain_game = Raindrops()
    rain_game.run()