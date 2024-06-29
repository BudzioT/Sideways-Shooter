import os
import math

import pygame


class Background:
    """Class that represents background"""
    def __init__(self, game):
        """Initialize background"""
        # Get surface from the game
        self.surface = game.surface

        # Get background image
        self.image = pygame.image.load(os.path.join(game.base_path, "images/background.png")).convert()

        # Background scroll
        self.scroll = 0

        # Calculate number of tiles that are in the background
        self.tiles = math.ceil(game.settings.window_width / self.image.get_width()) + 1

    def draw(self, i):
        """Draw the background"""
        # Draw the background at the right position
        self.surface.blit(self.image, (self.image.get_width() * i + self.scroll, 0))

    def reset_scroll(self):
        """Reset scroll when it is the end of background"""
        # If scroller moves beyond surface width, reset scroller
        if abs(self.scroll) > self.image.get_width():
            self.scroll = 0
