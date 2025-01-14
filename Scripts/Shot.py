import pygame
import math
from Scripts.Timer import *
from Scripts.AssetsManager import Enemy_Laser, Audio

class Shot(pygame.sprite.Sprite):
    def __init__(self, pos:tuple, damage, speed, hits, angle, image, groups, lifeDistance = 0, playerOffset:pygame.math.Vector2 = pygame.math.Vector2(0,0), size:tuple = None, hitAnimation = None):
        super().__init__(groups)
        self.isHeavy = False
        self.damage = damage
        self.speed = speed      
        self.hits = hits
        self.lifeDistance = lifeDistance
        self.isEnemy = False
        self.collided = False
        self.animationState = "idle"
        self.hitAnimation = hitAnimation
        self.frameIndex = 0
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
        if self.collided:
            self.animate(dt)
            if self.frameIndex > len(self.hitAnimation) -1:
                self.kill()
        elif self.lifeDistance != 0:
            currentPosition = pygame.math.Vector2(self.rect.center)
            if (currentPosition - self.startPos).length() >= self.lifeDistance:
                self.kill()
        if not self.collided:
            self.rect.center += self.direction * self.speed * dt

    def hit(self, enemy = None):
        if self.collided:
            return
        self.hits -= 1
        if enemy:
            self.collidedEnemies.add(enemy)
        if self.hits <= 0:
            self.collided = True
            self.frameIndex = 0
            self.animationState = "exploding"

    def animate(self, dt):
        self.frameIndex += 14*dt
        self.image = pygame.transform.scale(self.hitAnimation[int(self.frameIndex)], (26,26))

class ExplosionShot(Shot):
    def __init__(self, pos, damage, speed, hits, angle, explosionSize, image, groups, lifeDistance=0, playerOffset = pygame.math.Vector2(0, 0), size = None):
        super().__init__(pos, damage, speed, hits, angle, image, groups, lifeDistance, playerOffset, size)
        self.exploding = False
        self.collided = False
        self.isHeavy = True
        self.explosionSize = explosionSize
        self.explosionImage = Enemy_Laser.ENEMY_HEAVY_ATTACK
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