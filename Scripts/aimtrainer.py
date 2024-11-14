import pygame
import sys
import time
from Player import *
from Enemy import *
from GameWorld import GameWorld
from AssetsManager import *
    
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 640, 640
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("My Space Shooter")

clock = pygame.time.Clock()
world = GameWorld()
world.add_object(Enemy(0, 200, ENEMY_IMAGE, (64, 64)))
player = Player(WINDOW_WIDTH / 2, 500, SPACESHIP_IMAGE, (64, 64))
world.draw(screen)
player.draw(screen)
pygame.display.update()

running = True
while running:
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

    world.update(screen, dt)
    player.update(screen, dt)
    pygame.display.update()    

pygame.quit()