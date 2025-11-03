from circleshape import CircleShape
import pygame
import random

from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "red", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        random_angle = self.velocity.rotate(random.uniform(20, 50))
        random_angle2 = self.velocity.rotate(-random.uniform(20, 50))
        radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, radius)
        asteroid1.velocity = random_angle * 1.2
        asteroid2.velocity = random_angle2 * 1.2
