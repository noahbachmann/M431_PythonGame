import pygame
from Timer import *
from AssetsManager import *

class Player:
    def __init__(self, x: float, y:float, image, size:tuple = None):
        self.direction = "top"
        self.speed = 100
        self.atkSpeed = 1
        self.atkTimer = Timer(self.atkSpeed)
        self.heavyCd = 10
        self.heavyCdTimer = Timer(self.heavyCd)
        self.shots = []
        if size:
            self.image = pygame.transform.scale(image, size)
        else:
            self.image = image
        self.rect = self.image.get_frect(center=(x, y))

    def draw(self, surface):
        rotatedImage = RotateImageOfObject(self)
        surface.blit(rotatedImage, self.rect)

    def update(self, surface, dt): 
        self.rect.center += GetDirection(self.direction) * self.speed * dt
        self.draw(surface)

        keys = pygame.mouse.get_pressed()
        if keys[0] and not self.atkTimer.active:
            self.shoot()  
            self.atkTimer.activate()
        if self.atkTimer.active:
            self.atkTimer.update()
        if keys[2] and not self.heavyCdTimer.active:
            self.heavy()
            self.heavyCdTimer.activate()
        for shot in self.shots:
            shot.update(surface, dt)
    
    def shoot(self):
        if self.direction == "top":
            self.shots.append(Shot(self.rect.midtop,self.direction,200,LASER_IMAGE,(4,8)))
        elif self.direction == "right":
            self.shots.append(Shot(self.rect.midright,self.direction,200,LASER_IMAGE,(4,8)))
        elif self.direction == "bottom":
            self.shots.append(Shot(self.rect.midbottom,self.direction,200,LASER_IMAGE,(4,8)))
        elif self.direction == "left":
            self.shots.append(Shot(self.rect.midleft,self.direction,200,LASER_IMAGE,(4,8)))
    
    def heavy(self):
        if self.direction == "top":
            self.shots.append(Heavy(self.rect.midtop,self.direction,200,HEAVY_IMAGE,(8,8)))
        elif self.direction == "right":
            self.shots.append(Heavy(self.rect.midright,self.direction,200,HEAVY_IMAGE,(8,8)))
        elif self.direction == "bottom":
            self.shots.append(Heavy(self.rect.midbottom,self.direction,200,HEAVY_IMAGE,(8,8)))
        elif self.direction == "left":
            self.shots.append(Heavy(self.rect.midleft,self.direction,200,HEAVY_IMAGE,(8,8)))

class Shot:
    def __init__(self, pos:tuple, direction:str, speed, image, size:tuple = None):
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

class Heavy:
    def __init__(self, pos:tuple, direction:str, speed, image, size:tuple = None):
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