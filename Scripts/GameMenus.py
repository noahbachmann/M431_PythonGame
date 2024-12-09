import pygame
from Scripts.Button import *
from Scripts.AssetsManager import UI_Assets, Crosshair
from Scripts.Settings import *
from tkinter import filedialog
import Scripts.DataManager


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
            self.color = (240,240,240)
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
    def __init__(self, surface, left, top, player, gameState, color = None, size:tuple = None):
        super().__init__(surface,left,top, gameState, color,size=size)
        self.player = player
        self.upgrades = ["Upgrades", "atkSpeed", "atkDmg", "health", "heavyCd", "boostTank", "boostStrength"]
        self.upgradesLevel = [0,0,0,0,0,0]
        self.upgradesMultiplier = [25,50,50,15,25,50]
        self.generatedButtons = False
        self.buttons.append(Button((self.rect.centerx - TILE_SIZE, self.rect.midbottom[1] - TILE_SIZE * 1.5), func=self.mainMenu, icon=UI_Assets.ICON_HOME))
        self.buttons.append(Button((self.rect.centerx + TILE_SIZE, self.rect.midbottom[1] - TILE_SIZE * 1.5), func=self.quitGame, icon=UI_Assets.ICON_EXIT))

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
        pygame.draw.rect(self.cameraSurface, (240,240,240), self.rect, 0, 0)
        self.general()
        for button in self.buttons:
            button.update(surface)

class MainMenu(Menu):
    def __init__(self, surface, left, top, size:tuple, enabled, gameState):
        super().__init__(surface, left, top, gameState, enabled=enabled, size=size)
        self.buttons.append(Button((self.rect.centerx, self.rect.centery), func=self.newGame, icon=UI_Assets.ICON_PLAY))   
        self.buttons.append(Button((self.rect.centerx, self.rect.centery + 90), func=self.settings, icon=UI_Assets.ICON_SETTINGS))   
        self.buttons.append(Button((self.rect.centerx, self.rect.centery + 180), func=self.quitGame, icon=UI_Assets.ICON_EXIT))   
        self.texts.append((font.render(str("My Space Shooter"), False, (0,0,0)), None))
        self.texts[0] = (self.texts[0][0], self.texts[0][0].get_frect(center=(self.rect.centerx, self.rect.centery - 90)))

    def newGame(self):
        self.enabled = False
        self.gameState['gaming'] = "Gaming"

    def settings(self):
        self.enabled = False
        self.gameState['gaming'] = "Settings"

class SettingsMenu(Menu):
    def __init__(self, surface, left, top, size:tuple, enabled, gameState):
        super().__init__(surface, left, top, gameState, enabled=enabled, size=size)
        self.texts.append((font.render(str("Settings"), False, (0,0,0)), None))
        self.texts[0] = (self.texts[0][0], self.texts[0][0].get_frect(center=(self.rect.centerx, self.rect.centery - 290)))
        self.buttons.append(Button((self.rect.centerx + 325, self.rect.centery - 325), func=self.mainMenu, icon=UI_Assets.ICON_HOME))   
        self.buttons.append(Button((self.rect.centerx + 125, self.rect.centery - 50), text="upload", func=self.cursorUpload))   
        self.cursor = Crosshair.Crosshair1
            

    def cursorUpload(self,event=None):
        
        cursorPath = filedialog.askopenfilename()
        if cursorPath:
            clock = pygame.time.Clock()
            cursor_image = pygame.image.load(cursorPath).convert_alpha()
            cursor_image = pygame.transform.scale(cursor_image, (32, 32))
            self.cursor = cursor_image
            hotspot = (cursor_image.get_width() // 2, cursor_image.get_height() // 2)
            pygame.mouse.set_cursor((hotspot[0], hotspot[1]), cursor_image)
            Scripts.DataManager.dataJson['customCrosshair'] = True
            Scripts.DataManager.dataJson['crosshair'] = cursorPath
            Scripts.DataManager.saveData()

    
    def draw(self):
        super().draw()
        self.cameraSurface.blit(self.cursor, (125, 125))

