import pygame
import sys
import time
from Player import *
from Enemy import *
from AssetsManager import *
    
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 640, 640
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("My Space Shooter")

clock = pygame.time.Clock()

player = Player(WINDOW_WIDTH / 2, 500, SPACESHIP_IMAGE, (64, 64))
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


    player.update(screen, dt)
    pygame.display.update()    

pygame.quit()