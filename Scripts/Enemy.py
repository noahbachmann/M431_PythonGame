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
        self.angle = 0
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
            self.player.score += self.gold*5
            self.kill()
            del self
    
    def getAngle(self):
        playerPos = pygame.Vector2(self.player.rect.center)
        return math.degrees(math.atan2(playerPos.y - self.rect.centery, playerPos.x - self.rect.centerx))

class BasicMelee(Enemy):
    def __init__(self, pos:tuple, health, damage, gold, speed, player, image, groups, size:tuple = None):
        super().__init__(pos, health, damage, gold, speed, player, image, groups, size)  
        self.isEnemy = True
        self.isAttacking = False
        self.atkDistance = 180
        self.atkDistancePassed = 0
        self.atkDirection = pygame.Vector2(0,0)
        self.atkTimer = Timer(0.5, func=self.attack)
        self.rechargeSpeed = 0.1
        
    def update(self, surface, dt):
        directionToPlayer = (pygame.Vector2(self.player.rect.center) - pygame.Vector2(self.rect.center))
        if self.isAttacking:
            if self.atkDistancePassed >= self.atkDistance * 1.5:
                if not self.atkTimer.active:
                    #self.angle = 0
                    self.atkTimer.activate()
                else:
                    self.atkTimer.update()
                #targetAngle = self.getAngle()
                #self.angle += (targetAngle - self.angle) / 500 
                #self.image = pygame.transform.rotate(self.savedImage, -self.angle-90)
                self.rect.center += self.atkDirection * self.speed * self.rechargeSpeed * dt
                if self.rechargeSpeed < 0.8:
                    self.rechargeSpeed += 0.04
            else:
                self.rect.center += self.atkDirection * self.speed * 5 * dt
                self.atkDistancePassed += self.atkDirection.length() * self.speed * 5 * dt
        else:
            self.angle = self.getAngle()
            if directionToPlayer.length() <= self.atkDistance and not self.atkTimer.active:
                self.image = pygame.transform.rotate(self.savedImage, -self.angle-90)
                self.atkDirection = pygame.Vector2(
                    math.cos(math.radians(self.angle)),
                    math.sin(math.radians(self.angle)) 
                    ).normalize()
                self.atkTimer.activate()
            elif self.atkTimer.active:
                self.atkTimer.update()
            else:
                self.image = pygame.transform.rotate(self.savedImage, -self.angle-90)
                self.rect.center += directionToPlayer.normalize() * self.speed * dt
        
        self.draw(surface) 

    def attack(self):
        if self.isAttacking:
            self.atkDistancePassed = 0
        self.isAttacking = not self.isAttacking

class BasicShooter(Enemy):
    def __init__(self, pos:tuple, health, damage, gold, speed, atkSpeed, player, image, groups, range=None, size:tuple = None):
        super().__init__(pos, health, damage, gold, speed, player, image, groups, size)
        self.range = range
        self.atkSpeed = atkSpeed
        self.atkTimer = Timer(atkSpeed)
        self.isEnemy = True
    
    def update(self, surface, dt):
        directionToPlayer = pygame.Vector2(self.player.rect.center)-pygame.Vector2(self.rect.center)
        self.angle = self.getAngle()
        self.image = pygame.transform.rotate(self.savedImage, -self.angle-90)
        if not self.atkTimer.active:
            self.shoot(self.angle)
            self.atkTimer.activate()
        if self.range:
            if directionToPlayer.length() > self.range:
                self.rect.center += directionToPlayer.normalize() * self.speed * dt
            else:
                self.rect.center += directionToPlayer.normalize() * 0
        self.atkTimer.update()
        self.draw(surface)

    def shoot(self, angle):
        offset = pygame.math.Vector2(math.cos(math.radians(angle)), math.sin(math.radians(angle))) * self.rect.height / 2
        spawnPos = self.rect.center + offset
        Shot(spawnPos,self.damage,450,1,angle,LASER_IMAGE, self.groups(),700, (4,8))         