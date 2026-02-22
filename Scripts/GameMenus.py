import pygame
from Scripts.Button import *
from Scripts.AssetsManager import UI_Assets, karmaticArcadeFont_40, font, font_32
from Scripts.Settings import *

class Menu:
    def __init__(self, surface, left, top, gameState, color = None, enabled = False, size:tuple = None):
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
    
    def mainMenu(self):
        self.enabled = False
        self.gameState = 'menu'

class EndGameMenu(Menu):
    def __init__(self, surface, left, top, size:tuple, gameState, enabled, score):
        super().__init__(surface, left, top, gameState, enabled=enabled, size=size)
        self.buttons.append(Button((self.rect.centerx, self.rect.centery + TILE_SIZE), func=self.newGame, icon=UI_Assets.ICON_PLAY))

        self.texts.append((karmaticArcadeFont_40.render(str(score), False, (0,0,0)), None))
        self.texts[0] = (self.texts[0][0], self.texts[0][0].get_frect(center=(self.rect.centerx, self.rect.centery - TILE_SIZE)))

    def newGame(self):
        self.enabled = False

class UpgradesMenu(Menu):
    def __init__(self, surface, left, top, player, gameState, hudController, color = None, size:tuple = None):
        super().__init__(surface,left,top, gameState, color,size=size)
        self.player = player
        self.upgrades = ["Upgrades", "atkSpeed", "atkDmg", "health", "heavy cd", "boost tank", "boost power"]
        self.upgradesLevel = [0,0,0,0,0,0]
        self.upgradesMultiplier = [20,40,40,15,20,40]
        self.generatedButtons = False
        self.hudController = hudController
        self.buttons.append(Button((self.rect.centerx - TILE_SIZE, self.rect.midbottom[1] - TILE_SIZE), func=self.endPause, icon=UI_Assets.ICON_PLAY))
        self.buttons.append(Button((self.rect.centerx + TILE_SIZE, self.rect.midbottom[1] - TILE_SIZE), func=self.restart, icon=UI_Assets.ICON_RESET))
        self._cachedGold = self.player.gold
        goldSurface = font_32.render(f"$ {self.player.gold}", False, (250, 188, 0))
        goldRect = goldSurface.get_frect(center=(self.rect.centerx, self.rect.top + 30))
        self.texts.append((goldSurface, goldRect))
        self._upgradesLevelSnapshot = None
        self._cachedGeneralTexts = []

    def restart(self):
      self.hudController.pause = False
      self.enabled = False
      self.player.health = 0

    def general(self):
        upgrdHeight = self.rect.height - (self.rect.height // 4)
        header_height = 60
        rows_area = upgrdHeight - header_height
        name_x = self.rect.left + 24
        level_x = self.rect.left + int(self.rect.width * 0.55)
        btn_x = self.rect.left + int(self.rect.width * 0.68)
        cost_x = self.rect.left + int(self.rect.width * 0.85)
        if self.upgradesLevel != self._upgradesLevelSnapshot:
            self._upgradesLevelSnapshot = self.upgradesLevel[:]
            self._cachedGeneralTexts = []
            for i in range(1, 8):
                y = self.rect.top + header_height + (rows_area / 14) * (i * 2 - 1)
                upgradeText = font_32.render(self.upgrades[i - 1], False, (0, 0, 0))
                self._cachedGeneralTexts.append((upgradeText, upgradeText.get_frect(midleft=(name_x, y))))
                levelText = font_32.render("Lvl." if i == 1 else str(self.upgradesLevel[i - 2]), False, (0, 0, 0))
                self._cachedGeneralTexts.append((levelText, levelText.get_frect(center=(level_x, y))))
                if not self.generatedButtons and i > 1:
                    self.buttons.append(Button((btn_x, y), UI_Assets.BUTTON_32x32, "+", lambda j=i: self.player.upgrade(self.upgrades[j - 1], self.upgradesLevel)))
                costText = font_32.render("Cost" if i == 1 else str((self.upgradesLevel[i - 2] * self.upgradesMultiplier[i - 2]) + (self.upgradesMultiplier[i - 2] * 2)), False, (0, 0, 0))
                self._cachedGeneralTexts.append((costText, costText.get_frect(center=(cost_x, y))))
            self.generatedButtons = True
        for surf, rect in self._cachedGeneralTexts:
            self.cameraSurface.blit(surf, rect)

    def draw(self, surface):
        pygame.draw.rect(self.cameraSurface, self.color, self.rect, 0, 0)
        self.general()
        for button in self.buttons:
            button.update(surface)
        if self.player.gold != self._cachedGold:
            self._cachedGold = self.player.gold
            self.texts[0] = (font_32.render(f"$ {self.player.gold}", False, (250, 188, 0)), self.texts[0][1])
        for text, textRect in self.texts:
            self.cameraSurface.blit(text, textRect)

    def endPause(self):
        self.hudController.pause = False
        self.enabled = False

class MainMenu(Menu):
    def __init__(self, surface, left, top, size:tuple, enabled, gameState):
        super().__init__(surface, left, top, gameState, enabled=enabled, size=size)
        self.buttons.append(Button((self.rect.centerx, self.rect.centery + TILE_SIZE), func=self.newGame, icon=UI_Assets.ICON_PLAY))  
        self.texts.append((karmaticArcadeFont_40.render(str("Space Shooter"), False, (0,0,0)),))
        self.texts[0] = (self.texts[0][0], self.texts[0][0].get_frect(center=(self.rect.centerx, self.rect.centery - TILE_SIZE)))
        
    def newGame(self):
        self.enabled = False
