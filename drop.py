import pygame
from pygame.sprite import Sprite

class Drop(Sprite):
    """A class to represent a single raindrop."""
    def __init__(self, game):
        """Initialize raindrop attributes and starting position."""
        super().__init__()
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        self.image = pygame.image.load('drop.bmp')
        self.image = pygame.transform.scale(self.image, (60, 100))
        self.rect = self.image.get_rect()

        self.rect.x = 0
        self.rect.y = -self.rect.height

        self.y = float(self.rect.y)

    def update(self):
        """Updates raindrop positions."""
        self.rect.y += 7