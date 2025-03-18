import pygame
from circleshape import CircleShape
from constants import *

class Shot(CircleShape):
    containers = None

    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)
        if Shot.containers:
            self.add(Shot.containers)
        self.velocity = pygame.Vector2(0,0)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.position.x, self.position.y), self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt