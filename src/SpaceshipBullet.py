import pygame
from pygame.sprite import Sprite


class SpaceshipBullet(Sprite):
    """Bullet fired from the ship"""
    def __init__(self, game):
        """Initialize bullet starting at the spaceship position"""
        super().__init__()
        # Set surface from game reference
        self.surface = game.surface
        # Get settings from the game
        self.settings = game.settings

        # Set bullet color
        self.color = self.settings.sp_bullet_color

        # Create bullet at temp location, then fix it
        self.rect = pygame.Rect(0, 0, self.settings.sp_bullet_width,
                                self.settings.sp_bullet_height)
        self.rect.center = game.spaceship.rect.center

        # Store bullet position as float for higher precision
        self.x = float(self.rect.x)

    def draw(self):
        """Draw spaceship bullet onto the surface"""
        pygame.draw.rect(self.surface, self.color, self.rect)

    def update(self):
        """Move the bullet forward based off speed"""
        # Update position with float to get more precision
        self.x += self.settings.sp_bullet_speed
        # Update real rect position
        self.rect.x = self.x
