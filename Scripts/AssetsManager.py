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

TUTORIAL = pygame.image.load(os.path.join(ASSETS_PATH,'Other', 'Tutorial.png'))
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
    ICON_TROPHIE = pygame.image.load(os.path.join(ASSETS_PATH,'Other', 'icon_trophie.png'))
    HOTKEY_POPUP = pygame.image.load(os.path.join(ASSETS_PATH,'Other', 'hotkey_popup.png'))

class Heart_Assets:
    HEART_EMPTY = pygame.image.load(os.path.join(ASSETS_PATH, 'Heart', 'Empty_Heart.png'))
    HEART_HALFFULL = pygame.image.load(os.path.join(ASSETS_PATH, 'Heart', 'Half_Heart.png'))
    HEART_FULL = pygame.image.load(os.path.join(ASSETS_PATH, 'Heart', 'Full_Heart.png'))
    HALFHEART_EMPTY = pygame.image.load(os.path.join(ASSETS_PATH, 'Heart', 'Halfcontainer_Empty.png'))
    HALFHEART_FULL = pygame.image.load(os.path.join(ASSETS_PATH, 'Heart', 'Halfcontainer_Full.png'))
    HEALTHBAR = pygame.image.load(os.path.join(ASSETS_PATH, 'Heart', 'Healthbar.png'))

class Heavy_Attack_Assets:
    HEAVY_ATTACK_USED_1 = pygame.image.load(os.path.join(ASSETS_PATH, 'Heavyattackbar', 'Heavy_Attack_Used_1.png'))
    HEAVY_ATTACK_USED_2 = pygame.image.load(os.path.join(ASSETS_PATH, 'Heavyattackbar', 'Heavy_Attack_Used_2.png'))
    HEAVY_ATTACK_USED_3 = pygame.image.load(os.path.join(ASSETS_PATH, 'Heavyattackbar', 'Heavy_Attack_Used_3.png'))
    HEAVY_ATTACK_USED_4 = pygame.image.load(os.path.join(ASSETS_PATH, 'Heavyattackbar', 'Heavy_Attack_Used_4.png'))
    HEAVY_ATTACK_USED_5 = pygame.image.load(os.path.join(ASSETS_PATH, 'Heavyattackbar', 'Heavy_Attack_Used_5.png'))
    HEAVY_ATTACK_USED_6 = pygame.image.load(os.path.join(ASSETS_PATH, 'Heavyattackbar', 'Heavy_Attack_Used_6.png'))
    HEAVY_ATTACK_USED_7 = pygame.image.load(os.path.join(ASSETS_PATH, 'Heavyattackbar', 'Heavy_Attack_Used_7.png'))
    heavyAttackUsedArray = [HEAVY_ATTACK_USED_1,HEAVY_ATTACK_USED_2,HEAVY_ATTACK_USED_3,HEAVY_ATTACK_USED_4,HEAVY_ATTACK_USED_5,HEAVY_ATTACK_USED_6,HEAVY_ATTACK_USED_7]
    
    HEAVY_ATTACK_CHARGE_1 = pygame.image.load(os.path.join(ASSETS_PATH, 'Heavyattackbar', 'Heavy_Attack_Charge_1.png'))
    HEAVY_ATTACK_CHARGE_2 = pygame.image.load(os.path.join(ASSETS_PATH, 'Heavyattackbar', 'Heavy_Attack_Charge_2.png'))
    HEAVY_ATTACK_CHARGE_3 = pygame.image.load(os.path.join(ASSETS_PATH, 'Heavyattackbar', 'Heavy_Attack_Charge_3.png'))
    HEAVY_ATTACK_CHARGE_4 = pygame.image.load(os.path.join(ASSETS_PATH, 'Heavyattackbar', 'Heavy_Attack_Charge_4.png'))
    HEAVY_ATTACK_CHARGE_5 = pygame.image.load(os.path.join(ASSETS_PATH, 'Heavyattackbar', 'Heavy_Attack_Charge_5.png'))
    HEAVY_ATTACK_CHARGE_6 = pygame.image.load(os.path.join(ASSETS_PATH, 'Heavyattackbar', 'Heavy_Attack_Charge_6.png'))
    HEAVY_ATTACK_CHARGE_7 = pygame.image.load(os.path.join(ASSETS_PATH, 'Heavyattackbar', 'Heavy_Attack_Charge_7.png'))
    HEAVY_ATTACK_CHARGE_8 = pygame.image.load(os.path.join(ASSETS_PATH, 'Heavyattackbar', 'Heavy_Attack_Charge_8.png'))
    HEAVY_ATTACK_CHARGE_9 = pygame.image.load(os.path.join(ASSETS_PATH, 'Heavyattackbar', 'Heavy_Attack_Charge_9.png'))
    HEAVY_ATTACK_CHARGE_10 = pygame.image.load(os.path.join(ASSETS_PATH, 'Heavyattackbar', 'Heavy_Attack_Charge_10.png'))
    HEAVY_ATTACK_CHARGE_11 = pygame.image.load(os.path.join(ASSETS_PATH, 'Heavyattackbar', 'Heavy_Attack_Charge_11.png'))
    HEAVY_ATTACK_CHARGE_12 = pygame.image.load(os.path.join(ASSETS_PATH, 'Heavyattackbar', 'Heavy_Attack_Charge_12.png'))
    HEAVY_ATTACK_CHARGE_13 = pygame.image.load(os.path.join(ASSETS_PATH, 'Heavyattackbar', 'Heavy_Attack_Charge_13.png'))
    heavyAttackChargeArray = [HEAVY_ATTACK_CHARGE_1,HEAVY_ATTACK_CHARGE_2,HEAVY_ATTACK_CHARGE_3,HEAVY_ATTACK_CHARGE_4,HEAVY_ATTACK_CHARGE_5,HEAVY_ATTACK_CHARGE_6,HEAVY_ATTACK_CHARGE_7,HEAVY_ATTACK_CHARGE_8,HEAVY_ATTACK_CHARGE_9,HEAVY_ATTACK_CHARGE_10,HEAVY_ATTACK_CHARGE_11,HEAVY_ATTACK_CHARGE_12,HEAVY_ATTACK_CHARGE_13]

    HEAVYATTACKBAR = pygame.image.load(os.path.join(ASSETS_PATH, 'Heavyattackbar', 'Heavyattackbar.png'))

