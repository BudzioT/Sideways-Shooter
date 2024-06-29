import pygame.font


class Button:
    """Button with a label"""
    def __init__(self, game, label, width=200, height=50):
        """Initialize button"""
        # Set the surface to match the game's one
