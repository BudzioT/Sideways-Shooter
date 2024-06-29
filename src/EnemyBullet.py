import pygame
from pygame.sprite import Sprite


class EnemyBullet(Sprite):
    """Class representing bullet shot by the enemy"""
    def __init__(self, game, enemy):
        """Initialize the bullet fired from an enemy"""
        super().__init__()
        # Set surface to the game surface
        self.surface = game.surface
        # Get settings from the game
        self.settings = game.settings

        # Save enemy
        self.enemy = enemy

        # Set bullet color
        self.color = self.settings.enemy_bullet_color

        # Create bullet at temp location, fix it
        self.rect = pygame.Rect(0, 0, self.settings.enemy_bullet_width,
                                self.settings.enemy_bullet_height)
        self.rect.center = self.enemy.rect.center

        # Save position in float for higher precision
        self.x = float(self.rect.x)

    def draw(self):
        """Draw the enemy bullet"""
        pygame.draw.rect(self.surface, self.color, self.rect)

    def update(self):
        """Move bullet forward, in the left direction based off speed"""
        # Update float position
        self.x -= self.settings.enemy_bullet_speed
        # Update real rect
        self.rect.x = self.x
