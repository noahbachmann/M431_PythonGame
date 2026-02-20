import pygame
import os
import sys
import json

pygame.font.init()
pygame.mixer.init()

if getattr(sys, 'frozen', False):
    BASE_PATH = sys._MEIPASS
else:
    BASE_PATH = os.path.join(os.path.dirname(__file__), '..')

ASSETS_PATH = os.path.join(BASE_PATH, 'Assets')

# Load sprite sheet once
_sheet = pygame.image.load(os.path.join(ASSETS_PATH, 'sheet.png')).convert_alpha()
with open(os.path.join(ASSETS_PATH, 'sheet.json')) as _f:
    _atlas = {frame['filename']: frame['frame'] for frame in json.load(_f)['frames']}

def _get_sprite(name: str) -> pygame.Surface:
    r = _atlas[name]
    surf = pygame.Surface((r['w'], r['h']), pygame.SRCALPHA)
    surf.blit(_sheet, (0, 0), (r['x'], r['y'], r['w'], r['h']))
    return surf.convert_alpha()

STAR_IMAGE = _get_sprite('star.png')
BORDER_BLOCK = _get_sprite('meteor.png')
EXPLOSION_RADIUS = _get_sprite('explosionRadius.png')

class UI_Assets:
    BUTTON_32x32 = _get_sprite('button_32x32.png')
    BUTTON_64x32 = _get_sprite('button_64x32.png')
    ICON_UPGRADE = _get_sprite('icon_upgrade.png')
    ICON_HOME = _get_sprite('icon_home.png')
    ICON_PLAY = _get_sprite('icon_play.png')
    ICON_RESET = _get_sprite('icon_reset.png')

class Heart_Assets:
    HEART_EMPTY = _get_sprite('Empty_Heart.png')
    HEART_HALFFULL = _get_sprite('Half_Heart.png')
    HEART_FULL = _get_sprite('Full_Heart.png')
    HALFHEART_EMPTY = _get_sprite('Halfcontainer_Empty.png')
    HALFHEART_FULL = _get_sprite('Halfcontainer_Full.png')
    HEALTHBAR = _get_sprite('Healthbar.png')

class Heavy_Attack_Assets:
    HEAVY_ATTACK_USED_1 = _get_sprite('Heavy_Attack_Used_1.png')
    HEAVY_ATTACK_USED_2 = _get_sprite('Heavy_Attack_Used_2.png')
    HEAVY_ATTACK_USED_3 = _get_sprite('Heavy_Attack_Used_3.png')
    HEAVY_ATTACK_USED_4 = _get_sprite('Heavy_Attack_Used_4.png')
    HEAVY_ATTACK_USED_5 = _get_sprite('Heavy_Attack_Used_5.png')
    HEAVY_ATTACK_USED_6 = _get_sprite('Heavy_Attack_Used_6.png')
    HEAVY_ATTACK_USED_7 = _get_sprite('Heavy_Attack_Used_7.png')
    heavyAttackUsedArray = [HEAVY_ATTACK_USED_1, HEAVY_ATTACK_USED_2, HEAVY_ATTACK_USED_3, HEAVY_ATTACK_USED_4, HEAVY_ATTACK_USED_5, HEAVY_ATTACK_USED_6, HEAVY_ATTACK_USED_7]

    HEAVY_ATTACK_CHARGE_1 = _get_sprite('Heavy_Attack_Charge_1.png')
    HEAVY_ATTACK_CHARGE_2 = _get_sprite('Heavy_Attack_Charge_2.png')
    HEAVY_ATTACK_CHARGE_3 = _get_sprite('Heavy_Attack_Charge_3.png')
    HEAVY_ATTACK_CHARGE_4 = _get_sprite('Heavy_Attack_Charge_4.png')
    HEAVY_ATTACK_CHARGE_5 = _get_sprite('Heavy_Attack_Charge_5.png')
    HEAVY_ATTACK_CHARGE_6 = _get_sprite('Heavy_Attack_Charge_6.png')
    HEAVY_ATTACK_CHARGE_7 = _get_sprite('Heavy_Attack_Charge_7.png')
    HEAVY_ATTACK_CHARGE_8 = _get_sprite('Heavy_Attack_Charge_8.png')
    HEAVY_ATTACK_CHARGE_9 = _get_sprite('Heavy_Attack_Charge_9.png')
    HEAVY_ATTACK_CHARGE_10 = _get_sprite('Heavy_Attack_Charge_10.png')
    HEAVY_ATTACK_CHARGE_11 = _get_sprite('Heavy_Attack_Charge_11.png')
    HEAVY_ATTACK_CHARGE_12 = _get_sprite('Heavy_Attack_Charge_12.png')
    HEAVY_ATTACK_CHARGE_13 = _get_sprite('Heavy_Attack_Charge_13.png')
    heavyAttackChargeArray = [HEAVY_ATTACK_CHARGE_1, HEAVY_ATTACK_CHARGE_2, HEAVY_ATTACK_CHARGE_3, HEAVY_ATTACK_CHARGE_4, HEAVY_ATTACK_CHARGE_5, HEAVY_ATTACK_CHARGE_6, HEAVY_ATTACK_CHARGE_7, HEAVY_ATTACK_CHARGE_8, HEAVY_ATTACK_CHARGE_9, HEAVY_ATTACK_CHARGE_10, HEAVY_ATTACK_CHARGE_11, HEAVY_ATTACK_CHARGE_12, HEAVY_ATTACK_CHARGE_13]

    HEAVYATTACKBAR = _get_sprite('Heavyattackbar.png')

