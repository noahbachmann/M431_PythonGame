import pygame
import math
from Scripts.Timer import *
from Scripts.AssetsManager import *
from Scripts.Shot import *
from Scripts.Settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos:tuple, camOffset:tuple, health, speed, boostStrength, boostAmount:float, attackGroups, collisionSprites, size:tuple = None):
        super().__init__()
        self.camOffset = camOffset
        self.moveOffset = pygame.math.Vector2(0,0)
        self.direction = pygame.math.Vector2(0,0)
        self.normalSpeed = speed
        self.speed = speed
        self.maxHealth = health
        self.health = health
        self.boostTank = boostAmount
        self.boostAmount = boostAmount
        self.boostStrength = boostStrength
        self.boosting = False
        self.attackGroups = attackGroups
        self.collisionSprites = collisionSprites
        self.damageTimer = Timer(0.5)
        self.atkSpeed = 0.5
        self.atkDamage = 1
        self.atkTimer = Timer(self.atkSpeed)
        self.heavyCd = 8
        self.heavyCdTimer = Timer(self.heavyCd)
        self.gold = 0
        self.score = 0
        if size:
            self.image = pygame.transform.scale(Sunset.SUNSET, size)
        else:
            self.image = Sunset.SUNSET
        self.savedImage = self.image
        self.rect = self.image.get_frect(center=pos)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self, surface, dt): 
        mousePos = pygame.mouse.get_pos()
        mousePos = (mousePos[0] - self.camOffset[0], mousePos[1] - self.camOffset[1])
        mouse = pygame.mouse.get_pressed()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LSHIFT]:
            if not self.boosting and self.boostAmount > 0:
                self.boosting = True
        elif self.boosting:
            self.boosting = False
            self.speed = self.normalSpeed
        if self.boosting:
            self.boostAmount -= dt
            if self.speed == self.normalSpeed and self.boostAmount > 0:
                self.speed += self.boostStrength
        elif self.boostAmount < self.boostTank:
            if self.boostAmount + dt > self.boostTank:
                self.boostAmount = self.boostTank
            else:
                self.boostAmount += dt
        if self.boostAmount <= 0:
            self.boosting = False
            self.speed = self.normalSpeed
        self.direction.x = int(keys[pygame.K_d]) - int(keys[pygame.K_a])
        self.direction.y = int(keys[pygame.K_s]) - int(keys[pygame.K_w])
        angle = math.degrees(math.atan2(mousePos[1] - self.rect.centery, mousePos[0] - self.rect.centerx))
        self.image = pygame.transform.rotate(self.savedImage, -angle-90)
        if self.direction.length() > 0:
            self.direction = self.direction.normalize()
        check:pygame.math.Vector2 = self.moveOffset + (self.direction * self.speed * dt)
        halfSize = MAP_SIZE // 2 - TILE_SIZE // 2
        if -halfSize <= check.x <= halfSize:
            self.moveOffset.x = check.x
        if -halfSize <= check.y <= halfSize:
            self.moveOffset.y = check.y
        self.rect = self.image.get_frect(center=self.rect.center)
        if (mouse[0] or keys[pygame.K_SPACE]) and not self.atkTimer.active:
            self.shoot(angle)  
            self.atkTimer.activate()
        if (mouse[2] or keys[pygame.K_f]) and not self.heavyCdTimer.active:
            self.heavy(angle)
            self.heavyCdTimer.activate()       
        self.atkTimer.update()
        self.heavyCdTimer.update()
        self.damageTimer.update()
        self.draw(surface)
        
    def shoot(self, angle):
        offset = pygame.math.Vector2(math.cos(math.radians(angle)), math.sin(math.radians(angle))) * self.rect.height / 2
        spawnPos = self.rect.center + offset
        Shot(spawnPos,self.atkDamage,500,1,angle,LASER_BLUE_IMAGE, self.attackGroups, playerOffset=self.moveOffset.copy(), size=(4,8))
        Audio.LASER_HIGH.play()

    def heavy(self, angle):
        offset = pygame.math.Vector2(math.cos(math.radians(angle)), math.sin(math.radians(angle))) * self.rect.height / 2
        spawnPos = self.rect.center + offset
        Heavy(spawnPos,2,200,angle,128,HEAVY_IMAGE, EXPLOSION_RADIUS, self.attackGroups, self.moveOffset.copy(), (8,8))

    def hit(self, damage):
        if self.damageTimer.active:
            return
        self.damageTimer.activate()
        self.health -= damage
        Audio.PLAYER_DAMAGE.play()           

    def upgrade(self, type:str, upgradesLevel):
        cost = 0
        match type:
            case "atkSpeed":
                cost = ((upgradesLevel[0]*25) + 50)
                if cost > self.gold or upgradesLevel[0] >= 10:
                    return
                self.atkSpeed += 5
                upgradesLevel[0] += 1
            case "atkDmg":
                cost = ((upgradesLevel[1]*50)+100)
                if cost > self.gold or upgradesLevel[1] >= 10:
                    return
                self.atkDamage += 1
                upgradesLevel[1] += 1
            case "health":
                cost = ((upgradesLevel[2]*50)+100)
                if cost > self.gold or upgradesLevel[2] >= 10:
                    return
                self.maxHealth += 1
                self.health += 1
                upgradesLevel[2] += 1
            case "heavyCd":
                cost = ((upgradesLevel[3]*15)+30)
                if cost > self.gold or upgradesLevel[3] >= 10:
                    return
                self.heavyCd -= 0.5
                upgradesLevel[3] += 1
            case "boostTank":
                cost = ((upgradesLevel[4]*25)+50)
                if cost > self.gold or upgradesLevel[4] >= 10:
                    return
                self.boostTank += 0.5
                upgradesLevel[4] += 1
            case "boostStrength":
                cost = ((upgradesLevel[5]*50)+100)
                if cost > self.gold or upgradesLevel[5] >= 10:
                    return
                self.boostStrength += 10
                upgradesLevel[5] += 1
        self.gold -= cost
        Audio.COIN_UP.play()
            
                
