import pygame.font
from pygame.sprite import Sprite

from Spaceship import Spaceship


class Statboard:
    """Board with statistics displayed"""
    def __init__(self, game, font_color=(30, 30, 30)):
        """Initialize score display properties"""
        # Get reference to game
        self.game = game
        # Get game surface
        self.surface = game.surface
        self.surface_rect = self.surface.get_rect()

        # Settings for displaying scores
        self.font_color = font_color
        self.font = pygame.font.SysFont(None, 48)

        # Set all scoreboard text
        self._set_text()

    def draw(self):
        """Draw the live game statistics"""
        pass

    def draw_highscore(self):
        """Draw the highscore"""
        pass

    def set_score(self):
        """Render an image of the score"""
        pass

    def set_highscore(self):
        """Render an image of the highscore"""
        pass

    def set_spaceships(self):
        """Render an image of the count of spaceships"""
        pass

    def _set_text(self):
        """Set all scoreboard text"""
        # Set score text
        self.set_score()
        # Set highscore text
        self.set_highscore()
        # Set spaceships count text
        self.set_spaceships()

    def check_highscore(self):
        """Check if there is a new highscore and set it"""
        pass

