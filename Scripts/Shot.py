import pygame
import math
from Scripts.Timer import *
from Scripts.AssetsManager import EXPLOSION_RADIUS, Audio

class Shot(pygame.sprite.Sprite):
    def __init__(self, pos:tuple, damage, speed, hits, angle, image, groups, lifeDistance = 0, playerOffset:pygame.math.Vector2 = pygame.math.Vector2(0,0), size:tuple = None):
        super().__init__(groups)
        self.isHeavy = False
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
        self.offset = playerOffset

    def draw(self, surface):
        surface.blit(self.image, self.rect)
    
    def update(self, dt):
        if self.lifeDistance != 0:
            currentPosition = pygame.math.Vector2(self.rect.center)
            if (currentPosition - self.startPos).length() >= self.lifeDistance:
                self.kill()
        self.rect.center += self.direction * self.speed * dt

    def hit(self, enemy = None):
        self.hits -= 1
        if enemy:
            self.collidedEnemies.add(enemy)
        if self.hits <= 0:
            self.kill()
            del self

class ExplosionShot(Shot):
    def __init__(self, pos, damage, speed, hits, angle, explosionSize, image, groups, lifeDistance=0, playerOffset = pygame.math.Vector2(0, 0), size = None):
        super().__init__(pos, damage, speed, hits, angle, image, groups, lifeDistance, playerOffset, size)
        self.exploding = False
        self.collided = False
        self.isHeavy = True
        self.explosionSize = explosionSize
        self.explosionImage = EXPLOSION_RADIUS
        self.explosionPos = pygame.math.Vector2(0,0)
        self.currentSize = 4
        self.savedSize = 0

    def update(self, dt):
        if not self.exploding and self.lifeDistance != 0:
            currentPosition = pygame.math.Vector2(self.rect.center)
            if (currentPosition - self.startPos).length() >= self.lifeDistance:
                self.exploding = True
                self.explosionPos = pygame.math.Vector2(self.rect.center)
                Audio.EXPLOSION.play()
        if self.exploding:
            self.savedSize += dt * 250
            self.currentSize = int(self.savedSize) + 4
            self.image = pygame.transform.scale(self.explosionImage, (self.currentSize, self.currentSize))
            self.rect = self.image.get_frect(center = (self.explosionPos.x, self.explosionPos.y))
        else:
            self.rect.center += self.direction * self.speed * dt
        if self.currentSize > self.explosionSize:
            self.kill()

    def hit(self):
        if not self.collided:
            self.collided = True
        if not self.exploding:
            self.exploding = True
            self.explosionPos = pygame.math.Vector2(self.rect.center)
            Audio.EXPLOSION.play()