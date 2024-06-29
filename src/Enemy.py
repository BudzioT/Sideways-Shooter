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
        # Scale it down
        self.image = (
            pygame.transform.scale(self.image, (self.rect.width / 15, self.rect.height / 15)))
        # Update the rect
        self.rect = self.image.get_rect()

        # Spawn the enemy at random part of right side of the surface
        self.rect.x = self.settings.window_width
        self.rect.y = randint(self.rect.height, self.settings.window_height - self.rect.height)

        # Vertical direction of movement: 1 is downwards, 0 is straight, -1 is upwards
        self.vertical_direction = randint(-1, 1)
        # Horizontal direction of movement: -1 is left, 1 is right
        self.horizontal_direction = -1

        # Store float position for higher precision
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        """Update position of the enemy"""
        # Move enemy in specified horizontal direction
        self.x += self.settings.enemy_speed * self.horizontal_direction
        self.rect.x = self.x
        # Move enemy in specified vertical direction
        self.y += self.settings.enemy_speed * self.vertical_direction
        self.rect.y = self.y

    def check_vertical_edges(self):
        """Return if enemy touches an edge"""
        return ((self.rect.top <= 0)
                or (self.rect.bottom >= self.settings.window_height))

    def check_horizontal_edges(self):
        """Return if enemy touches left edge of the surface"""
        return (self.rect.left <= 0 or
                self.rect.right >= self.settings.window_width)

    def update_vertical_direction(self):
        """Change enemy direction to random one"""
        self.vertical_direction = randint(-1, 1)
