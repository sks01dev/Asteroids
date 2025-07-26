from circleshape import CircleShape
import pygame   
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y, direction):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = pygame.Vector2(0, 1).rotate(direction) * PLAYER_SHOOT_SPEED
        if hasattr(self.__class__, 'containers'):
            self.add(*self.__class__.containers)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt
