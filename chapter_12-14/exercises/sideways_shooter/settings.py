class Settings:
    """A class to store all settings for Sideways Shooter."""

    def __init__(self):
        """Initialise the game's static settings."""
        # Screen settings
        self.screen_width = 1600
        self.screen_height = 1000
        self.bg_colour = (0, 0, 0)

        # Ship settings
        self.ship_limit = 4

        # Bullet settings
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_colour = (255, 255, 0)
        self.bullets_allowed = 4

        # Alien settings
        self.fleet_flight_speed = 10

        # How quickly the game speeds up
        self.speedup_scale = 1.2

        # How quickly the alien point values increase
        self.score_scale = 1.75

        self.initialise_dynamic_settings()
    
    def initialise_dynamic_settings(self, difficulty_factor=1):
        """Initialise settings that change throughout the game."""
        # Speed ship, bullets and aliens, scaled based on difficulty selected
        self.ship_speed = 2.0 
        self.bullet_speed = 3.0 * difficulty_factor
        self.alien_speed = 1.0 * difficulty_factor

        # fleet direction of 1 represents down; -1 represents up.
        self.fleet_direction = 1

        # Scoring settings; adjusted based on difficulty selected
        self.alien_points = 50 * difficulty_factor
    
    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)