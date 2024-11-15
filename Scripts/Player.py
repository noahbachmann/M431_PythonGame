import pygame
import math
from Timer import *
from AssetsManager import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos:tuple, health, speed, attackGroups, size:tuple = None):
        super().__init__()
        self.attackGroups = attackGroups
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = speed
        self.health = health
        self.damageTimer = Timer(0.5)
        self.atkSpeed = 0.5
        self.atkTimer = Timer(self.atkSpeed)
        self.heavyCd = 10
        self.heavyCdTimer = Timer(self.heavyCd)
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
        Shot(spawnPos,2,500,1,angle,LASER_IMAGE, self.attackGroups, (4,8))
    
    def heavy(self, angle):
        offset = pygame.math.Vector2(math.cos(math.radians(angle)), math.sin(math.radians(angle))) * self.rect.height / 2
        spawnPos = self.rect.center + offset
        Heavy(spawnPos,200,angle,HEAVY_IMAGE,self.attackGroups,(8,8))

    def hit(self, damage):
        if self.damageTimer.active:
            print("player hit while timer up")
            return
        self.damageTimer.activate()
        self.health -= damage
        print(f"player hit and this much hp left: {self.health}")
        if self.health <= 0:
            self.kill()
            

class Shot(pygame.sprite.Sprite):
    def __init__(self, pos:tuple, damage, speed, hits, angle, image, groups, size:tuple = None):
        super().__init__(groups)
        self.damage = damage
        self.speed = speed      
        self.hits = hits
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
        self.hits -= 1
        self.collidedEnemies.add(enemy)
        if self.hits <= 0:
            self.kill()
            del self

class Heavy(pygame.sprite.Sprite):
    def __init__(self, pos:tuple, speed, angle, image, groups, size:tuple = None):
        super().__init__(groups)
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