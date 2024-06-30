import os.path
import sys
from time import sleep

import pygame

from Background import Background
from Settings import Settings
from Spaceship import Spaceship
from Enemy import Enemy
from Stats import Stats
from Button import Button
from Title import Title
from Statboard import Statboard
from PowerUp import PowerUp


class Shooter:
    """Class to manage the entire game"""
    def __init__(self, size=(720, 576), fullscreen=False):
        """Initialize the game"""
        # Init pygame and pygame mixer
        pygame.init()
        pygame.mixer.init()

        # Get current directory
        self.base_path = os.path.dirname(os.path.abspath(__file__))

        # Set setting of the game
        self.settings = Settings(size)

        # Lose count to fix spaceship count
        self.lose_count = 0

        # Current state of the game
        self.active = False

        # Stats of the game
        self.stats = Stats(self)

        # Set new surface with given size and name Sideways Shooter
        if fullscreen:
            self.surface = pygame.display.set_mode((0, 0), fullscreen)
        else:
            self.surface = pygame.display.set_mode(size)
        pygame.display.set_caption("Sideways Shooter")

        # Game's background
        self.background = Background(self)
        # Menu background
        self.menu_background = self.settings.bg_color
        # Spaceship - the player
        self.spaceship = Spaceship(self)
        # Enemies
        self.enemies = pygame.sprite.Group()
        self._create_enemies()
        # Powerups
        self.powerups = pygame.sprite.Group()

        # Timer for FPS calculation
        self.timer = pygame.time.Clock()

        # Statistics board
        self.stat_board = Statboard(self)

        # Play the game button
        self.play_button = Button(self, "Play")

        # Title of the game
        self.title = Title(self, "Sideways shooter")

        # Load enemy death sound
        self.enemy_death_sound = (
            pygame.mixer.Sound(os.path.join(self.base_path, "sounds/enemyKilled.flac")))
        # Set the volume to quieter one
        self.enemy_death_sound.set_volume(0.1)

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

            # Handle mouse presses
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Get the cursor position
                cursor_pos = pygame.mouse.get_pos()
                # If user clicked the mouse, check if he clicked Play button
                self._check_play(cursor_pos)

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

        # If game is active, draw its content
        if self.active:
            # Draw the background
            self._scroll_background()

            # Draw the player
            self.spaceship.draw()
            # Draw the enemies
            self.enemies.draw(self.surface)

            # Draw and update spaceship bullets
            self._update_sp_bullets()
            # Draw and update enemy bullets
            self._update_enemy_bullets()

            # Draw the PowerUps
            self.powerups.draw(self.surface)

            # Draw the statistics board
            self.stat_board.draw()

        # If game isn't active, draw the game menu
        else:
            # Draw background
            self.surface.fill(self.menu_background)
            # Draw play button
            self.play_button.draw_button()
            # Draw the title
            self.title.draw()
            # Draw the highscore
            self.stat_board.draw_highscore()

        # Update contents of the surface
        pygame.display.flip()

    def _update_pos(self):
        """Update position of things"""
        # If the game is active, update all positions
        if self.active:
            # Spaceship position
            self.spaceship.update_pos()

            # Spaceship bullets position
            self.spaceship.bullets.update()
            # Enemy bullets position
            for enemy in self.enemies.sprites():
                enemy.bullets.update()

            # PowerUp positions
            self.powerups.update()

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

        # Update enemy bullets
        self._update_enemy_bullets()

    def _update_sp_bullets(self):
        """Draw existing bullets, clean old ones"""
        # Draw the bullets, clean old ones
        self.spaceship.update_bullets()
        # Check for collision with enemies
        self._check_sp_bullet_collisions()

    def _update_enemy_bullets(self):
        """Fire new bullets, draw existing ones and clean old ones"""

        # Fire the bullets, draw them, clean old ones for every enemy
        for enemy in self.enemies:
            enemy.fire_randomly()
            enemy.update_bullets()
        # Check for collision with spaceship
        self._check_enemy_bullet_collisions()

    def _update_powerups(self):
        """Update PowerUps positions, clean old ones"""
        pass

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
        # While there is still space for enemies, create them
        while len(self.enemies) < self.settings.enemy_limit:
            self._create_enemy()

    def _create_enemy(self):
        """Create an enemy"""
        # Create an enemy
        new_enemy = Enemy(self)
        # Add it to the group
        self.enemies.add(new_enemy)

    def _check_enemies_edges(self):
        """If enemy touches edges, change its direction"""
        for enemy in self.enemies.sprites():
            if enemy.check_vertical_edges():
                enemy.update_vertical_direction()
            if enemy.check_horizontal_edges():
                enemy.horizontal_direction = -enemy.horizontal_direction
                enemy.update_vertical_direction()

    def _check_sp_bullet_collisions(self):
        """Check collisions between spaceship bullets and enemies, spawn enemies if needed"""
        # Check for collisions with enemies
        collisions = pygame.sprite.groupcollide(self.spaceship.bullets, self.enemies,
                                                True, True)

        # If there are collisions, update the score
        if collisions:
            # Check every collision, increase the score for each one
            for enemy in collisions.values():
                self.stats.score += self.settings.earn_points
                # Increase difficulty if needed
                self.settings.increase_diff(int(self.stats.score))

                # Spawn the PowerUp
                new_powerup = PowerUp(game, enemy[0], "BulletsUp")
                self.powerups.add(new_powerup)

            # Play the enemy death sound
            self._play_enemy_death_sound()

            # Update the statistics board
            self.stat_board.set_score()
            self.stat_board.check_highscore()

        # Spawn new enemies
        self._create_enemies()

    def _check_enemy_bullet_collisions(self):
        """Check collisions between enemy bullets and spaceship, decrease spaceship count if needed"""
        # Check for collisions with spaceship
        for enemy in self.enemies.sprites():
            collisions = pygame.sprite.spritecollideany(self.spaceship, enemy.bullets)
            if collisions:
                self._spaceship_hit()
                break

    def _check_play(self, mouse_pos):
        """If mouse is on the button, start the game"""
        # Check if mouse collides with the Play button
        if self.play_button.rect.collidepoint(mouse_pos) and not self.active:
            self._start_game()

    def _spaceship_hit(self):
        """Handle spaceship getting hit"""
        # Set the highscore
        self.stats.save_highscore()

        # If this was the last live, end the game
        if self.stats.spaceships_left <= 0:
            self.active = False

            # Increase lose count
            self.lose_count += 1
            # Show the mouse to navigate through the menu
            pygame.mouse.set_visible(True)

            # If user lost for the first time, increase the live limit, because after losing,
            # automatically user loses starting live
            if self.lose_count == 1:
                self.settings.spaceships_limit = self.settings.spaceships_limit + 1

            # Go back to menu
            return None

        # Decrement spaceships count (lives)
        self.stats.spaceships_left -= 1

        # Play spaceship explosion sound
        self.spaceship.play_explosion()

        # Update the spaceships count
        self.stat_board.set_spaceships()

        # Return spaceship to the starting position
        self.spaceship.return_start_pos()

        # Clean the bullets and the enemies
        self.spaceship.bullets.empty()
        for enemy in self.enemies.sprites():
            enemy.bullets.empty()
        self.enemies.empty()

        # Give player time to realize getting shot
        sleep(1)

    def _start_game(self):
        """Start the game"""
        # Reset the changed settings if user lost at least once
        if self.lose_count > 0:
            self.settings.reset_settings()

        # Reset the stats
        self.stats.reset_stats()

        # Update the score
        self.stat_board.set_score()

        # Activate the game
        self.active = True

        # Hide the cursor, so player can focus on the game
        pygame.mouse.set_visible(False)

    def _play_enemy_death_sound(self):
        """Play the death sound"""
        self.enemy_death_sound.play()

    def _clean_powerups(self):
        """Clean the powerups that left the visible surface"""
        # Go thorough each powerup that exists
        for powerup in self.powerups.sprites().copy():
            # If it went beyond the left edge of the surface, clean it
            if powerup.check_left_edge():
                self.powerups.remove(powerup)


if __name__ == "__main__":
    game = Shooter()
    game.run()
