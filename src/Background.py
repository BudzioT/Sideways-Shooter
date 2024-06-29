import os

import pygame


class Background:
    """Class that represents background"""
    def __init__(self, game):
        """Initialize background"""
        # Get surface from the game
        self.surface = game.surface

        # Get background image
        self.image = pygame.image.load(os.path.join(game.base_path, "images/background.png"))

    def draw(self):
        """Draw the background"""
        self.surface.blit(self.image, (0, 0))