class Energybar_Assets:
    ENERGYBAR = _get_sprite('Energybar.png')
    ENERGYBAR_ENERGY = _get_sprite('Energybar_Bar.png')

class Apex:
    APEX_IDLE_1 = _get_sprite('Apex_Idle_1.png')
    APEX_IDLE_2 = _get_sprite('Apex_Idle_2.png')

class Arachnis:
    ARACHNIS_1 = _get_sprite('Arachnis_1.png')
    ARACHNIS_2 = _get_sprite('Arachnis_2.png')

class Brawler:
    BRAWLER_IDLE_1 = _get_sprite('Brawler Idle/Brawler_1.png')
    BRAWLER_IDLE_2 = _get_sprite('Brawler Idle/Brawler_2.png')
    BRAWLER_IDLE_3 = _get_sprite('Brawler Idle/Brawler_3.png')

    BRAWLER_BOOSTATTACK_1 = _get_sprite('Boost Attack/Brawler_Boostattack_1.png')
    BRAWLER_BOOSTATTACK_2 = _get_sprite('Boost Attack/Brawler_Boostattack_2.png')

class Crypto:
    CRYPTO_1 = _get_sprite('Crypto_1.png')
    CRYPTO_2 = _get_sprite('Crypto_2.png')
    CRYPTO_3 = _get_sprite('Crypto_3.png')
    CRYPTO_4 = _get_sprite('Crypto_4.png')
    CRYPTO_5 = _get_sprite('Crypto_5.png')

class Dark_Force:
    DARK_FORCE_1 = _get_sprite('Dark_Force_1.png')
    DARK_FORCE_2 = _get_sprite('Dark_Force_2.png')

class Moculus:
    MOCULUS_1 = _get_sprite('Moculus_1.png')
    MOCULUS_2 = _get_sprite('Moculus_2.png')
    animationArray = [MOCULUS_1, MOCULUS_2]

class Jinx:
    JINX_1 = _get_sprite('Jinx_1.png')
    JINX_2 = _get_sprite('Jinx_2.png')
    animationArray = [JINX_1, JINX_2]

class Sunset:
    SUNSET_IDLE_1 = _get_sprite('Sunset Idle/Sunset_Idle_1.png')
    SUNSET_IDLE_2 = _get_sprite('Sunset Idle/Sunset_Idle_2.png')
    animationArray_idle = [SUNSET_IDLE_1, SUNSET_IDLE_2]

    SUNSET_BOOST_1 = _get_sprite('Sunset Boost/Sunset_Boost_1.png')
    SUNSET_BOOST_2 = _get_sprite('Sunset Boost/Sunset_Boost_2.png')
    SUNSET_BOOST_3 = _get_sprite('Sunset Boost/Sunset_Boost_3.png')
    SUNSET_BOOST_4 = _get_sprite('Sunset Boost/Sunset_Boost_4.png')
    animationArray_boost = [SUNSET_BOOST_1, SUNSET_BOOST_2, SUNSET_BOOST_3, SUNSET_BOOST_4]

    SUNSET_INVIS = _get_sprite('Sunset_Invisible.png')

