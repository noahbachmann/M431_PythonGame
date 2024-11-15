import pygame
import sys
import time
from Player import *
from Enemy import *
from EnemySpawner import *
from AssetsManager import *

def collisions():
    for laser in laserSprites:       
        enemies = pygame.sprite.spritecollide(laser, enemySprites, False)
        for enemy in enemies:
            if enemy not in laser.collided_enemies:
                print(f"Laser {laser} hitting Enemy {enemy}")
                laser.hit(enemy)
                enemy.hit(laser.damage)
    playerCol = pygame.sprite.spritecollide(player, enemySprites, False)
    if playerCol:
        player.hit(playerCol[0].damage)
        
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 640, 640
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("My Space Shooter")

clock = pygame.time.Clock()
allSprites = pygame.sprite.Group()
enemySprites = pygame.sprite.Group()
laserSprites = pygame.sprite.Group()
player = Player((WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2), 6, 150, (allSprites,laserSprites), (64, 64))
enemySpawner = Spawner("normal", (allSprites, enemySprites))
allSprites.draw(screen)
player.draw(screen)
pygame.display.update()

running = True
while running:
    screen.fill((0, 0, 0))
    dt = clock.tick() / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            continue
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player.direction = "top"
            elif event.key == pygame.K_d:
                player.direction = "right"
            elif event.key == pygame.K_s:
                player.direction = "bottom"
            elif event.key == pygame.K_a:
                player.direction = "left"

    collisions()
    if player.health <= 0:
            running = False
            continue
    enemySpawner.update()
    allSprites.update(screen, dt)
    player.update(screen, dt)
    pygame.display.update()    

pygame.quit()