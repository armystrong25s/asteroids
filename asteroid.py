import pygame
from circleshape import CircleShape
from constants import ASTEROID_MAX_RADIUS

class Asteroid(CircleShape):
    containers = []
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.position = pygame.Vector2(x, y) # Use this for position
        self.radius = radius

        self.velocity = pygame.Vector2(0, 0) 

        self.add(*self.containers)

    def update(self, dt):
        self.position += self.velocity * dt

        

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (int(self.position.x), int(self.position.y)), self.radius, 2)