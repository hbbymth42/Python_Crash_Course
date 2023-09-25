import sys

import pygame

from game_character import Crusader

class BlueSky:

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Blue Sky")

        self.crusader = Crusader(self)

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill((0, 225, 255))
            self.crusader.blitme()
            
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == '__main__':
    bs = BlueSky()
    bs.run_game()