class Heavy(pygame.sprite.Sprite):
    def __init__(self, pos:tuple, damage, speed, angle, explosionSize, image, explosionImage, groups, playerOffset:pygame.math.Vector2 = pygame.math.Vector2(0,0), size:tuple = None):
        super().__init__(groups)
        self.isHeavy = True
        self.exploding = False
        self.damage = damage
        self.speed = speed
        self.direction = pygame.math.Vector2(
            math.cos(math.radians(angle)), 
            math.sin(math.radians(angle))
        ).normalize()
        self.explosionSize = explosionSize
        self.explosionImage = explosionImage
        self.explosionPos:pygame.math.Vector2 = pygame.math.Vector2(0,0)
        self.currentSize = 4
        self.savedSize = 0
        self.collidedEnemies = set()
        if size:
            self.image = pygame.transform.scale(image, size)
        else:
            self.image = image
        self.image = pygame.transform.rotate(self.image, -angle-90)
        self.rect = self.image.get_frect(center=pos)
        self.offset = playerOffset

    def draw(self, surface):
        surface.blit(self.image, self.rect)
    
    def update(self, dt):  
        if self.exploding:
            self.savedSize += dt * 200
            self.currentSize = int(self.savedSize) + 4
            self.image = pygame.transform.scale(self.explosionImage, (self.currentSize, self.currentSize))
            self.rect = self.image.get_frect(center = (self.explosionPos.x, self.explosionPos.y))
        else:
            self.rect.center += self.direction * self.speed * dt
        if self.currentSize > self.explosionSize:
            self.kill()
    
    def hit(self, enemy):
        self.collidedEnemies.add(enemy)
        if not self.exploding:
            self.exploding = True
            self.explosionPos = pygame.math.Vector2(self.rect.center)
            Audio.EXPLOSION.play()