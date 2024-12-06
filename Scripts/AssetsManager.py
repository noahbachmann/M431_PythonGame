import pygame
import os
import sys

pygame.font.init()

if getattr(sys, 'frozen', False):
    BASE_PATH = sys._MEIPASS
else:
    BASE_PATH = os.path.join(os.path.dirname(__file__), '..')

ASSETS_PATH = os.path.join(BASE_PATH, 'Assets')

BULLSEYE_IMAGE = pygame.image.load(os.path.join(ASSETS_PATH, 'bullseye.png'))
SPACESHIP_IMAGE = pygame.image.load(os.path.join(ASSETS_PATH, 'spaceship.png'))
ENEMY_IMAGE = pygame.image.load(os.path.join(ASSETS_PATH, 'enemyspaceship.png'))
LASER_IMAGE = pygame.image.load(os.path.join(ASSETS_PATH, 'laser.png'))
LASER_BLUE_IMAGE = pygame.image.load(os.path.join(ASSETS_PATH, 'laser_blue.png'))
HEAVY_IMAGE = pygame.image.load(os.path.join(ASSETS_PATH, 'heavy.png'))
STAR_IMAGE = pygame.image.load(os.path.join(ASSETS_PATH, 'star.png'))
BORDER_BLOCK = pygame.image.load(os.path.join(ASSETS_PATH, 'meteor.png'))
EXPLOSION_RADIUS = pygame.image.load(os.path.join(ASSETS_PATH, 'explosionRadius.png'))
class UI_Assets:
    BUTTON_IMAGE = pygame.image.load(os.path.join(ASSETS_PATH, 'button.png'))
    BUTTON_32x32 = pygame.image.load(os.path.join(ASSETS_PATH, 'button_32x32.png'))
    BUTTON_64x32 = pygame.image.load(os.path.join(ASSETS_PATH, 'button_64x32.png'))
    ICON_UPGRADE = pygame.image.load(os.path.join(ASSETS_PATH, 'icon_upgrade.png'))
    ICON_HOME = pygame.image.load(os.path.join(ASSETS_PATH, 'icon_home.png'))
    ICON_PLAY = pygame.image.load(os.path.join(ASSETS_PATH, 'icon_play.png'))
    ICON_SETTINGS = pygame.image.load(os.path.join(ASSETS_PATH, 'icon_settings.png'))
    ICON_EXIT = pygame.image.load(os.path.join(ASSETS_PATH, 'icon_exit.png'))

class Heart_Assets:
    HEART_EMPTY = pygame.image.load(os.path.join(ASSETS_PATH, 'Heart', 'Heart_Empty.png'))
    HEART_HALFFULL = pygame.image.load(os.path.join(ASSETS_PATH, 'Heart', 'Heart_HalfFull.png'))
    HEART_FULL = pygame.image.load(os.path.join(ASSETS_PATH, 'Heart', 'Heart_Full.png'))
    HALFHEART_EMPTY = pygame.image.load(os.path.join(ASSETS_PATH, 'Heart', 'HalfHeart_Empty.png'))
    HALFHEART_FULL = pygame.image.load(os.path.join(ASSETS_PATH, 'Heart', 'HalfHeart_Full.png'))

class Energybar_Assets:
    ENERGYBAR_ENERGY = pygame.image.load(os.path.join(ASSETS_PATH, 'Energybar', 'Energybar_Energy.png'))
    ENERGYBAR_BACK = pygame.image.load(os.path.join(ASSETS_PATH, 'Energybar', 'Energybar_Back.png'))

class Apex:
    APEX_IDLE_1 = pygame.image.load(os.path.join(ASSETS_PATH, 'Apex', 'Apex_Idle_1.png'))
    APEX_IDLE_2 = pygame.image.load(os.path.join(ASSETS_PATH, 'Apex', 'Apex_Idle_2.png'))

class Arachnis:
    ARACHNIS_1 = pygame.image.load(os.path.join(ASSETS_PATH, 'Arachnis', 'Arachnis_1.png'))
    ARACHNIS_2 = pygame.image.load(os.path.join(ASSETS_PATH, 'Arachnis', 'Arachnis_2.png'))

