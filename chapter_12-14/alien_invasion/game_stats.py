from pathlib import Path

class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialise statistics."""
        self.settings = ai_game.settings
        self.reset_stats()
        # High score should never be reset.
        self.get_high_score()

    def get_high_score(self):
        path = Path('high_score.txt')
        if path.exists():
            self.high_score = int(path.read_text())
        else:
            self.high_score = 0
    
    def reset_stats(self):
        """Initialise statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1