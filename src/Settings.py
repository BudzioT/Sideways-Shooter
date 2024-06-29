class Settings:
    """Settings of the game"""
    def __init__(self, size, spaceship_speed_x=2.5, spaceship_speed_y=2,
                 sp_bullet_width=15, sp_bullet_height=3, sp_bullet_speed=3,
                 sp_bullet_limit=5, enemy_speed=1, enemy_limit=7, spaceships_limit=3,
                 enemy_bullet_limit=2, enemy_bullet_speed=2,
                 enemy_bullet_width=10, enemy_bullet_height=3):
        """Initialize settings"""
        # General settings
        self.window_width = size[0]
        self.window_height = size[1]

        # Spaceship settings
        self.spaceship_speed_x = spaceship_speed_x
        self.spaceship_speed_y = spaceship_speed_y
        self.spaceships_limit = spaceships_limit

        # Spaceship bullet settings
        self.sp_bullet_color = (250, 189, 90)
        self.sp_bullet_speed = sp_bullet_speed
        self.sp_bullet_width, self.sp_bullet_height = sp_bullet_width, sp_bullet_height
        self.sp_bullet_limit = sp_bullet_limit

        # Enemy settings
        self.enemy_speed = enemy_speed
        self.enemy_limit = enemy_limit

        # Enemy bullet settings
        self.enemy_bullet_color = (30, 250, 74)
        self.enemy_bullet_limit = enemy_bullet_limit
        self.enemy_bullet_speed = enemy_bullet_speed
        self.enemy_bullet_height, self.enemy_bullet_width = (
            enemy_bullet_height, enemy_bullet_width)
