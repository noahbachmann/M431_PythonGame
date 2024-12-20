import pygame
import math
from Scripts.Shot import *
from Scripts.Timer import *
from Scripts.AssetsManager import Enemy_Laser, Audio, Enemy_Explosion

class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos:tuple, health, damage, gold, speed, player, image, frames, groups, rotationSpeed = 0, size:tuple = None):
        super().__init__(groups)
        self.health = health
        self.damage = damage
        self.gold = gold
        self.speed = speed
        self.rotationSpeed = rotationSpeed
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
        if not self.animationState == "death":
            if self.rotationSpeed != 0:
                targetAngle = self.getAngle()
                angleDiff = (targetAngle - self.angle) % 360
                if angleDiff > 180:
                    angleDiff -= 360
                maxStep = self.rotationSpeed * dt
                self.angle += max(-maxStep, min(maxStep, angleDiff))
                self.angle %= 360
                radians = math.radians(self.angle)
                self.directionToPlayer = pygame.Vector2(math.cos(radians), math.sin(radians))
            else:
                self.angle = self.getAngle()
                self.directionToPlayer = pygame.Vector2(self.player.rect.center) - pygame.Vector2(self.rect.center)
            self.image = pygame.transform.rotate(self.savedImage, -self.angle-90)
        elif int(self.frameIndex) != 0 and int(self.frameIndex) % len(self.frames[self.animationState]["frames"]) == len(self.frames[self.animationState]["frames"]) - 1:
            self.kill()
            del self
        
    def hit(self, damage):
        if self.animationState == "death":
            return
        self.health -= damage
        if self.health <= 0:
            self.player.gold += self.gold
            self.player.score += self.gold*50
            self.animationState = "death"
            self.frameIndex = 0
            Audio.ENEMY_DEATH.play()
    
    def animate(self, dt):
        self.frameIndex += self.frames[self.animationState]["speed"]*dt
        if self.size:
            self.image = pygame.transform.scale(self.frames[self.animationState]["frames"][int(self.frameIndex) % len(self.frames[self.animationState]["frames"])], self.size)
            self.savedImage = self.image
        else:
            self.image = self.frames[self.animationState]["frames"][int(self.frameIndex) % len(self.frames[self.animationState]["frames"])]
            self.savedImage = self.image
    
    def getAngle(self):
        playerPos = pygame.Vector2(self.player.rect.center)
        return math.degrees(math.atan2(playerPos.y - self.rect.centery, playerPos.x - self.rect.centerx))

class BasicMelee(Enemy):
    def __init__(self, pos:tuple, health, damage, gold, speed, player, image, frames, groups, rotationSpeed, size:tuple = None):
        super().__init__(pos, health, damage, gold, speed, player, image, frames, groups, rotationSpeed, size)  
        self.isEnemy = True
        self.isAttacking = False
        self.atkDistance = 180
        self.atkDistancePassed = 0
        self.atkDirection = pygame.Vector2(0,0)
        self.atkTimer = Timer(0.5, func=self.attack)
        self.rechargeSpeed = 0.1
        
    def update(self, dt):
        self.animate(dt)
        if self.animationState == "death":
            if int(self.frameIndex) != 0 and int(self.frameIndex) % len(self.frames[self.animationState]["frames"]) == 0:
                self.kill()
                del self
            return
        self.directionToPlayer = (pygame.Vector2(self.player.rect.center) - pygame.Vector2(self.rect.center))
        self.image = pygame.transform.rotate(self.savedImage, -self.angle-90)
        if self.isAttacking:
            if self.atkDistancePassed >= self.atkDistance * 1.5:
                if not self.atkTimer.active:
                    self.atkTimer.activate()
                else:
                    self.atkTimer.update()
                self.rect.center += self.atkDirection * self.speed * self.rechargeSpeed * dt
                if self.rechargeSpeed < 0.8:
                    self.rechargeSpeed += 0.04
            else:
                if self.atkDistancePassed == 0:
                    Audio.ENEMY_BOOST.play()
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
                self.animationState = "attack"
            elif self.atkTimer.active:
                self.atkTimer.update()
            else:
                self.angle = self.getAngle()
                self.rect.center += self.directionToPlayer.normalize() * self.speed * dt

    def attack(self):
        if self.isAttacking:
            self.atkDistancePassed = 0
        self.isAttacking = not self.isAttacking
        if not self.isAttacking:
            self.animationState = "idle"

