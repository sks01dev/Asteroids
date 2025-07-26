import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        if hasattr(self.__class__, 'containers'):
            self.add(*self.__class__.containers)

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            (255, 255, 255),            # white color
            self.position,              # center of circle
            self.radius,
            width=2                     # outline only
        )

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):

        # Always kill the original asteroid
        self.kill()

        # If it's too small to split, just end here
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # Otherwise, spawn two smaller asteroids
        random_angle = random.uniform(20, 50)

        # Create two rotated velocity vectors
        velocity1 = self.velocity.rotate(random_angle) * 1.2
        velocity2 = self.velocity.rotate(-random_angle) * 1.2

        # New radius (step down one size)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # Create the two new asteroids
        a1 = Asteroid(self.position.x, self.position.y, new_radius)
        a1.velocity = velocity1

        a2 = Asteroid(self.position.x, self.position.y, new_radius)
        a2.velocity = velocity2

