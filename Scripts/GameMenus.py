import pygame
import Scripts.AssetsManager
from Scripts.Button import *
from Scripts.AssetsManager import UI_Assets, Crosshair, karmaticArcadeFont
from Scripts.Settings import *
import Scripts.DataManager
import asyncio

class Menu:
    def __init__(self, surface, left, top, gameState, color = None, enabled = False, size:tuple = None):
        Scripts.DataManager.loadData()
        self.cameraSurface = surface
        self.left = left
        self.top = top
        self.gameState = gameState
        self.buttons = []
        self.texts = []
        self.enabled = enabled
        if color:
            self.color = color
        else:
            self.color = (102, 153, 255)
        if size:
            self.size = size
            self.rect = pygame.FRect(self.left, self.top, size[0], size[1])
        else:
            self.rect = pygame.FRect(self.left, self.top, 500, 500)

    def draw(self):
        pygame.draw.rect(self.cameraSurface, self.color, self.rect, 0, 0)
        for button in self.buttons:
            button.update(self.cameraSurface)
        for text, textRect in self.texts:
            self.cameraSurface.blit(text, textRect)
            
    def quitGame(self):
        self.enabled = False
        self.gameState['quit'] = True
    
    def mainMenu(self):
        self.enabled = False
        Scripts.DataManager.saveData()
        self.gameState['gaming'] = "MainMenu"

class EndGameMenu(Menu):
    def __init__(self, surface, left, top, size:tuple, gameState, enabled,  score):
        super().__init__(surface, left, top, gameState, enabled=enabled, size=size)
        self.buttons.append(Button((self.rect.centerx, self.rect.centery), func=self.newGame, icon=UI_Assets.ICON_PLAY))
        self.buttons.append(Button((self.rect.centerx, self.rect.centery + 96), func=self.mainMenu, icon=UI_Assets.ICON_HOME))
        self.buttons.append(Button((self.rect.centerx, self.rect.centery + 192), func=self.quitGame, icon=UI_Assets.ICON_EXIT))
        self.texts.append((font.render(str(score), False, (0,0,0)), None))
        self.texts[0] = (self.texts[0][0], self.texts[0][0].get_frect(center=(self.rect.centerx, self.rect.centery - 96)))
        
    def newGame(self):
        self.enabled = False

