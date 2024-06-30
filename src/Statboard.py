import pygame
import pygame.font
from pygame.sprite import Group

from Spaceship import Spaceship


class Statboard:
    """Board with statistics displayed"""
    def __init__(self, game, font_color=(237, 242, 239)):
        """Initialize score display properties"""
        # Get reference to game
        self.game = game
        # Get game surface
        self.surface = game.surface
        self.surface_rect = self.surface.get_rect()

        # Set stats and settings
        self.settings = game.settings
        self.stats = game.stats

        # Settings for displaying scores
        self.font_color = font_color
        self.font = pygame.font.SysFont(None, 48)

        # Set all scoreboard text
        self._set_text()

    def draw(self):
        """Draw the live game statistics"""
        # Draw the score
        self.surface.blit(self.score_image, self.score_rect)
        # Draw the spaceships count
        self.spaceships.draw(self.surface)

    def draw_highscore(self):
        """Draw the highscore"""
        self.surface.blit(self.highscore_image, self.highscore_rect)

    def set_score(self):
        """Render an image of the score"""
        # Round the score
        score = int(round(self.stats.score, -1))
        # Format it
        score = str(f"{score:,}")
        # Render the image
        self.score_image = self.font.render(score, True, self.font_color).convert_alpha()

        # Display score at the top right part of the surface
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.surface_rect.right - 20
        self.score_rect.top = 20

    def set_highscore(self):
        """Render an image of the highscore"""
        # Round the highscore
        highscore = int(round(self.stats.highscore, -1))
        # Format it
        highscore = str(f"{highscore:,}")
        # Render the image
        self.highscore_image = self.font.render(highscore, True, self.font_color).convert_alpha()

        # Display highscore at the top center part of the screen
        self.highscore_rect = self.highscore_image.get_rect()
        self.highscore_rect.top = self.score_rect.top
        self.highscore_rect.centerx = self.surface_rect.centerx

    def set_spaceships(self):
        """Render an image of the count of spaceships"""
        # Set the margin to 0, to increase it later
        margin = 0
        # Make a group of spaceships representing lives
        self.spaceships = Group()
        # Go through each spaceship left and render it
        for spaceship_num in range(self.stats.spaceships_left):
            # Make a spaceship representing live
            spaceship = Spaceship(self.game)
            # Scale it down by half
            spaceship.image = (pygame.transform.scale(spaceship.image,
                                                      (spaceship.rect.width / 2,
                                                       spaceship.rect.height / 2)))
            # Fix its rectangle
            spaceship.rect = spaceship.image.get_rect()
            # Set position of the ship ten pixels from the left edge of the surface
            # and 5 pixels from the next ship
            spaceship.rect.x = 10 + spaceship_num * spaceship.rect.width + margin
            spaceship.rect.y = 10
            # Add it to the spaceships group
            self.spaceships.add(spaceship)
            # Increase margin by 5
            margin += 5

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
        if self.stats.score >= self.stats.highscore:
            # Set a new highscore and update old text
            self.stats.highscore = self.stats.score
            self.set_highscore()

