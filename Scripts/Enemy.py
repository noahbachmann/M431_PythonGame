import pygame
import math
from Shot import *
from Timer import *
from AssetsManager import LASER_IMAGE

class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos:tuple, health, damage, gold, speed, player, image, frames, groups, size:tuple = None):
        super().__init__(groups)
        self.health = health
        self.damage = damage
        self.gold = gold
        self.speed = speed
        self.player = player
        self.frames = frames
        self.frameIndex = 0
        self.animationState = "idle"
        self.angle = 0
        if size:
            self.size = size
            self.image = pygame.transform.scale(image, size)
        else:
            self.image = image
        self.savedImage = self.image
        self.rect = self.image.get_frect(center=pos)
        self.offset = player.moveOffset.copy()

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self, dt):
        self.animate(dt)
        self.directionToPlayer = (pygame.Vector2(self.player.rect.center) - pygame.Vector2(self.rect.center))
        self.image = pygame.transform.rotate(self.savedImage, -self.angle-90)
        if self.animationState == "death" and int(self.frameIndex) != 0 and int(self.frameIndex) % len(self.frames[self.animationState]) == 0:
            self.kill()
            del self
        
    def hit(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.player.gold += self.gold
            self.player.score += self.gold*5
            self.animationState = "death"
            self.frameIndex = 0
    
    def animate(self, dt):
        self.frameIndex += self.frames[self.animationState]["speed"]*dt
        if self.size:
            self.image = pygame.transform.scale(self.frames[self.animationState]["frames"][int(self.frameIndex) % len(self.frames[self.animationState])], self.size)
            self.savedImage = self.image
        else:
            self.image = self.frames[self.animationState]["frames"][int(self.frameIndex) % len(self.frames[self.animationState])]
            self.savedImage = self.image
    
    def getAngle(self):
        playerPos = pygame.Vector2(self.player.rect.center)
        return math.degrees(math.atan2(playerPos.y - self.rect.centery, playerPos.x - self.rect.centerx))

class BasicMelee(Enemy):
    def __init__(self, pos:tuple, health, damage, gold, speed, player, image, frames, groups, size:tuple = None):
        super().__init__(pos, health, damage, gold, speed, player, image, frames, groups, size)  
        self.isEnemy = True
        self.isAttacking = False
        self.atkDistance = 180
        self.atkDistancePassed = 0
        self.atkDirection = pygame.Vector2(0,0)
        self.atkTimer = Timer(0.5, func=self.attack)
        self.rechargeSpeed = 0.1
        
    def update(self, dt):
        super().update(dt)
        if self.animationState == "death":
            return
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
            if self.directionToPlayer.length() <= self.atkDistance and not self.atkTimer.active:
                self.angle = self.getAngle()
                self.atkDirection = pygame.Vector2(
                    math.cos(math.radians(self.angle)),
                    math.sin(math.radians(self.angle)) 
                    ).normalize()
                self.atkTimer.activate()
            elif self.atkTimer.active:
                self.atkTimer.update()
            else:
                self.angle = self.getAngle()
                self.rect.center += self.directionToPlayer.normalize() * self.speed * dt

    def attack(self):
        if self.isAttacking:
            self.atkDistancePassed = 0
        self.isAttacking = not self.isAttacking

class BasicShooter(Enemy):
    def __init__(self, pos:tuple, health, damage, gold, speed, atkSpeed, player, image, frames, groups, range=None, size:tuple = None):
        super().__init__(pos, health, damage, gold, speed, player, image, frames, groups, size)
        self.range = range
        self.atkSpeed = atkSpeed
        self.atkTimer = Timer(atkSpeed)
        self.isEnemy = True
    
    def update(self, dt):
        super().update(dt)
        if self.animationState == "death":
            return
        self.angle = self.getAngle()
        if not self.atkTimer.active:
            self.shoot()
            self.atkTimer.activate()
        if self.range:
            if self.directionToPlayer.length() > self.range:
                self.rect.center += self.directionToPlayer.normalize() * self.speed * dt
            else:
                self.rect.center += self.directionToPlayer.normalize() * 0
        self.atkTimer.update()

    def shoot(self):
        offset = pygame.math.Vector2(math.cos(math.radians(self.angle)), math.sin(math.radians(self.angle))) * self.rect.height / 2
        spawnPos = self.rect.center + offset
        Shot(spawnPos,self.damage,450,1,self.angle,LASER_IMAGE, self.groups(),700, self.offset.copy(), (4,8))
        
class DoubleShooter(BasicShooter):
    def __init__(self, pos: tuple, health, damage, gold, speed, atkSpeed, player, image, frames, groups, swap, range=None, size: tuple = None):
        super().__init__(pos, health, damage, gold, speed, atkSpeed, player, image, frames, groups, range, size)
        self.swap = swap
        if self.swap:
            self.right = True
        
    def shoot(self):
        sideOffset = pygame.math.Vector2(math.cos(math.radians(self.angle + 90)), math.sin(math.radians(self.angle + 90))) * (self.rect.width / 3)
        offset = pygame.math.Vector2(math.cos(math.radians(self.angle)), math.sin(math.radians(self.angle))) * self.rect.height / 2
        if not self.swap:
            Shot(self.rect.center + offset - sideOffset,self.damage,450,1,self.angle,LASER_IMAGE, self.groups(),700, self.offset.copy(), (4,8))
            Shot(self.rect.center + offset + sideOffset,self.damage,450,1,self.angle,LASER_IMAGE, self.groups(),700, self.offset.copy(), (4,8))
        else:
            if self.right:
                Shot(self.rect.center + offset + sideOffset,self.damage,450,1,self.angle,LASER_IMAGE, self.groups(),700, self.offset.copy(), (4,8))
            else:
                Shot(self.rect.center + offset - sideOffset,self.damage,450,1,self.angle,LASER_IMAGE, self.groups(),700, self.offset.copy(), (4,8))
            self.right = not self.right

class MiniBoss(DoubleShooter):
    def __init__(self, pos, health, damage, gold, speed, atkSpeed, player, image, frames, groups, swap, range=None, size: tuple = None):
        super().__init__(pos, health, damage, gold, speed, atkSpeed, player, image, frames, groups, swap, range, size)

    