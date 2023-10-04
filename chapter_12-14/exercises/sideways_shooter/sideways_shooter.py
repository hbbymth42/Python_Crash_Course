import sys
from time import sleep

import pygame

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from bullet import Bullet
from alien import Alien

class SidewaysShooter:
    """Overall class to manage game assets and behaviour."""

    def __init__(self):
        """Initialise the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width,
                                               self.settings.screen_height))
        pygame.display.set_caption("Sideways Shooter")

        # Create an instance to store game statistics, and create a scoreboard.
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        # Create ship.
        self.ship = Ship(self)

        # Create bullet and alien groups.
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        # Start Sideways Shooter in an inactive state.
        self.game_active = False

        # Make the play button.
        self.play_button = Button(self, "Play")

        # Make difficulty buttons.
        self.easy_button = Button(self, "Easy")
        self.normal_button = Button(self, "Normal")
        self.hard_button = Button(self, "Hard")

        # Make Sound Effects for firing bullets, and ship and alien explosions.
        pygame.mixer.init()
        self.ship_laser_sfx = pygame.mixer.Sound('sfx/laser_sound.wav')
        self.alien_explosion_sfx = pygame.mixer.Sound('sfx/alien_explosion.wav')
        self.ship_explosion_sfx = pygame.mixer.Sound('sfx/ship_explosion.wav')

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()

            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()
            self.clock.tick(60)
    
    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_difficulty(mouse_pos)
                self._check_play_button(mouse_pos)
    
    def _check_keydown_events(self, event):
        """Respond to key presses."""
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_p and not self.game_active:
            self._start_game()
    
    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False
    
    def _check_difficulty(self, mouse_pos):
        """Scale difficulty depending on which difficulty button user clicks."""
        if self.hard_button.rect.collidepoint(mouse_pos):
            self.settings.initialise_dynamic_settings(2)
        elif self.normal_button.rect.collidepoint(mouse_pos):
            self.settings.initialise_dynamic_settings(1)
        elif self.easy_button.rect.collidepoint(mouse_pos):
            self.settings.initialise_dynamic_settings(0.75)
        
    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks Play."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)

        if button_clicked and not self.game_active:
            self._start_game()
    
    def _start_game(self):
        """Method to prepare a new game"""
        self.stats.reset_stats()
        self.sb.prep_images()
        self.game_active = True

        # Get rid of any remaining bullets and aliens.
        self.bullets.empty()
        self.aliens.empty()

        # Create a new fleet and center the ship
        self._create_fleet()
        self.ship.center_ship()

        # Hide the moue cursor.
        pygame.mouse.set_visible(False)
    
    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            pygame.mixer.Sound.play(self.ship_laser_sfx)
            self.bullets.add(new_bullet)
    
    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # Update bullet positions
        self.bullets.update()

        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.left >= self.settings.screen_width:
                self.bullets.remove(bullet)
        
        self._check_bullet_alien_collisions()
    
    def _check_bullet_alien_collisions(self):
        """Respond to bullet-alien collisions."""
        # Remove any bullets and aliens that have collided.
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens,
                                                True, True)
        
        if collisions:
            pygame.mixer.Sound.play(self.alien_explosion_sfx)
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()
        
        if not self.aliens:
            self._start_new_level()
    
    def _start_new_level(self):
        """Method to start new level when all aliens have been hit."""
        # Destroy existing bullets and create new fleet.
        self.bullets.empty()
        self._create_fleet()
        self.settings.increase_speed()

        # Increase level.
        self.stats.level += 1
        self.sb.prep_level()

    def _ship_hit(self):
        """Respond to the ship being hit by an alien"""
        if self.stats.ships_left > 0:
            # Decrement ships left
            self.stats.ships_left -= 1
            pygame.mixer.Sound.play(self.ship_explosion_sfx)
            self.sb.prep_ships()

            # Get rid of any remaining bullets and aliens.
            self.bullets.empty()
            self.aliens.empty()

            # Create a new fleet and center the ship.
            self._create_fleet()
            self.ship.center_ship()

            # Pause
            sleep(0.5)
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)

    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    
    def _change_fleet_direction(self):
        """Move the entire fleet and change the fleet's direction."""
        for alien in self.aliens.sprites():
            alien.rect.x -= self.settings.fleet_flight_speed
        self.settings.fleet_direction *= -1
    
    def _check_aliens_left(self):
        """Check if any aliens have reached the left of the screen."""
        for alien in self.aliens.sprites():
            if alien.rect.left <= 0:
                # Treat this the same as if the ship got hit.
                self._ship_hit()
                break
    
    def _update_aliens(self):
        """Check if the fleet is at an edge, then update positions."""
        self._check_fleet_edges()
        self.aliens.update()

        # Look for alien-ship collisions.
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        
        # Look for aliens hitting the left of the screen.
        self._check_aliens_left()
    
    def _create_fleet(self):
        """Create the fleet of aliens."""
        # Create an alien and keep adding aliens until there's no room left.
        # Spacing between aliens is one alien width and one alien height
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        current_x, current_y = 8 * alien_width, alien_height
        while current_x < (self.settings.screen_width - alien_width):
            while current_y < (self.settings.screen_height -  3 * alien_height):
                self._create_alien(current_x, current_y)
                current_y += alien_height
            
            # Finished a column, reset y value, and increment x value.
            current_y = alien_height
            current_x += 2 * alien_width
        
    def _create_alien(self, x_position, y_position):
        """Create an alien and place it in the fleet."""
        new_alien = Alien(self)
        new_alien.y = y_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    
    def _update_screen(self):
        """Update images on the screen. and flip to the new screen"""
        self.screen.fill(self.settings.bg_colour)

        # Draw bullets where they have been fired
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # Draw the ship
        self.ship.blitme()

        # Draw the alien fleet
        self.aliens.draw(self.screen)

        # Draw the score information
        self.sb.show_score()

        # Draw the difficulty and play buttons if the game is inactive.
        if not self.game_active:
            self.play_button.draw_button()
            self.easy_button.draw_button()
            self.normal_button.draw_button()
            self.hard_button.draw_button()

        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ss = SidewaysShooter()
    ss.run_game()