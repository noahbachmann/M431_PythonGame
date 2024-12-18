import pygame
import os
import sys

pygame.font.init()
pygame.mixer.init()

if getattr(sys, 'frozen', False):
    BASE_PATH = sys._MEIPASS
else:
    BASE_PATH = os.path.join(os.path.dirname(__file__), '..')

ASSETS_PATH = os.path.join(BASE_PATH, 'Assets')

HEAVY_IMAGE = pygame.image.load(os.path.join(ASSETS_PATH,'Other', 'heavy.png'))
STAR_IMAGE = pygame.image.load(os.path.join(ASSETS_PATH,'Other', 'star.png'))
BORDER_BLOCK = pygame.image.load(os.path.join(ASSETS_PATH,'Other', 'meteor.png'))
EXPLOSION_RADIUS = pygame.image.load(os.path.join(ASSETS_PATH,'Other', 'explosionRadius.png'))
BACKGROUND_IMAGE = pygame.image.load(os.path.join(ASSETS_PATH,'Other','background_muster.png'))

class UI_Assets:
    BUTTON_32x32 = pygame.image.load(os.path.join(ASSETS_PATH,'Other', 'button_32x32.png'))
    BUTTON_64x32 = pygame.image.load(os.path.join(ASSETS_PATH,'Other', 'button_64x32.png'))
    ICON_UPGRADE = pygame.image.load(os.path.join(ASSETS_PATH,'Other', 'icon_upgrade.png'))
    ICON_HOME = pygame.image.load(os.path.join(ASSETS_PATH,'Other', 'icon_home.png'))
    ICON_PLAY = pygame.image.load(os.path.join(ASSETS_PATH,'Other', 'icon_play.png'))
    ICON_SETTINGS = pygame.image.load(os.path.join(ASSETS_PATH,'Other', 'icon_settings.png'))
    ICON_EXIT = pygame.image.load(os.path.join(ASSETS_PATH,'Other', 'icon_exit.png'))
    ICON_TRASH = pygame.image.load(os.path.join(ASSETS_PATH,'Other', 'icon_trash.png'))
    ICON_RESET = pygame.image.load(os.path.join(ASSETS_PATH,'Other', 'icon_reset.png'))

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

class Moculus:
    MOCULUS_1 = pygame.image.load(os.path.join(ASSETS_PATH, 'Moculus', 'Moculus_1.png'))
    MOCULUS_2 = pygame.image.load(os.path.join(ASSETS_PATH, 'Moculus', 'Moculus_2.png'))
    animationArray = [MOCULUS_1, MOCULUS_2]

class Jinx:
    JINX_1 = pygame.image.load(os.path.join(ASSETS_PATH, 'Jinx', 'Jinx_1.png'))
    JINX_2 = pygame.image.load(os.path.join(ASSETS_PATH, 'Jinx', 'Jinx_2.png'))
    animationArray = [JINX_1, JINX_2]

    
class Sunset:
    SUNSET_IDLE_1 = pygame.image.load(os.path.join(ASSETS_PATH, 'Sunset', 'Sunset Idle', 'Sunset_Idle_1.png'))
    SUNSET_IDLE_2 = pygame.image.load(os.path.join(ASSETS_PATH, 'Sunset', 'Sunset Idle', 'Sunset_Idle_2.png'))
    animationArray_idle = [SUNSET_IDLE_1, SUNSET_IDLE_2]

    SUNSET_BOOST_1 = pygame.image.load(os.path.join(ASSETS_PATH, 'Sunset', 'Sunset Boost', 'Sunset_Boost_1.png'))
    SUNSET_BOOST_2 = pygame.image.load(os.path.join(ASSETS_PATH, 'Sunset', 'Sunset Boost', 'Sunset_Boost_2.png'))
    SUNSET_BOOST_3 = pygame.image.load(os.path.join(ASSETS_PATH, 'Sunset', 'Sunset Boost', 'Sunset_Boost_3.png'))
    SUNSET_BOOST_4 = pygame.image.load(os.path.join(ASSETS_PATH, 'Sunset', 'Sunset Boost', 'Sunset_Boost_4.png'))
    animationArray_boost = [SUNSET_BOOST_1, SUNSET_BOOST_2, SUNSET_BOOST_3, SUNSET_BOOST_4]

