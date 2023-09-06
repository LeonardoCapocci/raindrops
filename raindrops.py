import sys
import pygame

#from drop import Drop

class Raindrops:
    """A class to represent raindrops falling down the sky to the ground"""
    def __init__(self):
        """Initialize starting app atributes"""
        pygame.init()
        self.screen = pygame.display.set_mode((1280,720))
        self.clock = pygame.time.Clock()
        self.bg_color = (151, 204, 255)
    
    def run_app(self):
        """Main loop for the app"""
        while True:
            self.screen.fill(self.bg_color)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        sys.exit()

            self.clock.tick(60)
            pygame.display.flip()


if __name__ == '__main__':
    rd = Raindrops()
    rd.run_app()