class Energybar_Assets:
    ENERGYBAR = pygame.image.load(os.path.join(ASSETS_PATH, 'Energybar', 'Energybar.png'))
    ENERGYBAR_ENERGY = pygame.image.load(os.path.join(ASSETS_PATH, 'Energybar', 'Energybar_Bar.png'))

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
    
    SUNSET_INVIS = pygame.image.load(os.path.join(ASSETS_PATH, 'Sunset', 'Sunset_Invisible.png'))

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
    ENEMY_HEAVY_LASER = pygame.image.load(os.path.join(ASSETS_PATH, 'Enemy Laser', 'Heavy_Attack_Laser.png'))
    ENEMY_HEAVY_ATTACK = pygame.image.load(os.path.join(ASSETS_PATH, 'Enemy Laser', 'Enemy_Heavy_Attack.png'))
class Heavy_Attack:
    HEAVY_ATTACK_1 = pygame.image.load(os.path.join(ASSETS_PATH, 'Heavy Attack', 'Heavy_Attack_1.png'))
    HEAVY_ATTACK_2 = pygame.image.load(os.path.join(ASSETS_PATH, 'Heavy Attack', 'Heavy_Attack_2.png'))
    HEAVY_ATTACK_3 = pygame.image.load(os.path.join(ASSETS_PATH, 'Heavy Attack', 'Heavy_Attack_3.png'))
    HEAVY_ATTACK_4 = pygame.image.load(os.path.join(ASSETS_PATH, 'Heavy Attack', 'Heavy_Attack_4.png'))
    HEAVY_ATTACK_5 = pygame.image.load(os.path.join(ASSETS_PATH, 'Heavy Attack', 'Heavy_Attack_5.png'))
    HEAVY_ATTACK_6 = pygame.image.load(os.path.join(ASSETS_PATH, 'Heavy Attack', 'Heavy_Attack_6.png'))
    HEAVY_ATTACK_7 = pygame.image.load(os.path.join(ASSETS_PATH, 'Heavy Attack', 'Heavy_Attack_7.png'))
    HEAVY_ATTACK_8 = pygame.image.load(os.path.join(ASSETS_PATH, 'Heavy Attack', 'Heavy_Attack_8.png'))
    animationArray = [HEAVY_ATTACK_2, HEAVY_ATTACK_3, HEAVY_ATTACK_4, HEAVY_ATTACK_5]
    HEAVY_ATTACK = pygame.image.load(os.path.join(ASSETS_PATH, 'Heavy Attack', 'Heavy_Attack.png'))
    HEAVY_ATTACK_LASER = pygame.image.load(os.path.join(ASSETS_PATH, 'Heavy Attack', 'Heavy_Attack_Laser.png'))


