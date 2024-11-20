import pygame
import math
from Shot import *
from Timer import *
from AssetsManager import LASER_IMAGE

class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos:tuple, health, damage, gold, speed, player, image, groups, size:tuple = None):
        super().__init__(groups)
        self.health = health
        self.damage = damage
        self.gold = gold
        self.speed = speed
        self.player = player
        if size:
            self.image = pygame.transform.scale(image, size)
        else:
            self.image = image
        self.savedImage = self.image
        self.rect = self.image.get_frect(center=pos)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def hit(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.player.gold += self.gold
            self.kill()
            del self

class BasicMelee(Enemy):
    def __init__(self, pos:tuple, health, damage, gold, speed, player, image, groups, size:tuple = None):
        super().__init__(pos, health, damage, gold, speed, player, image, groups, size)  
        self.isEnemy = True
    
    def update(self, surface, dt):
        playerPos = pygame.Vector2(self.player.rect.center)
        angle = math.degrees(math.atan2(playerPos.y - self.rect.centery, playerPos.x - self.rect.centerx))
        self.image = pygame.transform.rotate(self.savedImage, -angle-90)
        self.rect.center += (playerPos - pygame.Vector2(self.rect.center)).normalize() * self.speed * dt
        self.draw(surface)  

class BasicShooter(Enemy):
    def __init__(self, pos:tuple, health, damage, gold, speed, atkSpeed, player, image, groups, range=None, size:tuple = None):
        super().__init__(pos, health, damage, gold, speed, player, image, groups, size)
        self.range = range
        self.atkSpeed = atkSpeed
        self.atkTimer = Timer(atkSpeed)
        self.isEnemy = True
    
    def update(self, surface, dt):
        playerPos = pygame.Vector2(self.player.rect.center)
        directionToPlayer = playerPos-pygame.Vector2(self.rect.center)
        distanceToPlayer = directionToPlayer.length()
        angle = math.degrees(math.atan2(playerPos.y - self.rect.centery, playerPos.x - self.rect.centerx))
        self.image = pygame.transform.rotate(self.savedImage, -angle-90)
        if not self.atkTimer.active:
            self.shoot(angle)
            self.atkTimer.activate()
        if self.range:
            if distanceToPlayer > self.range:
                self.rect.center += directionToPlayer.normalize() * self.speed * dt
            else:
                self.rect.center += directionToPlayer.normalize() * 0
        self.atkTimer.update()
        self.draw(surface)

    def shoot(self, angle):
        offset = pygame.math.Vector2(math.cos(math.radians(angle)), math.sin(math.radians(angle))) * self.rect.height / 2
        spawnPos = self.rect.center + offset
        Shot(spawnPos,self.damage,450,1,angle,LASER_IMAGE, self.groups(),700, (4,8))         