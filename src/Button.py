import pygame.font


class Button:
    """Button with a label"""
    def __init__(self, game, label, width=200, height=50, button_color=(40, 199, 119),
                 font_color=(48, 48, 43), center=0):
        """Initialize button"""
        # Set the surface to match the game's one
        self.surface = game.surface
        self.surface_rect = self.surface.get_rect()

        # Set the dimensions and properties of the button
        self.width, self.height = width, height
        self.button_color = button_color
        self.font_color = font_color
        self.font = pygame.font.Font(None, 48)

        # Make Button's rect, center it
        self.rect = pygame.Rect(0, 0, width, height)
        if center == 0:
            self.rect.center = self.surface_rect.center
        else:
            self.rect.center = center
            self.rect.centery = self.surface_rect.centery

        # Set label
        self._set_label(label)

    def _set_label(self, label):
        """Set label of the button, render it"""
        # Create image from the label
        self.label_image = self.font.render(label, True, self.font_color,
                                            self.button_color)
        # Place it in center of the surface
        self.label_image_rect = self.label_image.get_rect()
        self.label_image_rect.center = self.rect.center

    def draw_button(self):
        """Draw the button with a message"""
        # Draw button's background
        self.surface.fill(self.button_color, self.rect)
        # Draw the message
        self.surface.blit(self.label_image, self.label_image_rect)