class Enemy_Explosion:
    ENEMY_EXPLOSION_1 = _get_sprite('Enemy_Explosion_1.png')
    ENEMY_EXPLOSION_2 = _get_sprite('Enemy_Explosion_2.png')
    ENEMY_EXPLOSION_3 = _get_sprite('Enemy_Explosion_3.png')
    ENEMY_EXPLOSION_4 = _get_sprite('Enemy_Explosion_4.png')
    ENEMY_EXPLOSION_5 = _get_sprite('Enemy_Explosion_5.png')
    ENEMY_EXPLOSION_6 = _get_sprite('Enemy_Explosion_6.png')
    ENEMY_EXPLOSION_7 = _get_sprite('Enemy_Explosion_7.png')
    ENEMY_EXPLOSION_8 = _get_sprite('Enemy_Explosion_8.png')
    animationArray = [ENEMY_EXPLOSION_1, ENEMY_EXPLOSION_2, ENEMY_EXPLOSION_3, ENEMY_EXPLOSION_4, ENEMY_EXPLOSION_5, ENEMY_EXPLOSION_6, ENEMY_EXPLOSION_7, ENEMY_EXPLOSION_8]

class Player_Laser:
    PLAYER_LASER_1 = _get_sprite('Player_Laser_1.png')
    PLAYER_LASER_2 = _get_sprite('Player_Laser_2.png')
    PLAYER_LASER_3 = _get_sprite('Player_Laser_3.png')
    animationArray_player_laser = [PLAYER_LASER_1, PLAYER_LASER_2, PLAYER_LASER_3]

    LASER_EXPLOSION_1 = _get_sprite('Laser_Explosion/Laser_Explosion_1.png')
    LASER_EXPLOSION_2 = _get_sprite('Laser_Explosion/Laser_Explosion_2.png')
    LASER_EXPLOSION_3 = _get_sprite('Laser_Explosion/Laser_Explosion_3.png')
    LASER_EXPLOSION_4 = _get_sprite('Laser_Explosion/Laser_Explosion_4.png')
    LASER_EXPLOSION_5 = _get_sprite('Laser_Explosion/Laser_Explosion_5.png')
    animationArray_laser_explosion = [LASER_EXPLOSION_1, LASER_EXPLOSION_2, LASER_EXPLOSION_3, LASER_EXPLOSION_4, LASER_EXPLOSION_5]

class Enemy_Laser:
    ENEMY_LASER_1 = _get_sprite('Enemy_Laser_1.png')
    ENEMY_LASER_2 = _get_sprite('Enemy_Laser_2.png')
    ENEMY_LASER_3 = _get_sprite('Enemy_Laser_3.png')
    animationArray_enemy_laser = [ENEMY_LASER_1, ENEMY_LASER_2, ENEMY_LASER_3]

    LASER_EXPLOSION_1 = _get_sprite('Laser Explosion/Laser_Explosion_1.png')
    LASER_EXPLOSION_2 = _get_sprite('Laser Explosion/Laser_Explosion_2.png')
    LASER_EXPLOSION_3 = _get_sprite('Laser Explosion/Laser_Explosion_3.png')
    LASER_EXPLOSION_4 = _get_sprite('Laser Explosion/Laser_Explosion_4.png')
    LASER_EXPLOSION_5 = _get_sprite('Laser Explosion/Laser_Explosion_5.png')
    animationArray_laser_explosion = [LASER_EXPLOSION_1, LASER_EXPLOSION_2, LASER_EXPLOSION_3, LASER_EXPLOSION_4, LASER_EXPLOSION_5]
    ENEMY_HEAVY_LASER = _get_sprite('Enemy_Heavy_Attack_Laser.png')
    ENEMY_HEAVY_ATTACK = _get_sprite('Enemy_Heavy_Attack.png')

