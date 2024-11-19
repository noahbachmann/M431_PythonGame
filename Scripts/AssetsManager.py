import pygame
import os

pygame.font.init()

ASSETS_PATH = os.path.join(os.path.dirname(__file__),  '..', 'Assets')

BULLSEYE_IMAGE = pygame.image.load(os.path.join(ASSETS_PATH, 'bullseye.png'))
SPACESHIP_IMAGE = pygame.image.load(os.path.join(ASSETS_PATH, 'spaceship.png'))
ENEMY_IMAGE = pygame.image.load(os.path.join(ASSETS_PATH, 'enemyspaceship.png'))
LASER_IMAGE = pygame.image.load(os.path.join(ASSETS_PATH, 'laser.png'))
LASER_BLUE_IMAGE = pygame.image.load(os.path.join(ASSETS_PATH, 'laser_blue.png'))
HEAVY_IMAGE = pygame.image.load(os.path.join(ASSETS_PATH, 'heavy.png'))
font = pygame.font.Font(os.path.join(ASSETS_PATH, 'upheavtt.ttf'), 20)