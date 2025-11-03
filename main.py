import pygame
from asteroidfield import AsteroidField
from constants import *
from player import Player
from asteroid import Asteroid
import sys


def main():
    pygame.init()
    frames = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawble = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawble)
    Player.containers = (updatable, drawble)
    AsteroidField.containers = updatable
    field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)
        for obj in asteroids:
            if obj.collision(player):
                print("Game over!")
                sys.exit()
        screen.fill("black")
        for obj in drawble:
            obj.draw(screen)
        pygame.display.flip()

        dt = frames.tick(60) / 1000


if __name__ == "__main__":
    main()