class BasicShooter(Enemy):
    def __init__(self, pos:tuple, health, damage, gold, speed, atkSpeed, player, image, frames, groups, range=None, rotationSpeed = 0, size:tuple = None):
        super().__init__(pos, health, damage, gold, speed, player, image, frames, groups, rotationSpeed, size)
        self.range = range
        self.atkSpeed = atkSpeed
        self.atkTimer = Timer(atkSpeed, True, True, self.shoot)
        self.isEnemy = True
    
    def update(self, dt):
        super().update(dt)
        if self.animationState == "death":
            return
        if self.range:
            if (pygame.Vector2(self.player.rect.center) - pygame.Vector2(self.rect.center)).length() > self.range:
                self.rect.center += self.directionToPlayer.normalize() * self.speed * dt
            else:
                self.rect.center += self.directionToPlayer.normalize() * 0
        self.atkTimer.update()

    def shoot(self):
        offset = pygame.math.Vector2(math.cos(math.radians(self.angle)), math.sin(math.radians(self.angle))) * self.rect.height / 2
        spawnPos = self.rect.center + offset
        Shot(spawnPos,self.damage,450,1,self.angle,Enemy_Laser.ENEMY_LASER_1, self.groups(),700, self.offset.copy(), (7,14), Enemy_Laser.animationArray_laser_explosion)
        
class DoubleShooter(BasicShooter):
    def __init__(self, pos: tuple, health, damage, gold, speed, atkSpeed, player, image, frames, groups, swap, range=None, rotationSpeed = 0, size: tuple = None):
        super().__init__(pos, health, damage, gold, speed, atkSpeed, player, image, frames, groups, range, rotationSpeed, size)
        self.swap = swap
        if self.swap:
            self.right = True
        
    def shoot(self):
        sideOffset = pygame.math.Vector2(math.cos(math.radians(self.angle + 90)), math.sin(math.radians(self.angle + 90))) * (self.rect.width / 3)
        offset = pygame.math.Vector2(math.cos(math.radians(self.angle)), math.sin(math.radians(self.angle))) * self.rect.height / 2
        if not self.swap:
            Shot(self.rect.center + offset - sideOffset,self.damage,450,1,self.angle,Enemy_Laser.ENEMY_LASER_1, self.groups(),700, self.offset.copy(), (7,14), Enemy_Laser.animationArray_laser_explosion)
            Shot(self.rect.center + offset + sideOffset,self.damage,450,1,self.angle,Enemy_Laser.ENEMY_LASER_1, self.groups(),700, self.offset.copy(), (7,14), Enemy_Laser.animationArray_laser_explosion)
        else:
            if self.right:
                Shot(self.rect.center + offset + sideOffset,self.damage,450,1,self.angle,Enemy_Laser.ENEMY_LASER_1, self.groups(),700, self.offset.copy(), (7,14), Enemy_Laser.animationArray_laser_explosion)
            else:
                Shot(self.rect.center + offset - sideOffset,self.damage,450,1,self.angle,Enemy_Laser.ENEMY_LASER_1, self.groups(),700, self.offset.copy(), (7,14), Enemy_Laser.animationArray_laser_explosion)
            self.right = not self.right

class MiniBoss(DoubleShooter):
    def __init__(self, pos, health, damage, gold, speed, atkSpeed, player, image, frames, groups, swap, range=None, rotationSpeed = 0, size: tuple = None):
        super().__init__(pos, health, damage, gold, speed, atkSpeed, player, image, frames, groups, swap, range, rotationSpeed, size)
        self.heavyTimer = Timer(5, True, True, self.heavyShoot)

    def update(self,dt):
        super().update(dt)
        self.heavyTimer.update()

    def heavyShoot(self):
        offset = pygame.math.Vector2(math.cos(math.radians(self.angle)), math.sin(math.radians(self.angle))) * self.rect.height / 2
        spawnPos = self.rect.center + offset
        ExplosionShot(spawnPos,self.damage,450,1,self.angle,128,Enemy_Laser.ENEMY_HEAVY_LASER, self.groups(), 300, self.offset.copy(), (9,14))
