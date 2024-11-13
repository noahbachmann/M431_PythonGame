import pygame
import os

ASSETS_PATH = os.path.join(os.path.dirname(__file__),  '..', 'Assets')

BULLSEYE_IMAGE = pygame.image.load(os.path.join(ASSETS_PATH, 'bullseye.png'))