AUDIO_PATH = os.path.join(ASSETS_PATH, '_Audio')

class Audio:
    COIN_UP = pygame.mixer.Sound(os.path.join(AUDIO_PATH,'coin_up.wav'))
    COIN_UP.set_volume(0.35)
    LASER_HIGH = pygame.mixer.Sound(os.path.join(AUDIO_PATH,'laser.mp3'))
    LASER_HIGH.set_volume(0.32)
    PLAYER_DAMAGE = pygame.mixer.Sound(os.path.join(AUDIO_PATH,'player_damage_explosion.mp3'))
    PLAYER_DAMAGE.set_volume(0.4)
    MINIBOSS_SPAWN = pygame.mixer.Sound(os.path.join(AUDIO_PATH,'miniboss_spawn.mp3'))
    MINIBOSS_SPAWN.set_volume(0.4)
    GAME_END = pygame.mixer.Sound(os.path.join(AUDIO_PATH,'game_end.mp3'))
    GAME_END.set_volume(0.37)
    EXPLOSION = pygame.mixer.Sound(os.path.join(AUDIO_PATH,'explosion.mp3'))
    EXPLOSION.set_volume(0.35)
    ENEMY_BOOST = pygame.mixer.Sound(os.path.join(AUDIO_PATH,'enemy_boost.wav'))
    ENEMY_BOOST.set_volume(0.24)
    BUTTON_PRESS = pygame.mixer.Sound(os.path.join(AUDIO_PATH,'button_press.mp3'))
    BUTTON_PRESS.set_volume(0.35)
    BOOST = pygame.mixer.Sound(os.path.join(AUDIO_PATH,'boost.mp3'))
    BOOST.set_volume(0.13)
    ENEMY_DEATH = pygame.mixer.Sound(os.path.join(AUDIO_PATH,'enemyDeath.mp3'))
    ENEMY_DEATH.set_volume(0.38)
    UNREAL = pygame.mixer.Sound(os.path.join(AUDIO_PATH,'unreal.mp3'))
    UNREAL.set_volume(0.5)
    
class Crosshair:
    Crosshair1 = pygame.image.load(os.path.join(ASSETS_PATH, 'Crosshair', 'Crosshair-1.png'))
    Crosshair2 = pygame.image.load(os.path.join(ASSETS_PATH, 'Crosshair', 'Crosshair-2.png'))

font = pygame.font.Font(os.path.join(ASSETS_PATH, 'upheavtt.ttf'), 20)
karmaticArcadeFont = pygame.font.Font(os.path.join(ASSETS_PATH, 'KarmaticArcade.ttf'), 20)
karmaticArcadeFont_25 = pygame.font.Font(os.path.join(ASSETS_PATH, 'KarmaticArcade.ttf'), 25)
