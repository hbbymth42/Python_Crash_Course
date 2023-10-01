class GameStats:
    def __init__(self, tp_game):
        self.settings = tp_game.settings
        self.reset_stats()
    
    def reset_stats(self):
        self.ships_left = self.settings.ship_limit