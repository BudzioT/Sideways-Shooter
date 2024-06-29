class Stats:
    """Game statistics"""
    def __init__(self, game):
        """Initialize statistics of the game"""
        # Get settings from the game
        self.settings = game.settings
        # Set stats that are crucial to the game
        self.reset_stats()

    def reset_stats(self):
        """Reset statistics"""
        self.spaceships_left = self.settings.spaceships_limit
