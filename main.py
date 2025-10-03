# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *


def main():
   pygame.init()
   screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
   BLACK = (0, 0, 0)
   while True:
        for event in pygame.event.get():
             if event.type == pygame.QUIT:
                pygame.quit()
                return
        screen.fill(BLACK)
        pygame.display.flip()
   

if __name__ == "__main__":
    main()
