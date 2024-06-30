from pygame.sprite import Sprite


class PowerUp(Sprite):
    """PowerUp that increases certain settings"""
    def __init__(self, power_type, speed=3):
        """Initialize PowerUp"""
        super().__init__()
        # Set the type of PowerUp
        self.power_type = power_type