class Enemy_Explosion:
    ENEMY_EXPLOSION_1 = pygame.image.load(os.path.join(ASSETS_PATH, 'Enemy Explosion', 'Enemy_Explosion_1.png'))
    ENEMY_EXPLOSION_2 = pygame.image.load(os.path.join(ASSETS_PATH, 'Enemy Explosion', 'Enemy_Explosion_2.png'))
    ENEMY_EXPLOSION_3 = pygame.image.load(os.path.join(ASSETS_PATH, 'Enemy Explosion', 'Enemy_Explosion_3.png'))
    ENEMY_EXPLOSION_4 = pygame.image.load(os.path.join(ASSETS_PATH, 'Enemy Explosion', 'Enemy_Explosion_4.png'))
    ENEMY_EXPLOSION_5 = pygame.image.load(os.path.join(ASSETS_PATH, 'Enemy Explosion', 'Enemy_Explosion_5.png'))
    ENEMY_EXPLOSION_6 = pygame.image.load(os.path.join(ASSETS_PATH, 'Enemy Explosion', 'Enemy_Explosion_6.png'))
    ENEMY_EXPLOSION_7 = pygame.image.load(os.path.join(ASSETS_PATH, 'Enemy Explosion', 'Enemy_Explosion_7.png'))
    ENEMY_EXPLOSION_8 = pygame.image.load(os.path.join(ASSETS_PATH, 'Enemy Explosion', 'Enemy_Explosion_8.png'))
    animationArray = [ENEMY_EXPLOSION_1,ENEMY_EXPLOSION_2,ENEMY_EXPLOSION_3,ENEMY_EXPLOSION_4,ENEMY_EXPLOSION_5,ENEMY_EXPLOSION_6,ENEMY_EXPLOSION_7,ENEMY_EXPLOSION_8]

class Player_Laser:
    PLAYER_LASER_1 = pygame.image.load(os.path.join(ASSETS_PATH, 'Player Laser', 'Player_Laser_1.png'))
    PLAYER_LASER_2 = pygame.image.load(os.path.join(ASSETS_PATH, 'Player Laser', 'Player_Laser_2.png'))
    PLAYER_LASER_3 = pygame.image.load(os.path.join(ASSETS_PATH, 'Player Laser', 'Player_Laser_3.png'))
    animationArray_player_laser = [PLAYER_LASER_1, PLAYER_LASER_2, PLAYER_LASER_3]

    LASER_EXPLOSION_1 = pygame.image.load(os.path.join(ASSETS_PATH, 'Player Laser', 'Laser_Explosion', 'Laser_Explosion_1.png'))
    LASER_EXPLOSION_2 = pygame.image.load(os.path.join(ASSETS_PATH, 'Player Laser', 'Laser_Explosion', 'Laser_Explosion_2.png'))
    LASER_EXPLOSION_3 = pygame.image.load(os.path.join(ASSETS_PATH, 'Player Laser', 'Laser_Explosion', 'Laser_Explosion_3.png'))
    LASER_EXPLOSION_4 = pygame.image.load(os.path.join(ASSETS_PATH, 'Player Laser', 'Laser_Explosion', 'Laser_Explosion_4.png'))
    LASER_EXPLOSION_5 = pygame.image.load(os.path.join(ASSETS_PATH, 'Player Laser', 'Laser_Explosion', 'Laser_Explosion_5.png'))
    animationArray_laser_explosion = [LASER_EXPLOSION_1, LASER_EXPLOSION_2, LASER_EXPLOSION_3, LASER_EXPLOSION_4, LASER_EXPLOSION_5]

