from pathlib import Path

class GameStats:
    """Tracks statistics for Sideways Shooter. """
    
    def __init__(self, ss_game):
        """Initialise statistics."""
        self.settings = ss_game.settings
        self.reset_stats()
        self.get_high_score()
    
    def get_high_score(self):
        """Gets high score from saved file if it exists"""
        path = Path('high_score.txt')
        if path.exists():
            self.high_score = int(path.read_text())
        else:
            self.high_score = 0
    
    def reset_stats(self):
        """Initialise statistics that can change during the game"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1