import pygame
import sys
import time
from GameObject import GameObject
from GameWorld import GameWorld
from AssetsManager import BULLSEYE_IMAGE as bullseye
    
pygame.init()
# Set the size of the game window
WINDOW_SIZE = (800, 600)
screen = pygame.display.set_mode(WINDOW_SIZE)
# Set the title of the game window
pygame.display.set_caption("My Point and Click Adventure Game")

world = GameWorld()
world.add_object(GameObject(100, 200, bullseye))
world.draw(screen)
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()