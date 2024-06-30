class Settings:
    """Settings of the game"""
    def __init__(self, size, spaceship_speed_x=2.5, spaceship_speed_y=2,
                 sp_bullet_width=15, sp_bullet_height=3, sp_bullet_speed=3,
                 sp_bullet_limit=5, enemy_speed=1, enemy_limit=5, spaceships_limit=3,
                 enemy_bullet_limit=2, enemy_bullet_speed=2,
                 enemy_bullet_width=10, enemy_bullet_height=3, bg_color=(32, 57, 61),
                 earn_points=5, powerup_speed_x=3, powerup_speed_y=4):
        """Initialize settings"""
        # General settings
        self.window_width = size[0]
        self.window_height = size[1]
        self.bg_color = bg_color
        self.earn_points = earn_points

        # General init settings
        self.earn_points_init = earn_points

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

        # Enemy init settings
        self.enemy_init_speed = enemy_speed
        self.enemy_init_limit = enemy_limit

        # Enemy bullet settings
        self.enemy_bullet_color = (30, 250, 74)
        self.enemy_bullet_limit = enemy_bullet_limit
        self.enemy_bullet_speed = enemy_bullet_speed
        self.enemy_bullet_height, self.enemy_bullet_width = (
            enemy_bullet_height, enemy_bullet_width)

        # Enemy bullet init settings
        self.enemy_bullet_init_limit = enemy_bullet_limit
        self.enemy_bullet_init_speed = enemy_bullet_speed

        # PowerUps settings
        self.powerup_speed_x = powerup_speed_x
        self.powerup_speed_y = powerup_speed_y

        # PowerUps init settings
        self.powerup_init_speed_x = powerup_speed_x
        self.powerup_init_speed_y = powerup_speed_y

    def increase_diff(self, score):
        """Change difficulty depending on the score"""
        if score > 0:
            # If score is multiply of 100 but not 1000 and 5000
            if (score % 100 == 0) and (score % 1000 != 0) and (score % 5000 != 0):
                # Increase enemy limit by 1
                self.enemy_limit += 1
                # Earn more points
                self.earn_points += 3

            # If score is multiply of 1000 and not 5000
            elif (score % 1000 == 0) and (score % 5000 != 0):
                # Increase enemy bullets limit by 1
                self.enemy_bullet_limit += 1
                # Earn more points
                self.earn_points += 7

            # If score is multiply of 5000
            elif score % 5000 == 0:
                # Increase enemy speed by 1 pixel
                self.enemy_speed += 1
                # Increase enemy bullet speed by 1 pixel
                self.enemy_bullet_speed += 1
                # Earn more points
                self.earn_points += 15

    def reset_settings(self):
        """Reset changed settings"""
        # Reset enemy settings
        self.enemy_limit = self.enemy_init_limit
        self.enemy_speed = self.enemy_init_speed

        # Reset enemy bullet settings
        self.enemy_bullet_limit = self.enemy_bullet_init_limit
        self.enemy_bullet_speed = self.enemy_bullet_init_speed

        # Points settings
        self.earn_points = self.earn_points_init
