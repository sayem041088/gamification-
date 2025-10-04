import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    # create the player in the middle of the screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    BLACK = (0, 0, 0)
    running = True
    while running:
        dt = clock.tick(60) / 1000.0  # delta time

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # draw loop
        screen.fill(BLACK)
        player.draw(screen)  # draw player each frame
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()