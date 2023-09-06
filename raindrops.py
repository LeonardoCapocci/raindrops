import sys
import pygame

from drop import Drop

class Raindrops:
    """A class to represent raindrops falling down the sky to the ground."""
    def __init__(self):
        """Initialize starting app atributes."""
        pygame.init()
        self.screen = pygame.display.set_mode((1280,720))
        self.screen_rect = self.screen.get_rect()
        self.clock = pygame.time.Clock()
        self.bg_color = (151, 204, 255)
        self.drops = pygame.sprite.Group()
    
    def run_app(self):
        """Main loop for the app."""
        while True:
            self._check_events()
            self.create_rain()
            self._update_drops()
            self._update_screen()
            
            self.clock.tick(60)
            pygame.display.flip()

    def create_rain(self):
        """Creates a row of raindrops at the top of the screen."""
        if len(self.drops) == 0:
            drop = Drop(self)
            drop_width = drop.rect.width
            current_x = drop_width * 0.5
            while current_x < (self.screen_rect.width - drop_width):
                new_drop = Drop(self)
                new_drop.rect.x = current_x
                current_x += 2 * drop_width
                self.drops.add(new_drop)

    def _update_drops(self):
        """Update the drops."""
        self.drops.update()
        self._cleanup_drops()
    
    def _cleanup_drops(self):
        """Remove drops that are off screen."""
        for drop in self.drops.copy():
            if drop.rect.y > self.screen_rect.bottom:
                self.drops.remove(drop)

    def _check_events(self):
        """Checks keyboard events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()

    def _update_screen(self):
        """Updates screen for each loop."""
        self.screen.fill(self.bg_color)
        self.drops.draw(self.screen)

if __name__ == '__main__':
    rd = Raindrops()
    rd.run_app()