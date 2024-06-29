import os.path
import sys

import pygame

from Background import Background
from Settings import Settings
from Spaceship import Spaceship
from Enemy import Enemy


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
        # Enemies
        self.enemies = pygame.sprite.Group()
        self._create_enemies()

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
        # Shoot a bullet
        elif event.key == pygame.K_SPACE:
            self.spaceship.fire_bullet()

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
        # Draw the bullets
        self.spaceship.update_bullets()
        # Draw the enemies
        self.enemies.draw(self.surface)

        # Update contents of the surface
        pygame.display.flip()

    def _update_pos(self):
        """Update position of things"""
        # Spaceship position
        self.spaceship.update_pos()
        # Spaceship bullets position
        self.spaceship.bullets.update()
        # Enemies position
        self._update_enemies()

    def _update_enemies(self):
        """Update all enemies positions"""
        self.enemies.update()
        # Change direction if there is a collision with an edge
        self._check_enemies_edges()

        # If there is a collision between enemy and spaceship
        if pygame.sprite.spritecollideany(self.spaceship, self.enemies):
            # Handle spaceship getting hit
            self._spaceship_hit()

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

    def _create_enemies(self):
        """Create group of enemies"""
        # Create first enemy to get size of it
        enemy = Enemy(self)
        enemy_height = enemy.rect.height
        # While there is still space for enemies, create them
        while len(self.enemies) < self.settings.enemy_limit:
            self._create_enemy()

    def _create_enemy(self):
        """Create an enemy"""
        # Create an enemy
        new_enemy = Enemy(self)
        # Add it to the group
        self.enemies.add(new_enemy)

    def _spaceship_hit(self):
        """Handle spaceship getting hit"""
        pass

    def _check_enemies_edges(self):
        """If enemy touches edges, change its direction"""
        for enemy in self.enemies.sprites():
            if enemy.check_vertical_edges():
                enemy.update_vertical_direction()
                print("EDGE!")
            if enemy.check_horizontal_edges():
                enemy.horizontal_direction = not enemy.horizontal_direction
                enemy.update_vertical_direction()
                print("EDGE!")


if __name__ == "__main__":
    game = Shooter()
    game.run()
