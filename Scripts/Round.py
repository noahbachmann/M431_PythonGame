import pygame
import sys
import time
from random import randint
from Settings import *
from Player import *
from HUDController import *
from EnemySpawner import *
from AssetsManager import *
from Groups import AllSprites

class Round:
    def __init__(self, surface, screen):
        self.screen = screen  
        self.cameraSurface = surface
        screenSize = screen.get_size()
        self.offset = (screenSize[0] // 2 - WINDOW_SIZE // 2, screenSize[1] // 2 - WINDOW_SIZE // 2)
        self.clock = pygame.time.Clock()
        self.allSprites = AllSprites()
        self.hudSprites = pygame.sprite.Group()
        self.enemySprites = pygame.sprite.Group()
        self.playerShotSprites = pygame.sprite.Group()
        self.collisionSprites = pygame.sprite.Group()
        self.border = []
        self.stars = []
        self.player = Player((WINDOW_SIZE // 2, WINDOW_SIZE // 2), self.offset, 6, 220, 150, 3, (self.allSprites,self.playerShotSprites), self.collisionSprites, (64, 64))
        self.hudController = HUDController(self.cameraSurface, self.player, self.allSprites)
        self.enemySpawner = Spawner("normal", self.player, (self.allSprites, self.enemySprites))
        self.running = True

    def run(self):
        self.createBackground()
        self.createBorder()
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    return -1
                if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            self.hudController.pause = not self.hudController.pause
                            continue
            
            dt = self.clock.tick() / 1000

            if self.hudController.pause:
                self.hudController.update(self.cameraSurface)
                self.drawToScreen()
                continue
        
            if not self.hudController.pause:
                self.cameraSurface.fill((7, 0, 25))
                self.collisions()
                if self.player.health <= 0:
                    self.running = False
                    return self.player.score          
                self.enemySpawner.update()
                self.allSprites.update(self.cameraSurface, dt, self.player.moveOffset)
                self.player.update(self.cameraSurface, dt)
                self.hudController.update(self.cameraSurface)
                self.drawToScreen()
        
    def collisions(self):
        for shot in self.playerShotSprites:       
            enemies = pygame.sprite.spritecollide(shot, self.enemySprites, False)
            for enemy in enemies:
                if enemy not in shot.collidedEnemies and enemy.isEnemy:
                    shot.hit(enemy)
                    enemy.hit(shot.damage)
        enemies = pygame.sprite.spritecollide(self.player, self.enemySprites, False)
        if enemies:
            self.player.hit(enemies[0].damage)
            for enemy in enemies:
                if not enemy.isEnemy:
                    enemy.hit()

    def drawToScreen(self):
        screenSize = self.screen.get_size()
        self.screen.fill((0,0,0))
        self.screen.blit(self.cameraSurface, self.cameraSurface.get_frect(center = (screenSize[0]//2,screenSize[1]//2)))
        pygame.display.update()

    def createBackground(self):
        currentPointX = currentPointY = -(MAP_SIZE//3)*1.5 + (TILE_SIZE//2)
        randomNum = randint(1, 20)
        x = 1
        while currentPointY < MAP_SIZE - ((MAP_SIZE//3)//2):
            while currentPointX < MAP_SIZE - ((MAP_SIZE//3)//2):
                if x == randomNum:
                    self.stars.append(ImageSprite((currentPointX + randint(-16,16), currentPointY + randint(-16,16)), self.allSprites, STAR_IMAGE, (32,32)))
                    randomNum = randint(4,20)
                    x = 1
                else:    
                    x += 1
                currentPointX += TILE_SIZE
            currentPointX = -(MAP_SIZE//3)*1.5 + (TILE_SIZE//2)
            currentPointY += TILE_SIZE
    
    def createBorder(self):
        currentPoint = -(MAP_SIZE//3) - (TILE_SIZE//2)
        while currentPoint < MAP_SIZE - (MAP_SIZE//3) + TILE_SIZE:
            self.border.append(BorderSprite((currentPoint, -(MAP_SIZE//3) - (TILE_SIZE//2)), (self.allSprites, self.collisionSprites), BORDER_BLOCK, (64,64)))
            self.border.append(BorderSprite((currentPoint, MAP_SIZE - (MAP_SIZE//3) + (TILE_SIZE//2)), (self.allSprites, self.collisionSprites), BORDER_BLOCK, (64,64)))
            if not (currentPoint == -(MAP_SIZE//3) - (TILE_SIZE//2) or currentPoint == MAP_SIZE - (MAP_SIZE//3) + (TILE_SIZE//2)):
                self.border.append(BorderSprite((-(MAP_SIZE//3) - (TILE_SIZE//2), currentPoint), (self.allSprites, self.collisionSprites), BORDER_BLOCK, (64,64)))
                self.border.append(BorderSprite((MAP_SIZE - (MAP_SIZE//3) + (TILE_SIZE//2), currentPoint), (self.allSprites, self.collisionSprites), BORDER_BLOCK, (64,64)))
            currentPoint += TILE_SIZE

class ImageSprite(pygame.sprite.Sprite):
    def __init__(self, pos:tuple, groups, image, size:tuple=None):
        super().__init__(groups)
        if size:
            self.image = pygame.transform.scale(image, size)
        else:
            self.image = image
        self.rect = self.image.get_frect(center=pos)
        self.offset = pygame.math.Vector2(0,0)
    
    def draw(self, surface):
        surface.blit(self.image, self.rect)

class BorderSprite(ImageSprite):
    def __init__(self, pos, groups, image, size = None):
        super().__init__(pos, groups, image, size)
        self.rotation = float(randint(1,360))
        self.savedImage = self.image
        self.image = pygame.transform.rotate(self.savedImage, self.rotation)
        if randint(1,2) == 1:
            self.rotationDir = True
        else:
            self.rotationDir = False

    def update(self, dt):
        if self.rotationDir:
            self.rotation -= 0.5
        else:
            self.rotation += 0.5
        self.image = pygame.transform.rotate(self.savedImage, self.rotation)
