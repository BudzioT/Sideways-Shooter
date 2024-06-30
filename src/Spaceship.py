import os

import pygame.image
from pygame.sprite import Sprite

from SpaceshipBullet import SpaceshipBullet


class Spaceship(Sprite):
    """Spaceship which player can control"""
    def __init__(self, game):
        """Initialize spaceship at starting position"""
        super().__init__()

        # Set the surface based of the game one
        self.surface = game.surface
        self.surface_rect = self.surface.get_rect()

        # Set settings like the game
        self.settings = game.settings

        # Set game reference
        self.game = game

        # Get file path
        base_path = game.base_path
        # Load the image, convert it to accept transparency, get its rectangle
        self.image = pygame.image.load(os.path.join(base_path, "images/player.png")).convert_alpha()
        self.rect = self.image.get_rect()
        # Make it 2.3 times smaller, update the hitboxes
        self.image = (
            pygame.transform.scale(self.image, (self.rect.width / 2.3, self.rect.height / 2.3)))
        self.rect = self.image.get_rect()

        # Load the shooting sound
        self.shoot_sound = pygame.mixer.Sound(os.path.join(base_path, "sounds/sp_shoot.wav"))
        # Set the volume to quieter
        self.shoot_sound.set_volume(0.05)

        # Load explosion sound
        self.explosion_sound = pygame.mixer.Sound(os.path.join(base_path, "sounds/explosion.wav"))
        # Set the volume to quieter
        self.shoot_sound.set_volume(0.1)

        # Set the player start position
        self.return_start_pos()

        # Exact positions
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Spaceship bullets
        self.bullets = pygame.sprite.Group()

        # Flags indicating movement
        self.move_flags = {
            "Left": False,
            "Right": False,
            "Up": False,
            "Down": False
        }

    def draw(self):
        """Draw the spaceship"""
        self.surface.blit(self.image, self.rect)

    def update_pos(self):
        """Update position based of movement flags"""
        # Move left
        if self.move_flags["Left"] and self.rect.left > 0:
            self.x -= self.settings.spaceship_speed_x
        # Move right
        if self.move_flags["Right"] and self.rect.right < self.surface_rect.right:
            self.x += self.settings.spaceship_speed_x
        # Move up
        if self.move_flags["Up"] and self.rect.top > 0:
            self.y -= self.settings.spaceship_speed_y
        # Move down
        if self.move_flags["Down"] and self.rect.bottom < self.surface_rect.bottom:
            self.y += self.settings.spaceship_speed_y

        # Update real rect positions
        self.rect.x = self.x
        self.rect.y = self.y

    def return_start_pos(self):
        """Return to the start position"""
        # Return to the center left part of the surface
        self.rect.left = self.surface.get_rect().left
        self.rect.centery = self.surface.get_rect().centery

        # Set the more precise, exact positions
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def fire_bullet(self):
        """Fire a bullet"""
        # Create a bullet if there is still space, add it to the bullets group
        if len(self.bullets) < self.settings.sp_bullet_limit:
            bullet = SpaceshipBullet(self.game)
            self.bullets.add(bullet)
            self.shoot_sound.play()

    def _cleanup_bullets(self):
        """Cleanup bullets after they leave visible part of the surface"""
        # Go through each bullet (copy, because bullets can be removed)
        for bullet in self.bullets.sprites().copy():
            # If left part of the bullet touches the edge, remove it
            if bullet.rect.left > self.settings.window_width:
                self.bullets.remove(bullet)

    def update_bullets(self):
        """Draw bullets, cleanup old ones"""
        # Draw every bullet
        for bullet in self.bullets.sprites():
            bullet.draw()
        # Cleanup old bullets
        self._cleanup_bullets()

    def play_explosion(self):
        """Play the explosion sound"""
        self.explosion_sound.play()
