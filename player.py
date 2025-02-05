import pygame

class Player:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.rotation = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = pygame.Vector2(self.x, self.y) + forward * self.radius
        b = pygame.Vector2(self.x, self.y) - forward * self.radius - right
        c = pygame.Vector2(self.x, self.y) - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, self.color, self.triangle(), 2)