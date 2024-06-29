import os
from random import randint

import pygame
from pygame.sprite import Sprite


class Enemy(Sprite):
    """Enemy which shoots bullets"""
    def __init__(self, game):
        """Initialize the enemy and its position"""
        super().__init__()
        # Get the game surface
        self.surface = game.surface
        # Use game settings
        self.settings = game.settings

        # Load the image and hitboxes
        base_path = game.base_path
        self.image = pygame.image.load(os.path.join(base_path, "images/enemy.png")).convert_alpha()
        self.rect = self.image.get_rect()

        # Spawn the enemy at random part of right side of the surface
        self.rect.x = self.settings.window_width
        self.rect.y = randint(self.rect.y, self.settings.window_height)

        # Store float position for higher precision
        self.x = float(self.rect.x)

    def update(self):
        """Update position of the enemy"""
        # Move enemy forwards
        self.x -= self.settings.enemy_speed
        self.rect.x = self.x

    def check_edges(self):
        """Return if enemy touches an edge"""
        return self.rect.left <= 0
