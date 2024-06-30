from pathlib import Path
import json
import os


class Stats:
    """Game statistics"""
    def __init__(self, game):
        """Initialize statistics of the game"""
        # Get settings from the game
        self.settings = game.settings
        # Set spaceships left equal to the limit
        self.spaceships_left = self.settings.spaceships_limit
        # Set score to 0
        self.score = 0

        # Highscore, that isn't affected by reset
        self.highscore = 0
        # Absolute path to game's directory
        self.base_path = game.base_path
        # Read the highscore
        self.read_highscore()

    def reset_stats(self):
        """Reset statistics"""
        # Reset spaceships count
        self.spaceships_left = self.settings.spaceships_limit
        # Reset score
        self.score = 0

    def save_highscore(self):
        """Save highscore to a file"""
        # Open file at the absolute path
        file = Path(os.path.join(self.base_path, "data/highscore.json"))
        # Save highscore in file
        file.write_text(json.dumps(self.highscore))

    def read_highscore(self):
        """Read highscore from a file"""
        # Open file at the absolute path
        file = Path(os.path.join(self.base_path, "data/highscore.json"))
        # Set new highscore to 0, so in case the file doesn't exist, data doesn't corrupt
        new_highscore = 0
        # If file exists, save highscore from it
        if file.exists():
            # Read value from the file
            new_highscore = json.loads(file.read_text())
            # If highscore stored in file is higher than the current one, replace current
            if self.highscore < new_highscore:
                self.highscore = new_highscore
