import pygame
from constants import PLAYER_RADIUS
from circleshape import CircleShape


class Player(CircleShape):
    def __init__(self, x, y):
        # call parent constructor with position + radius
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0  # angle in degrees

    def triangle(self):
        # math for the points of the triangle
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5

        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        # draw a white triangle using the points from triangle()
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)

    def update(self, dt):
        # for now, player doesn't move yet
        pass