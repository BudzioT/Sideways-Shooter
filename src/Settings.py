class Settings:
    """Settings of the game"""
    def __init__(self, size, spaceship_speed_x=2.5, spaceship_speed_y=2,
                 sp_bullet_width=15, sp_bullet_height=3, sp_bullet_speed=3,
                 sp_bullet_limit=3, enemy_speed=2, enemy_limit=10):
        """Initialize settings"""
        # General settings
        self.window_width = size[0]
        self.window_height = size[1]

        # Spaceship settings
        self.spaceship_speed_x = spaceship_speed_x
        self.spaceship_speed_y = spaceship_speed_y

        # Spaceship bullet settings
        self.sp_bullet_color = (250, 189, 90)
        self.sp_bullet_speed = sp_bullet_speed
        self.sp_bullet_width, self.sp_bullet_height = sp_bullet_width, sp_bullet_height
        self.sp_bullet_limit = sp_bullet_limit

        # Enemy settings
        self.enemy_speed = enemy_speed
        self.enemy_limit = enemy_limit
