import pygame
import math
from Timer import *
from AssetsManager import *
from Shot import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos:tuple, health, speed, boostStrength, boostAmount:float, attackGroups, size:tuple = None):
        super().__init__()
        self.direction = pygame.math.Vector2(0, 0)
        self.normalSpeed = speed
        self.speed = speed
        self.maxHealth = health
        self.health = health
        self.boostTank = boostAmount
        self.boostAmount = boostAmount
        self.boostStrength = boostStrength
        self.boosting = False
        self.attackGroups = attackGroups
        self.damageTimer = Timer(0.5)
        self.atkSpeed = 0.5
        self.atkDamage = 1
        self.atkTimer = Timer(self.atkSpeed)
        self.heavyCd = 10
        self.heavyCdTimer = Timer(self.heavyCd)
        self.gold = 0
        if size:
            self.image = pygame.transform.scale(SPACESHIP_IMAGE, size)
        else:
            self.image = SPACESHIP_IMAGE
        self.savedImage = self.image
        self.rect = self.image.get_frect(center=pos)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self, surface, dt): 
        mousePos = pygame.mouse.get_pos()
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
        self.rect.center += self.direction * self.speed * dt
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
        Shot(spawnPos,2,500,self.atkDamage,angle,LASER_BLUE_IMAGE, self.attackGroups,size=(4,8))
    
    def heavy(self, angle):
        offset = pygame.math.Vector2(math.cos(math.radians(angle)), math.sin(math.radians(angle))) * self.rect.height / 2
        spawnPos = self.rect.center + offset
        Heavy(spawnPos,2,200,angle,HEAVY_IMAGE,self.attackGroups,(8,8))

    def hit(self, damage):
        if self.damageTimer.active:
            print("dmg while timer up")
            return
        self.damageTimer.activate()
        self.health -= damage
        print(f"player hit and this much hp left: {self.health}")
        if self.health <= 0:
            self.kill()

    def upgrade(self, type:str, upgradesLevel):
        cost = 0
        match type:
            case "atkSpeed":
                cost = (upgradesLevel[0]+1) * 1
                if cost > self.gold or upgradesLevel[0] >= 10:
                    return
                self.atkSpeed += 5
                upgradesLevel[0] += 1
            case "atkDmg":
                cost = (upgradesLevel[1]+1) * 1
                if cost > self.gold or upgradesLevel[1] >= 10:
                    return
                self.atkDamage += 1
                upgradesLevel[1] += 1
            case "health":
                cost = (upgradesLevel[2]+1) * 1
                if cost > self.gold or upgradesLevel[2] >= 10:
                    return
                self.maxHealth += 1
                self.health += 1
                upgradesLevel[2] += 1
            case "heavyCd":
                cost = (upgradesLevel[3]+1) * 1
                if cost > self.gold or upgradesLevel[3] >= 10:
                    return
                self.heavyCd -= 0.5
                upgradesLevel[3] += 1
            case "boostTank":
                cost = (upgradesLevel[4]+1) * 1
                if cost > self.gold or upgradesLevel[4] >= 10:
                    return
                self.boostTank += 0.5
                upgradesLevel[4] += 1
            case "boostStrength":
                cost = (upgradesLevel[5]+1) * 1
                if cost > self.gold or upgradesLevel[5] >= 10:
                    return
                self.boostStrength += 10
                upgradesLevel[5] += 1
        self.gold -= cost
        print(f"Upgraded {type}")
            
                
class Heavy(pygame.sprite.Sprite):
    def __init__(self, pos:tuple, damage, speed, angle, image, groups, size:tuple = None):
        super().__init__(groups)
        self.damage = damage
        self.speed = speed
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

    def draw(self, surface):
        surface.blit(self.image, self.rect)
    
    def update(self, surface, dt):   
        self.rect.center += self.direction * self.speed * dt
        self.draw(surface)
    
    def hit(self, enemy):
        self.collidedEnemies.add(enemy)
        self.kill()
        del self