import pygame
import sys
import time
from Player import *
from HUDController import *
from EnemySpawner import *
from AssetsManager import *

def collisions():
    for shot in playerShotSprites:       
        enemies = pygame.sprite.spritecollide(shot, enemySprites, False)
        for enemy in enemies:
            if enemy not in shot.collidedEnemies and enemy.isEnemy:
                print(f"Laser {shot} hitting Enemy {enemy}")
                shot.hit(enemy)
                enemy.hit(shot.damage)
    enemies = pygame.sprite.spritecollide(player, enemySprites, False)
    if enemies:
        player.hit(enemies[0].damage)
        for enemy in enemies:
            if not enemy.isEnemy:
                enemy.hit()  
        
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 850, 850
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("My Space Shooter")

clock = pygame.time.Clock()
allSprites = pygame.sprite.Group()
enemySprites = pygame.sprite.Group()
playerShotSprites = pygame.sprite.Group()
player = Player((WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2), 6, 250, 150, 3, (allSprites,playerShotSprites), (64, 64))
hudController = HUDController(player)
enemySpawner = Spawner("normal", player, (allSprites, enemySprites))
allSprites.draw(screen)
player.draw(screen)
pygame.display.update()

running = True
while running:
    screen.fill((7, 0, 25))
    dt = clock.tick() / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            continue

    collisions()
    if player.health <= 0:
            running = False
            continue
        
    player.update(screen, dt)
    enemySpawner.update()
    allSprites.update(screen, dt)
    hudController.update(screen)
    pygame.display.update()

pygame.quit()