import pygame
from Timer import *
from AssetsManager import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos:tuple, health, speed, attackGroups, size:tuple = None):
        super().__init__()
        self.attackGroups = attackGroups
        self.direction = "top"
        self.speed = speed
        self.health = health
        self.atkSpeed = 1
        self.atkTimer = Timer(self.atkSpeed)
        self.heavyCd = 10
        self.heavyCdTimer = Timer(self.heavyCd)
        if size:
            self.image = pygame.transform.scale(SPACESHIP_IMAGE, size)
        else:
            self.image = SPACESHIP_IMAGE
        self.rect = self.image.get_frect(center=pos)

    def draw(self, surface):
        rotatedImage = RotateImageOfObject(self)
        surface.blit(rotatedImage, self.rect)

    def update(self, surface, dt): 
        self.rect.center += GetDirection(self.direction) * self.speed * dt

        mouse = pygame.mouse.get_pressed()
        keys = pygame.key.get_pressed()
        if (mouse[0] or keys[pygame.K_SPACE]) and not self.atkTimer.active:
            self.shoot()  
            self.atkTimer.activate()
        if self.atkTimer.active:
            self.atkTimer.update()
        if (mouse[2] or keys[pygame.K_f]) and not self.heavyCdTimer.active:
            self.heavy()
            self.heavyCdTimer.activate()
        if self.heavyCdTimer.active:
           self.heavyCdTimer.update()
        self.draw(surface)
        
    def shoot(self):
        if self.direction == "top":
            Shot(self.rect.midtop,2,200,1,self.direction,LASER_IMAGE, self.attackGroups, (4,8))
        elif self.direction == "right":
            Shot(self.rect.midright,2,200,1,self.direction,LASER_IMAGE, self.attackGroups, (4,8))
        elif self.direction == "bottom":
            Shot(self.rect.midbottom,2,200,1,self.direction,LASER_IMAGE, self.attackGroups, (4,8))
        elif self.direction == "left":
            Shot(self.rect.midleft,2,200,1,self.direction,LASER_IMAGE, self.attackGroups, (4,8))
    
    def heavy(self):
        if self.direction == "top":
            Heavy(self.rect.midtop,200,self.direction,HEAVY_IMAGE,self.attackGroups,(8,8))
        elif self.direction == "right":
            Heavy(self.rect.midright,200,self.direction,HEAVY_IMAGE,self.attackGroups,(8,8))
        elif self.direction == "bottom":
            Heavy(self.rect.midbottom,200,self.direction,HEAVY_IMAGE,self.attackGroups,(8,8))
        elif self.direction == "left":
            Heavy(self.rect.midleft,200,self.direction,HEAVY_IMAGE,self.attackGroups,(8,8))

class Shot(pygame.sprite.Sprite):
    def __init__(self, pos:tuple, damage, speed, hits, direction:str, image, groups, size:tuple = None):
        super().__init__(groups)
        self.damage = damage
        self.speed = speed      
        self.hits = hits
        self.direction = direction
        self.vectorDir = GetDirection(direction)
        self.collided_enemies = set()
        if size:
            self.image = pygame.transform.scale(image, size)
        else:
            self.image = image
        self.image = RotateImageOfObject(self)
        self.rect = self.image.get_frect(center=pos)

    def draw(self, surface):
        surface.blit(self.image, self.rect)
    
    def update(self, surface, dt):   
        self.rect.center += self.vectorDir * self.speed * dt
        self.draw(surface)

    def hit(self, enemy):
        self.hits -= 1
        self.collided_enemies.add(enemy)
        if self.hits <= 0:
            self.kill()
            del self

class Heavy(pygame.sprite.Sprite):
    def __init__(self, pos:tuple, speed, direction:str, image, groups, size:tuple = None):
        super().__init__(groups)
        self.vectorDir = GetDirection(direction)
        self.direction = direction
        self.speed = speed
        if size:
            self.image = pygame.transform.scale(image, size)
        else:
            self.image = image
        self.image = RotateImageOfObject(self)
        self.rect = self.image.get_frect(center=pos)

    def draw(self, surface):
        surface.blit(self.image, self.rect)
    
    def update(self, surface, dt):   
        self.rect.center += self.vectorDir * self.speed * dt
        self.draw(surface)
    
    def hit(self):
        self.kill()
        del self

def RotateImageOfObject(object):
        if object.direction == "top":
            return object.image 
        elif object.direction == "right":
            return pygame.transform.rotate(object.image, -90)
        elif object.direction == "bottom":
            return pygame.transform.rotate(object.image, 180)
        elif object.direction == "left":
            return pygame.transform.rotate(object.image, 90)

def GetDirection(direction:str):
        if direction == "top":
            return pygame.math.Vector2(0, -1)
        elif direction == "right":
            return pygame.math.Vector2(1, 0)
        elif direction == "bottom":
            return pygame.math.Vector2(0, 1)
        elif direction == "left":
            return pygame.math.Vector2(-1, 0)