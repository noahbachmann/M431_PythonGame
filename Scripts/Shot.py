import pygame
import math
from Timer import *

class Shot(pygame.sprite.Sprite):
    def __init__(self, pos:tuple, damage, speed, hits, angle, image, groups, lifeDistance = 0, size:tuple = None):
        super().__init__(groups)
        self.damage = damage
        self.speed = speed      
        self.hits = hits
        self.lifeDistance = lifeDistance
        self.isEnemy = False
        self.direction = pygame.math.Vector2(
            math.cos(math.radians(angle)), 
            math.sin(math.radians(angle))
        ).normalize()
        self.collidedEnemies = set()
        if size:
            self.image = pygame.transform.scale(image, size)
        else:
            self.image = image
        self.image = pygame.transform.rotate(self.image, -angle-90)
        self.rect = self.image.get_frect(center=pos)
        self.startPos = self.rect.center

    def draw(self, surface):
        surface.blit(self.image, self.rect)
    
    def update(self, surface, dt):
        if self.lifeDistance != 0:
            currentPosition = pygame.math.Vector2(self.rect.center)
            if (currentPosition - self.startPos).length() >= self.lifeDistance:
                self.kill()
        self.rect.center += self.direction * self.speed * dt
        self.draw(surface)

    def hit(self, enemy = None):
        self.hits -= 1
        if enemy:
            self.collidedEnemies.add(enemy)
        if self.hits <= 0:
            self.kill()
            del self