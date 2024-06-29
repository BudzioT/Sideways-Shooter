import os

import pygame.image


class Spaceship:
    """Spaceship which player can control"""
    def __init__(self, game):
        """Initialize spaceship at starting position"""
        self.surface = game.surface

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

    def return_start_pos(self):
        """Return to the start position"""
        # Return to the center left part of the surface
        self.rect.left = self.surface.get_rect().left
        self.rect.centery = self.surface.get_rect().centery

        # Set the more precise, exact positions
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