class Brawler:
    BRAWLER_IDLE_1 = pygame.image.load(os.path.join(ASSETS_PATH, 'Brawler', 'Brawler Idle', 'Brawler_1.png'))
    BRAWLER_IDLE_2 = pygame.image.load(os.path.join(ASSETS_PATH, 'Brawler', 'Brawler Idle', 'Brawler_2.png'))
    BRAWLER_IDLE_3 = pygame.image.load(os.path.join(ASSETS_PATH, 'Brawler', 'Brawler Idle', 'Brawler_3.png'))

    BRAWLER_BOOSTATTACK_1 = pygame.image.load(os.path.join(ASSETS_PATH, 'Brawler', 'Boost Attack', 'Brawler_Boostattack_1.png'))
    BRAWLER_BOOSTATTACK_2 = pygame.image.load(os.path.join(ASSETS_PATH, 'Brawler', 'Boost Attack', 'Brawler_Boostattack_2.png'))

class Crypto:
    CRYPTO_1 = pygame.image.load(os.path.join(ASSETS_PATH, 'Crypto', 'Crypto_1.png'))
    CRYPTO_2 = pygame.image.load(os.path.join(ASSETS_PATH, 'Crypto', 'Crypto_2.png'))
    CRYPTO_3 = pygame.image.load(os.path.join(ASSETS_PATH, 'Crypto', 'Crypto_3.png'))
    CRYPTO_4 = pygame.image.load(os.path.join(ASSETS_PATH, 'Crypto', 'Crypto_4.png'))
    CRYPTO_5 = pygame.image.load(os.path.join(ASSETS_PATH, 'Crypto', 'Crypto_5.png'))

class Dark_Force:
    DARK_FORCE_1 = pygame.image.load(os.path.join(ASSETS_PATH, 'Dark Force', 'Dark_Force_1.png'))
    DARK_FORCE_2 = pygame.image.load(os.path.join(ASSETS_PATH, 'Dark Force', 'Dark_Force_2.png'))

# class Moculus:
#   WIP
    
class Sunset:
    SUNSET = pygame.image.load(os.path.join(ASSETS_PATH, 'Sunset', 'Sunset Idle', 'Sunset Idle.png'))

class Enemy_Explosion:
    ENEMY_EXPLOSION_1 = pygame.image.load(os.path.join(ASSETS_PATH, 'Enemy Explosion', 'Enemy_Explosion_1.png'))
    ENEMY_EXPLOSION_2 = pygame.image.load(os.path.join(ASSETS_PATH, 'Enemy Explosion', 'Enemy_Explosion_2.png'))
    ENEMY_EXPLOSION_3 = pygame.image.load(os.path.join(ASSETS_PATH, 'Enemy Explosion', 'Enemy_Explosion_3.png'))
    ENEMY_EXPLOSION_4 = pygame.image.load(os.path.join(ASSETS_PATH, 'Enemy Explosion', 'Enemy_Explosion_4.png'))
    ENEMY_EXPLOSION_5 = pygame.image.load(os.path.join(ASSETS_PATH, 'Enemy Explosion', 'Enemy_Explosion_5.png'))
    ENEMY_EXPLOSION_6 = pygame.image.load(os.path.join(ASSETS_PATH, 'Enemy Explosion', 'Enemy_Explosion_6.png'))
    ENEMY_EXPLOSION_7 = pygame.image.load(os.path.join(ASSETS_PATH, 'Enemy Explosion', 'Enemy_Explosion_7.png'))
    ENEMY_EXPLOSION_8 = pygame.image.load(os.path.join(ASSETS_PATH, 'Enemy Explosion', 'Enemy_Explosion_8.png'))
    ENEMY_EXPLOSION_9 = pygame.image.load(os.path.join(ASSETS_PATH, 'Enemy Explosion', 'Enemy_Explosion_9.png'))
    animationArray = [ENEMY_EXPLOSION_1,ENEMY_EXPLOSION_2,ENEMY_EXPLOSION_3,ENEMY_EXPLOSION_4,ENEMY_EXPLOSION_5,ENEMY_EXPLOSION_6,ENEMY_EXPLOSION_7,ENEMY_EXPLOSION_8,ENEMY_EXPLOSION_9]
    

font = pygame.font.Font(os.path.join(ASSETS_PATH, 'upheavtt.ttf'), 20)