class Enemy_Laser:
    ENEMY_LASER_1 = pygame.image.load(os.path.join(ASSETS_PATH, 'Enemy Laser', 'Enemy_Laser_1.png'))
    ENEMY_LASER_2 = pygame.image.load(os.path.join(ASSETS_PATH, 'Enemy Laser', 'Enemy_Laser_2.png'))
    ENEMY_LASER_3 = pygame.image.load(os.path.join(ASSETS_PATH, 'Enemy Laser', 'Enemy_Laser_3.png'))
    animationArray_enemy_laser = [ENEMY_LASER_1, ENEMY_LASER_2, ENEMY_LASER_3]

    LASER_EXPLOSION_1 = pygame.image.load(os.path.join(ASSETS_PATH, 'Enemy Laser', 'Laser Explosion', 'Laser_Explosion_1.png'))
    LASER_EXPLOSION_2 = pygame.image.load(os.path.join(ASSETS_PATH, 'Enemy Laser', 'Laser Explosion', 'Laser_Explosion_2.png'))
    LASER_EXPLOSION_3 = pygame.image.load(os.path.join(ASSETS_PATH, 'Enemy Laser', 'Laser Explosion', 'Laser_Explosion_3.png'))
    LASER_EXPLOSION_4 = pygame.image.load(os.path.join(ASSETS_PATH, 'Enemy Laser', 'Laser Explosion', 'Laser_Explosion_4.png'))
    LASER_EXPLOSION_5 = pygame.image.load(os.path.join(ASSETS_PATH, 'Enemy Laser', 'Laser Explosion', 'Laser_Explosion_5.png'))
    animationArray_laser_explosion = [LASER_EXPLOSION_1, LASER_EXPLOSION_2, LASER_EXPLOSION_3, LASER_EXPLOSION_4, LASER_EXPLOSION_5]

# class Heavy_Attack:
#     WIP

AUDIO_PATH = os.path.join(ASSETS_PATH, '_Audio')

class Audio:
    COIN_UP = pygame.mixer.Sound(os.path.join(AUDIO_PATH,'coin_up.wav'))
    COIN_UP.set_volume(0.5)
    LASER_HIGH = pygame.mixer.Sound(os.path.join(AUDIO_PATH,'laser_high.wav'))
    LASER_HIGH.set_volume(0.4)
    PLAYER_DAMAGE = pygame.mixer.Sound(os.path.join(AUDIO_PATH,'player_damage_explosion.mp3'))
    PLAYER_DAMAGE.set_volume(0.4)
    MINIBOSS_SPAWN = pygame.mixer.Sound(os.path.join(AUDIO_PATH,'miniboss_spawn.mp3'))
    MINIBOSS_SPAWN.set_volume(0.4)
    GAME_END = pygame.mixer.Sound(os.path.join(AUDIO_PATH,'game_end.mp3'))
    GAME_END.set_volume(0.4)
    EXPLOSION = pygame.mixer.Sound(os.path.join(AUDIO_PATH,'explosion.mp3'))
    EXPLOSION.set_volume(0.5)
    ENEMY_BOOST = pygame.mixer.Sound(os.path.join(AUDIO_PATH,'enemy_boost.wav'))
    ENEMY_BOOST.set_volume(0.35)
    BUTTON_PRESS = pygame.mixer.Sound(os.path.join(AUDIO_PATH,'button_press.mp3'))
    BUTTON_PRESS.set_volume(0.4)
    
class Crosshair:
    Crosshair1 = pygame.image.load(os.path.join(ASSETS_PATH, 'Crosshair', 'Crosshair-1.png'))
    Crosshair2 = pygame.image.load(os.path.join(ASSETS_PATH, 'Crosshair', 'Crosshair-2.png'))

font = pygame.font.Font(os.path.join(ASSETS_PATH, 'upheavtt.ttf'), 20)
karmaticArcadeFont = pygame.font.Font(os.path.join(ASSETS_PATH, 'KarmaticArcade.ttf'), 20)
