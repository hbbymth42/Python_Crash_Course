class Settings:

    def __init__(self):
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_colour = (0, 0, 0)

        # Ship settings
        self.ship_limit = 2

        # Bullet settings
        self.bullet_speed = 3.0
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_colour = (255, 255, 0)
        self.bullets_allowed = 4

        # Rectangle settings
        self.rect_colour = (200, 0, 0)

        self.speedup_scale = 1.2
        
        self.initialise_dynamic_settings()
    
    def initialise_dynamic_settings(self):
        self.ship_speed = 2.0
        self.rect_speed = 1.0
        
        self.rect_direction = 1
    
    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.rect_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale