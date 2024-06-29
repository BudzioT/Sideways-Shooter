import pygame.font


class Title:
    """Rendered title"""
    def __init__(self, game, text):
        """Initialize the title"""
        # Get surface from the game
        self.surface = game.surface
        self.surface_rect = self.surface.get_rect()

        # Save game reference
        self.game = game

        # Set the font size and color
        self.font_color = (189, 189, 121)
        self.font = pygame.font.Font(None, 76)

        # Set the title rendering
        self._set_title(text)

    def _set_title(self, text):
        """Render image from a title text"""
        self.title_image = self.font.render(text, True, self.font_color,
                                            self.game.settings.bg_color)
        # Place title in the upper center of the screen
        self.title_image_rect = self.title_image.get_rect()
        self.title_image_rect.centerx = self.surface_rect.centerx
        self.title_image_rect.centery = self.surface_rect.centery - self.surface_rect.height / 2

    def draw(self):
        """Draw the renderer title"""
        # Draw the title
        self.surface.blit(self.title_image, self.title_image_rect)
