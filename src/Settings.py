class Settings:
    """Settings of the game"""
    def __init__(self, size, spaceship_speed_x=2, spaceship_speed_y=1.5):
        """Initialize settings"""
        # General settings
        self.window_width = size[0]
        self.window_height = size[1]

        # Spaceship settings
        self.spaceship_speed_x = spaceship_speed_x
        self.spaceship_speed_y = spaceship_speed_y
