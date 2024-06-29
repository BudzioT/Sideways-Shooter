import os

import pygame.image


class Spaceship:
    """Spaceship which player can control"""
    def __init__(self, game):
        """Initialize spaceship at starting position"""
        self.surface = game.surface
        self.surface_rect = self.surface.get_rect()

        # Set settings like the game
        self.settings = game.settings

        # Get file path
        base_path = game.base_path
        # Load the image, convert it to accept transparency, get its rectangle
        self.image = pygame.image.load(os.path.join(base_path, "images/player.png")).convert_alpha()
        self.rect = self.image.get_rect()
        # Make it 2.3 times smaller, update the hitboxes
        self.image = (
            pygame.transform.scale(self.image, (self.rect.width / 2.3, self.rect.height / 2.3)))
        self.rect = self.image.get_rect()

        # Set the player start position
        self.return_start_pos()

        # Exact positions
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

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