class Heavy_Attack:
    HEAVY_ATTACK_1 = _get_sprite('Heavy_Attack_1.png')
    HEAVY_ATTACK_2 = _get_sprite('Heavy_Attack_2.png')
    HEAVY_ATTACK_3 = _get_sprite('Heavy_Attack_3.png')
    HEAVY_ATTACK_4 = _get_sprite('Heavy_Attack_4.png')
    HEAVY_ATTACK_5 = _get_sprite('Heavy_Attack_5.png')
    HEAVY_ATTACK_6 = _get_sprite('Heavy_Attack_6.png')
    HEAVY_ATTACK_7 = _get_sprite('Heavy_Attack_7.png')
    HEAVY_ATTACK_8 = _get_sprite('Heavy_Attack_8.png')
    animationArray = [HEAVY_ATTACK_2, HEAVY_ATTACK_3, HEAVY_ATTACK_4, HEAVY_ATTACK_5]
    HEAVY_ATTACK = _get_sprite('Heavy_Attack.png')
    HEAVY_ATTACK_LASER = _get_sprite('Heavy_Attack_Laser.png')


AUDIO_PATH = os.path.join(ASSETS_PATH, '_Audio')

class Audio:
    COIN_UP = pygame.mixer.Sound(os.path.join(AUDIO_PATH, 'coin_up.ogg'))
    COIN_UP.set_volume(0.35)
    LASER_HIGH = pygame.mixer.Sound(os.path.join(AUDIO_PATH, 'laser.ogg'))
    LASER_HIGH.set_volume(0.32)
    PLAYER_DAMAGE = pygame.mixer.Sound(os.path.join(AUDIO_PATH, 'player_damage_explosion.ogg'))
    PLAYER_DAMAGE.set_volume(0.4)
    MINIBOSS_SPAWN = pygame.mixer.Sound(os.path.join(AUDIO_PATH, 'miniboss_spawn.ogg'))
    MINIBOSS_SPAWN.set_volume(0.4)
    GAME_END = pygame.mixer.Sound(os.path.join(AUDIO_PATH, 'game_end.ogg'))
    GAME_END.set_volume(0.37)
    EXPLOSION = pygame.mixer.Sound(os.path.join(AUDIO_PATH, 'explosion.ogg'))
    EXPLOSION.set_volume(0.35)
    ENEMY_BOOST = pygame.mixer.Sound(os.path.join(AUDIO_PATH, 'enemy_boost.ogg'))
    ENEMY_BOOST.set_volume(0.24)
    BUTTON_PRESS = pygame.mixer.Sound(os.path.join(AUDIO_PATH, 'button_press.ogg'))
    BUTTON_PRESS.set_volume(0.35)
    BOOST = pygame.mixer.Sound(os.path.join(AUDIO_PATH, 'boost.ogg'))
    BOOST.set_volume(0.13)
    ENEMY_DEATH = pygame.mixer.Sound(os.path.join(AUDIO_PATH, 'enemyDeath.ogg'))
    ENEMY_DEATH.set_volume(0.38)
    UNREAL = pygame.mixer.Sound(os.path.join(AUDIO_PATH, 'unreal.ogg'))
    UNREAL.set_volume(0.5)

class Crosshair:
    Crosshair1 = _get_sprite('Crosshair-1.png')
    Crosshair2 = _get_sprite('Crosshair-2.png')

font = pygame.font.Font(os.path.join(ASSETS_PATH, 'upheavtt.ttf'), 24)
font_32 = pygame.font.Font(os.path.join(ASSETS_PATH, 'upheavtt.ttf'), 32)
karmaticArcadeFont = pygame.font.Font(os.path.join(ASSETS_PATH, 'KarmaticArcade.ttf'), 24)
karmaticArcadeFont_40 = pygame.font.Font(os.path.join(ASSETS_PATH, 'KarmaticArcade.ttf'), 40)
karmaticArcadeFont_48 = pygame.font.Font(os.path.join(ASSETS_PATH, 'KarmaticArcade.ttf'), 48)
