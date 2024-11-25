import pygame
import sys
import time
from Settings import *
from Player import *
from HUDController import *
from EnemySpawner import *
from AssetsManager import *

class Round:
    def __init__(self, surface, screen):
        self.screen = screen  
        self.cameraSurface = surface
        screenSize = screen.get_size()
        self.offset = (screenSize[0] // 2 - WINDOW_WIDTH // 2, screenSize[1] // 2 - WINDOW_HEIGHT // 2)
        self.clock = pygame.time.Clock()
        self.allSprites = pygame.sprite.Group()
        self.hudSprites = pygame.sprite.Group()
        self.enemySprites = pygame.sprite.Group()
        self.playerShotSprites = pygame.sprite.Group()
        self.player = Player((WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2), self.offset, 6, 250, 150, 3, (self.allSprites,self.playerShotSprites), (64, 64))
        self.hudController = HUDController(self.cameraSurface, self.player, self.allSprites)
        self.enemySpawner = Spawner("normal", self.player, (self.allSprites, self.enemySprites))
        self.running = True

    def run(self):
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
                self.allSprites.update(self.cameraSurface, dt)
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