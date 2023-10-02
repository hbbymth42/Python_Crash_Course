import sys
from time import sleep

import pygame

from settings import Settings
from game_stats import GameStats
from button import Button
from ship import Ship
from bullet import Bullet
from rectangle import Rectangle

class TargetPractice:

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width,
                                               self.settings.screen_height))
        
        pygame.display.set_caption("Target Practice")

        self.stats = GameStats(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.rectangle = Rectangle(self)

        self.num_bullets_missed = 0

        self.game_active = False

        self.play_button = Button(self, "Play")

    def run_game(self):
        while True:
            self._check_events()

            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_rectangle()
            
            self._update_screen()
            self.clock.tick(60)
    
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
    
    def _start_game(self):
        self.settings.initialise_dynamic_settings()
        self.stats.reset_stats()
        self.game_active = True

        self.bullets.empty()

        self.ship.center_ship()
        self.rectangle.center_rectangle()

        pygame.mouse.set_visible(False)
    
    def _check_play_button(self, mouse_pos):
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            self._start_game()
    
    def _check_keydown_events(self, event):
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False
        
    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.left >= self.settings.screen_width:
                self._bullet_missed()
                self.bullets.remove(bullet)
        
        if pygame.sprite.spritecollide(self.rectangle, self.bullets, True):
            self.settings.increase_speed()
    
    def _bullet_missed(self):
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1
        else:
            self.game_active = False
            self.bullets.empty()
            self.ship.center_ship()
            self.rectangle.center_rectangle()
            pygame.mouse.set_visible(True)
    
    def _check_rectangle_edges(self):
        if self.rectangle.check_edges():
            self._change_rectangle_direction()
    
    def _change_rectangle_direction(self):
        self.settings.rect_direction *= -1
    
    def _update_rectangle(self):
        self._check_rectangle_edges()
        self.rectangle.update()

    def _update_screen(self):
        self.screen.fill(self.settings.bg_colour)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.rectangle.draw_rectangle()

        if not self.game_active:
            self.play_button.draw_button()

        pygame.display.flip()

if __name__ == '__main__':
    tp = TargetPractice()
    tp.run_game()
    