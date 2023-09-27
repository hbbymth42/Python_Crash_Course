import sys

import pygame

from random import randint

from star import Star

class Stars:

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((1200, 800))

        pygame.display.set_caption("Stars")

        self.stars = pygame.sprite.Group()

        self._create_stars()
    
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self._update_screen()
            self.clock.tick(60)
    
    def _create_stars(self):
        star = Star(self)
        star_width, star_height = star.rect.size

        current_x, current_y = star_width, star_height
        while current_y < (800):
            while current_x < (1200):
                self._create_star(current_x, current_y)
                current_x += star_width

            current_x = star_width
            current_y += star_height
    
    def _create_star(self, x_position, y_position):
        random_number = randint(-90, 90)
        new_star = Star(self)
        new_star.x = x_position 
        new_star.rect.x = x_position + random_number
        random_number = randint(-60, 60)
        new_star.rect.y = y_position + random_number
        self.stars.add(new_star)
    
    def _update_screen(self):
        self.screen.fill((0, 0, 0))
        self.stars.draw(self.screen)

        pygame.display.flip()
    
if __name__ == '__main__':
    s_game = Stars()
    s_game.run()