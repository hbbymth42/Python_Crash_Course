class Settings:

    def __init__(self):

        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_colour = (0, 0, 0)

        # Ship settings
        self.ship_speed = 2.0

        # Bullet settings
        self.bullet_speed = 3.0
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_colour = (255, 255, 0)
        self.bullets_allowed = 4

        # Alien settings
        self.alien_speed = 1.0
        self.fleet_flight_speed = 10
        self.fleet_direction = 1