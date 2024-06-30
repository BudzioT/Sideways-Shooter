import os
from random import randint

import pygame.image
from pygame.sprite import Sprite


class PowerUp(Sprite):
    """PowerUp that increases certain settings"""
    def __init__(self, game, enemy, power_type):
        """Initialize PowerUp"""
        super().__init__()
        # Save the game and enemy reference
        self.game = game
        self.enemy = enemy

        # Save the game settings
        self.settings = game.settings

        # Save reference to the spaceship
        self.spaceship = game.spaceship

        # Grab surface from the game
        self.surface = game.surface
        self.surface_rect = self.surface.get_rect()
        # Set the type of PowerUp
        self.power_type = power_type

        # Create the file name based off PowerUp type
        name = str("images/" + power_type + ".png")
        # Load the image and its rect
        self.image = pygame.image.load(os.path.join(game.base_path, name))
        self.rect = self.image.get_rect()
        # Scale it down, update the rect
        self.image = (
            pygame.transform.scale(self.image, (self.rect.width / 8, self.rect.height / 8)))
        self.rect = self.image.get_rect()

        # Spawn PowerUp at enemy location
        self.rect.center = self.enemy.rect.center

        # Random vertical direction of movement: 1 is downwards, 0 is straight, -1 is upwards
        self.vertical_direction = randint(-1, 1)

        # Store float position for higher precision
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        """Update position of a PowerUp"""
        # Move the PowerUp in horizontal direction
        self.x -= self.settings.powerup_speed_x
        self.rect.x = self.x
        # Move the PowerUp in vertical direction
        self.y += self.settings.powerup_speed_y * self.vertical_direction
        self.rect.y = self.y

    def check_vertical_edges(self):
        """Check if there is a collision with vertical edge, if so, change the direction"""
        if (self.rect.bottom >= self.game.settings.window_height) or (self.rect.top <= 0):
            # Change the direction
            self.vertical_direction = -self.vertical_direction

    def check_left_edge(self):
        """Return if the PowerUp is behind the left edge"""
        return self.rect.right <= 0

    def upgrade_ship(self):
        """Upgrade the ship based of a PowerUp type"""
        # Increase limit of bullets
        if self.power_type == "BulletsUp":
            self.settings.sp_bullet_limit += 1
        # Increase the height of bullets
        elif self.power_type == "HeightUp":
            self.settings.sp_bullet_height += 2
        # Increase the speed of spaceship and bullets
        elif self.power_type == "SpeedUp":
            self.settings.sp_bullet_speed += 0.5
            self.settings.spaceship_speed_x += 0.5
            self.settings.spaceship_speed_y += 0.5
        # Create a shield
        elif self.power_type == "Shield":
            self.spaceship.shield = True
            self.spaceship.timer = float(pygame.time.get_ticks())

