import os
from random import randint, random

import pygame
import pygame.mixer
from pygame.sprite import Sprite

from EnemyBullet import EnemyBullet


class Enemy(Sprite):
    """Enemy which shoots bullets"""
    def __init__(self, game):
        """Initialize the enemy and its position"""
        super().__init__()
        # Get the game surface
        self.surface = game.surface
        # Use game settings
        self.settings = game.settings

        # Reference to the game
        self.game = game

        # Bullets shot by the enemy
        self.bullets = pygame.sprite.Group()

        # Load the image and hitboxes
        base_path = game.base_path
        self.image = pygame.image.load(os.path.join(base_path, "images/enemy.png")).convert_alpha()
        self.rect = self.image.get_rect()
        # Scale it down
        self.image = (
            pygame.transform.scale(self.image, (self.rect.width / 15, self.rect.height / 15)))
        # Update the rect
        self.rect = self.image.get_rect()

        # Load shoot sound
        self.shoot_sound = pygame.mixer.Sound(os.path.join(base_path, "sounds/enemy_shoot.ogg"))
        # Set the volume to quieter one
        self.shoot_sound.set_volume(0.3)

        # Spawn the enemy at random part of right side of the surface
        self.rect.x = self.settings.window_width - self.rect.width - 1
        self.rect.y = randint(self.rect.height + 1, self.settings.window_height - self.rect.height - 1)

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

    def _fire_bullet(self):
        """Fire bullet that flies to the left"""
        # If the limit is not reached yet, create a new bullet and add it to the group
        if len(self.bullets) < self.settings.enemy_bullet_limit:
            new_bullet = EnemyBullet(self.game, self)
            self.bullets.add(new_bullet)
            self.shoot_sound.play()

    def fire_randomly(self):
        """Fire bullet at random interval"""
        if random() < 0.01:
            self._fire_bullet()

    def check_vertical_edges(self):
        """Return if enemy touches an edge"""
        return ((self.rect.top <= 0)
                or (self.rect.bottom >= self.settings.window_height))

    def check_horizontal_edges(self):
        """Return if enemy touches left edge of the surface"""
        return (self.rect.left <= 0 or
                self.rect.right >= self.settings.window_width)

    def update_vertical_direction(self):
        """Change enemy's vertical direction to opposite one"""
        # Change the direction
        direction = -self.vertical_direction
        # Update direction to a new one
        self.vertical_direction = direction

    def _cleanup_bullets(self):
        """Cleanup bullets, that left visible part of the surface"""
        # Check if each bullet left the screen, if any did, clean it
        for bullet in self.bullets.sprites().copy():
            if bullet.rect.right <= 0:
                self.bullets.remove(bullet)

    def update_bullets(self):
        """Draw bullets and clean old ones"""
        # Draw every bullet
        for bullet in self.bullets.sprites():
            bullet.draw()
        # Clean old ones
        self._cleanup_bullets()
