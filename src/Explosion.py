import os

import pygame.image
from pygame.sprite import Sprite


class Explosion(Sprite):
    """Explosion effect"""
    def __init__(self, game, spaceship):
        """Initialize the explosion effect"""
        super().__init__()
        # Get surface of the game
        self.surface = game.surface
        self.surface_rect = self.surface.get_rect()

        # Save reference to the spaceship
        self.spaceship = spaceship

        # Get files directory
        base_path = game.base_path

        # Set the images of explosion
        self.images = []
        # Go through each explosion image, numbered from 00 to 08
        for i in range(9):
            # Create a file name based of explosion number
            file_name = "images/explosion/explosion0" + str(i) + ".png"
            # Append the file to the images list
            self.images.append(pygame.image.load(os.path.join(base_path, file_name)))

        # Current frame
        self.frame = 0
        # Current image
        self.image = self.images[self.frame]
        # Take rect from the current image
        self.rect = self.image.get_rect()
        # Center the explosion to the spaceship position
        self.rect.center = spaceship.rect.center

        # Frame counter to make animation slower
        self.tick_count = 0

    def update(self):
        """Update frames of explosion"""
        # Count the game frame
        self.tick_count += 1

        # If this is the fifth frame from the last one, update the image
        if self.tick_count % 5 == 0:
            # If there are still frames left
            if self.frame < len(self.images) - 1:
                # Go to the next frame
                self.frame += 1
                # Save the image of the new explosion frame
                self.image = self.images[self.frame]
                # Set new rect and center it based off the ship position
                self.rect = self.image.get_rect()
                self.rect.center = self.spaceship.rect.center
            # If there aren't frames anymore, delete the explosion effect
            else:
                self.kill()
