from pygame.sprite import Sprite


class EnemyBullet(Sprite):
    """Class representing bullet shot by the enemy"""
    def __init__(self, game):
        """Initialize the bullet fired from an enemy"""
        super().__init__()
        # Set surface to the game surface
        self.surface = game.surface
        # Get settings from the game
        self.settings = game.settings

        # Set bullet color
        self.color = self.settings.enemy_bullet_color
