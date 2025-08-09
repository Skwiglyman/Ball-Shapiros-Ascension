import pygame, sys
from settings import *
from Level import Level
from gameData import *
from support import *
        
class Game: 
    def __init__(self):
        pygame.event.set_allowed([pygame.QUIT, pygame.KEYDOWN])
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()

        pygame.display.set_caption("""Ball Shapiro's Ascension""")

        self.level = Level(level.layers, self.screen)


    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:

                    pygame.quit()
                    sys.exit()
                    
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:

                        pygame.quit()
                        sys.exit()
            self.screen.fill('Black')
            self.level.run()
            # debug(round(self.clock.get_fps(), 2), 10, 60)
            pygame.display.update()

            self.clock.tick(FPS)

if __name__ == '__main__':
    game = Game()
    game.run()
