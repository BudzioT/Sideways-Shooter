import os.path
import sys

import pygame

from Background import Background


class Shooter:
    """Class to manage the entire game"""
    def __init__(self, size=(720, 576), fullscreen=False):
        """Initialize the game"""
        # Init pygame and pygame mixer
        pygame.init()
        pygame.mixer.init()

        # Get current directory
        self.base_path = os.path.dirname(os.path.abspath(__file__))

        # Set new surface with given size and name Sideways Shooter
        if fullscreen:
            self.surface = pygame.display.set_mode((0, 0), fullscreen)
        else:
            self.surface = pygame.display.set_mode(size)
        pygame.display.set_caption("Sideways Shooter")

        # Game's background
        self.background = Background(self)

        # Timer for FPS calculation
        self.timer = pygame.time.Clock()

    def run(self):
        """Run the game"""
        while True:
            # Handle all events
            self._get_events()

            # Update the surface
            self._update_surface()
            # Put the game in 60 FPS
            self.timer.tick(60)

    def _get_events(self):
        """Handle given events"""
        for event in pygame.event.get():
            # Quit
            if event.type == pygame.QUIT:
                sys.exit()
            # Handle keydown events
            elif event.type == pygame.KEYDOWN:
                # Quit on escape
                if event.key == pygame.K_ESCAPE:
                    sys.exit()

    def _update_surface(self):
        """Update visible items on surface"""
        # Draw the background
        self.background.draw()

        # Update contents of the surface
        pygame.display.flip()


if __name__ == "__main__":
    game = Shooter()
    game.run()