class UpgradesMenu(Menu):
    def __init__(self, surface, left, top, player, gameState, hudController, color = None, size:tuple = None):
        super().__init__(surface,left,top, gameState, color,size=size)
        self.player = player
        self.upgrades = ["Upgrades", "atkSpeed", "atkDmg", "health", "heavyCd", "boostTank", "boostStrength"]
        self.upgradesLevel = [0,0,0,0,0,0]
        self.upgradesMultiplier = [20,40,40,15,20,40]
        self.generatedButtons = False
        self.hudController = hudController
        self.buttons.append(Button((self.rect.centerx - TILE_SIZE*1.5, self.rect.midbottom[1] - TILE_SIZE * 1.5), func=self.endPause, icon=UI_Assets.ICON_PLAY))
        self.buttons.append(Button((self.rect.centerx, self.rect.midbottom[1] - TILE_SIZE * 1.5), func=self.mainMenu, icon=UI_Assets.ICON_HOME))
        self.buttons.append(Button((self.rect.centerx + TILE_SIZE*1.5, self.rect.midbottom[1] - TILE_SIZE * 1.5), func=self.quitGame, icon=UI_Assets.ICON_EXIT))
        self.texts.append((font.render(str(self.player.gold), False, (0,0,0)), None))
        self.texts[0] = (self.texts[0][0], self.texts[0][0].get_frect(center=(self.rect.bottomright[0] - 64, self.rect.bottomright[1] - 64)))
    
    def general(self):
        upgrdHeight = self.rect.height - (self.rect.height//4) 
        upgrdWidth = self.rect.width - TILE_SIZE*2   
        for i in range(1,8):
            x = self.rect.left + TILE_SIZE
            y = self.rect.top + (upgrdHeight /14) * (i*2 - 1)
            upgradeText = font.render(self.upgrades[i-1], False, (0,0,0))
            upgradeTextRect = upgradeText.get_frect(midleft = (x,y))
            self.cameraSurface.blit(upgradeText, upgradeTextRect)
            x += upgrdWidth / 2 + (TILE_SIZE /2)
            if i == 1:
                levelText = font.render("Lvl.", False, (0,0,0))
            else:
                levelText = font.render(str(self.upgradesLevel[i-2]), False, (0,0,0))
            levelTextRect = levelText.get_frect(center = (x,y))
            self.cameraSurface.blit(levelText, levelTextRect)
            x += (upgrdWidth / 2)*(1/3)
            if not self.generatedButtons and i > 1:
                self.buttons.append(Button((x,y),UI_Assets.BUTTON_32x32,"+", lambda j=i: self.player.upgrade(self.upgrades[j-1], self.upgradesLevel)))
            x += (upgrdWidth / 2)*(1/3)
            if i == 1:
                costText = font.render("Cost", False, (0,0,0))
            else:
                costText = font.render(str((self.upgradesLevel[i-2]*self.upgradesMultiplier[i-2])+(self.upgradesMultiplier[i-2]*2)), False, (0,0,0))
            costTextRect = costText.get_frect(center = (x,y))
            self.cameraSurface.blit(costText, costTextRect)
        self.generatedButtons = True

    def draw(self, surface):
        pygame.draw.rect(self.cameraSurface, self.color, self.rect, 0, 0)
        self.general()
        for button in self.buttons:
            button.update(surface)
        self.texts[0] = (font.render(str(self.player.gold), False, (0,0,0)), self.texts[0][1])
        for text, textRect in self.texts:
            self.cameraSurface.blit(text, textRect)

    def endPause(self):
        self.hudController.pause = False


class MainMenu(Menu):
    def __init__(self, surface, left, top, size:tuple, enabled, gameState):
        super().__init__(surface, left, top, gameState, enabled=enabled, size=size)
        self.buttons.append(Button((self.rect.centerx *0.8, self.rect.centery - TILE_SIZE*1.2), func=self.newGame, icon=UI_Assets.ICON_PLAY)) 
        self.buttons.append(Button((self.rect.centerx *0.8, self.rect.centery), func=self.settings, icon=UI_Assets.ICON_SETTINGS))   
        self.buttons.append(Button((self.rect.centerx *0.8, self.rect.centery + TILE_SIZE*1.2), func=self.stats, icon=UI_Assets.ICON_TROPHIE))
        self.buttons.append(Button((self.rect.centerx *0.8, self.rect.centery + TILE_SIZE*2.4), func=self.quitGame, icon=UI_Assets.ICON_EXIT))   
        self.texts.append((karmaticArcadeFont.render(str("Space Shooter"), False, (0,0,0)),))
        self.texts.append((karmaticArcadeFont.render(str("Play"), False, (0,0,0)),))
        self.texts.append((karmaticArcadeFont.render(str("Settings"), False, (0,0,0)),))
        self.texts.append((karmaticArcadeFont.render(str("Stats"), False, (0,0,0)),))
        self.texts.append((karmaticArcadeFont.render(str("Exit"), False, (0,0,0)),))
        self.texts[0] = (self.texts[0][0], self.texts[0][0].get_frect(center=(self.rect.centerx, self.rect.centery //2)))
        self.texts[1] = (self.texts[1][0], self.texts[1][0].get_frect(midleft=(self.rect.centerx *0.8 + TILE_SIZE, self.rect.centery - TILE_SIZE*1.2)))
        self.texts[2] = (self.texts[2][0], self.texts[2][0].get_frect(midleft=(self.rect.centerx *0.8 + TILE_SIZE, self.rect.centery)))
        self.texts[3] = (self.texts[3][0], self.texts[3][0].get_frect(midleft=(self.rect.centerx *0.8 + TILE_SIZE, self.rect.centery + TILE_SIZE*1.2)))
        self.texts[4] = (self.texts[4][0], self.texts[4][0].get_frect(midleft=(self.rect.centerx *0.8 + TILE_SIZE, self.rect.centery + TILE_SIZE*2.4)))
    def newGame(self):
        self.enabled = False
        self.gameState['gaming'] = "Gaming"

    def stats(self):
        self.enabled = False
        self.gameState['gaming'] = "Stats"

    def settings(self):
        self.enabled = False
        self.gameState['gaming'] = "Settings"
        Scripts.DataManager.loadData()

class SettingsMenu(Menu):
    def __init__(self, surface, left, top, size:tuple, enabled, gameState):
        super().__init__(surface, left, top, gameState, enabled=enabled, size=size)
        self.generalButtons = []
        self.controlsButtons = []
        self.keybindTexts = []
        self.keyModal = UI_Assets.HOTKEY_POPUP
        self.keyModalRect = self.keyModal.get_frect(center=(self.rect.centerx, self.rect.centery))
        self.keyChange = False
        self.keyToChange = ''
        self.sec1 = False
        self.sec2 = False
        self.texts.append((font.render(str("Settings"), False, (0,0,0)), None))
        self.texts[0] = (self.texts[0][0], self.texts[0][0].get_frect(center=(self.rect.centerx, self.rect.centery - 290)))
        self.buttons.append(Button((self.rect.centerx + 325, self.rect.centery - 325), func=self.mainMenu, icon=UI_Assets.ICON_HOME))   
        self.cursor = Crosshair.Crosshair1
        self.KeybindList = ["Keybinds", "Up", "Down", "Left", "Right", "Boost", "Close Game"]
        self.controlsButtons.append(Button((self.rect.centerx * 0.75, self.rect.midbottom[1] - TILE_SIZE * 6.7),func= lambda:self.change_Hotkey('Hotkey_Up'), text='Hotkey_Up', keyText=True))
        self.controlsButtons.append(Button((self.rect.centerx * 0.75, self.rect.midbottom[1] - TILE_SIZE * 5.6),func= lambda:self.change_Hotkey('Hotkey_Down'), text='Hotkey_Down', keyText=True))
        self.controlsButtons.append(Button((self.rect.centerx * 0.75, self.rect.midbottom[1] - TILE_SIZE * 4.5),func= lambda:self.change_Hotkey('Hotkey_Left'), text='Hotkey_Left', keyText=True))
        self.controlsButtons.append(Button((self.rect.centerx * 0.75, self.rect.midbottom[1] - TILE_SIZE * 3.4),func= lambda:self.change_Hotkey('Hotkey_Right'), text='Hotkey_Right', keyText=True))
        self.controlsButtons.append(Button((self.rect.centerx * 0.75, self.rect.midbottom[1] - TILE_SIZE * 2.3),func= lambda:self.change_Hotkey('Hotkey_Boost'), text='Hotkey_Boost', keyText=True))
        self.controlsButtons.append(Button((self.rect.centerx * 0.75, self.rect.midbottom[1] - TILE_SIZE * 1.2),func= lambda:self.change_Hotkey('Hotkey_close'), text='Hotkey_close', keyText=True))
        self.controlsButtons.append(Button((self.rect.centerx * 1.35, self.rect.midbottom[1] - TILE_SIZE * 3.6),func= lambda:self.change_Hotkey('Hotkey_Attack'), text='Hotkey_Attack', keyText=True))
        self.controlsButtons.append(Button((self.rect.centerx * 1.35, self.rect.midbottom[1] - TILE_SIZE * 4.8),func= lambda:self.change_Hotkey('Hotkey_HeavyAttack'), text='Hotkey_HeavyAttack', keyText=True))
        self.controlsButtons.append(Button((self.rect.centerx * 1.35, self.rect.midbottom[1] - TILE_SIZE * 1.2),func=Scripts.DataManager.resetHotkeys , icon=UI_Assets.ICON_RESET))
        self.keybindTexts.append((font.render("Move Up", False, (0,0,0)), (self.rect.centerx * 0.4, self.rect.midbottom[1] - TILE_SIZE * 6.8)))
        self.keybindTexts.append((font.render("Move Down", False, (0,0,0)), (self.rect.centerx * 0.4, self.rect.midbottom[1] - TILE_SIZE * 5.8)))
        self.keybindTexts.append((font.render("Move Left", False, (0,0,0)), (self.rect.centerx * 0.4, self.rect.midbottom[1] - TILE_SIZE * 4.7)))
        self.keybindTexts.append((font.render("Move Right", False, (0,0,0)), (self.rect.centerx * 0.4, self.rect.midbottom[1] - TILE_SIZE * 3.6)))
        self.keybindTexts.append((font.render("Boost", False, (0,0,0)), (self.rect.centerx * 0.4, self.rect.midbottom[1] - TILE_SIZE * 2.4)))
        self.keybindTexts.append((font.render("Close Game", False, (0,0,0)), (self.rect.centerx * 0.4, self.rect.midbottom[1] - TILE_SIZE * 1.2)))           
        self.keybindTexts.append((font.render("Reset Hotkeys", False, (0,0,0)), (self.rect.centerx * 0.95, self.rect.midbottom[1] - TILE_SIZE * 1.2)))
        self.keybindTexts.append((font.render("Attack", False, (0,0,0)), (self.rect.centerx * 0.95, self.rect.midbottom[1] - TILE_SIZE * 3.6)))
        self.keybindTexts.append((font.render("HeavyAttack", False, (0,0,0)), (self.rect.centerx * 0.95, self.rect.midbottom[1] - TILE_SIZE * 4.8))) 

    def change_Hotkey(self, key):
        self.keyChange = True
        self.keyToChange = key

    async def draw(self):
      super().draw()
      while self.keyChange:   
          await asyncio.sleep(0)           
          for event in pygame.event.get():
              if event.type == pygame.KEYDOWN:
                  if event.key == pygame.K_ESCAPE:
                      self.keyChange = False
                      break
                  Scripts.DataManager.dataJson[self.keyToChange] = event.key
                  Scripts.DataManager.saveData()
                  self.keyChange = False
                  
      for controlsButtons in self.controlsButtons:
          controlsButtons.update(self.cameraSurface)
      for kbTextes, position in self.keybindTexts:
          self.cameraSurface.blit(kbTextes, position)
      if self.keyChange:
          self.cameraSurface.blit(self.keyModal, self.keyModalRect)

class StatsMenu(Menu):
    def __init__(self, surface, left, top, size: tuple, enabled, gameState):
        super().__init__(surface, left, top, gameState, enabled=enabled, size=size)
        self.buttons.append(Button((self.rect.centerx + 325, self.rect.centery - 325), text="x", func=self.mainMenu))  
        self.top5Highscores = Scripts.DataManager.dataJson['top5Highscores']
        
        self.font = Scripts.AssetsManager.font

    def draw(self):
        super().draw()
        
        statsText = self.font.render("Stats", True, (0, 0, 0))  
        text_rect = statsText.get_rect(center=(self.rect.centerx, self.rect.top + 50))  
        self.cameraSurface.blit(statsText, text_rect)
        
        for index, score in enumerate(self.top5Highscores):
            score_text = self.font.render(f"{index + 1}. {score}", True, (0, 0, 0))
            score_rect = score_text.get_rect(center=(self.rect.centerx, self.rect.top + 100 + index * 40))
            self.cameraSurface.blit(score_text, score_rect)