import os.path
import sys

import pygame

from Background import Background
from Settings import Settings
from Spaceship import Spaceship


class Shooter:
    """Class to manage the entire game"""
    def __init__(self, size=(720, 576), fullscreen=False):
        """Initialize the game"""
        # Init pygame and pygame mixer
        pygame.init()
        pygame.mixer.init()

        # Set setting of the game
        self.settings = Settings(size)

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
        # Spaceship - the player
        self.spaceship = Spaceship(self)

        # Timer for FPS calculation
        self.timer = pygame.time.Clock()

    def run(self):
        """Run the game"""
        while True:
            # Handle all events
            self._get_events()

            # Update positions
            self._update_pos()

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
            # Handle key press events
            elif event.type == pygame.KEYDOWN:
                self._handle_keydown(event)
            # Handle key release events
            elif event.type == pygame.KEYUP:
                self._handle_keyup(event)

    def _handle_keydown(self, event):
        """Handle keydown events"""
        # Quit on escape
        if event.key == pygame.K_ESCAPE:
            sys.exit()
        # Move left
        elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
            self.spaceship.move_flags["Left"] = True
        # Move right
        elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            self.spaceship.move_flags["Right"] = True
        # Move up
        elif event.key == pygame.K_UP or event.key == pygame.K_w:
            self.spaceship.move_flags["Up"] = True
        # Move down
        elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
            self.spaceship.move_flags["Down"] = True

    def _handle_keyup(self, event):
        """Handle keyup events"""
        # Stop moving left
        if event.key == pygame.K_LEFT or event.key == pygame.K_a:
            self.spaceship.move_flags["Left"] = False
        # Stop moving right
        elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            self.spaceship.move_flags["Right"] = False
        # Stop moving up
        elif event.key == pygame.K_UP or event.key == pygame.K_w:
            self.spaceship.move_flags["Up"] = False
        # Stop moving down
        elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
            self.spaceship.move_flags["Down"] = False

    def _update_surface(self):
        """Update visible items on surface"""
        # Draw the background
        self._scroll_background()
        # Draw the player
        self.spaceship.draw()

        # Update contents of the surface
        pygame.display.flip()

    def _update_pos(self):
        """Update position of things"""
        self.spaceship.update_pos()

    def _scroll_background(self):
        """Scroll the background"""
        # Position variable
        i = 0
        # While current position is still in background tiles, draw it
        while i < self.background.tiles:
            self.background.draw(i)
            i += 1
        # Scroll the background and reset it if needed
        self.background.scroll -= 6
        self.background.reset_scroll()


if __name__ == "__main__":
    game = Shooter()
    game.run()
