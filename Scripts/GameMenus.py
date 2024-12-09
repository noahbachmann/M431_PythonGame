import pygame
from Button import *
from AssetsManager import UI_Assets
from Settings import *
from tkinter import filedialog
import tkinter
import AssetsManager
import DataManager


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
        DataManager.saveData()

    def mainMenu(self):
        self.enabled = False
        self.gameState['gaming'] = "MainMenu"
        DataManager.saveData()

class EndGameMenu(Menu):
    def __init__(self, surface, left, top, size:tuple, gameState, enabled,  score):
        super().__init__(surface, left, top, gameState, enabled=enabled, size=size)
        self.gameState = gameState
        self.buttons.append(Button((self.rect.centerx, self.rect.centery), text="Play Again", func=self.newGame))
        self.buttons.append(Button((self.rect.centerx, self.rect.centery + 96), text="Main Menu", func=self.mainMenu))
        self.buttons.append(Button((self.rect.centerx, self.rect.centery + 192), text="Exit", func=self.quitGame))
        self.texts.append((font.render(str(score), False, (0,0,0)), None))
        self.texts[0] = (self.texts[0][0], self.texts[0][0].get_frect(center=(self.rect.centerx, self.rect.centery - 96)))
        
    def newGame(self):
        self.enabled = False

class UpgradesMenu(Menu):
    def __init__(self, surface, left, top, player, gameState, color = None, size:tuple = None):
        super().__init__(surface,left,top, gameState, color,size=size)
        self.player = player
        self.gameState = gameState
        self.left = left
        self.top = top
        self.upgrades = ["atkSpeed", "atkDmg", "health", "heavyCd", "boostTank", "boostStrength"]
        self.upgradesLevel = [0,0,0,0,0,0]
        self.generatedButtons = False
        self.buttons.append(Button((self.rect.centerx, self.rect.centery + self.rect.height), text="Main Menu", func=self.mainMenu))
        self.buttons.append(Button((self.rect.centerx + 128, self.rect.centery + self.rect.height), text="Exit", func=self.quitGame))

    def general(self):
        rect = pygame.FRect(self.left, self.top, 600, 900)
        pygame.draw.rect(self.cameraSurface, (240,240,240), rect, 0, 0)
        for i in range(1,7):
            x = rect.left + (rect.width / 3)
            y = rect.top + (rect.height /12) * (i*2 - 1) 
            upgradeText = font.render(self.upgrades[i-1], False, (0,0,0))
            upgradeTextRect = upgradeText.get_frect(center = (x,y))
            self.cameraSurface.blit(upgradeText, upgradeTextRect)
            x += (rect.width / 3)*1.25
            levelText = font.render(str(self.upgradesLevel[i-1]), False, (0,0,0))
            levelTextRect = levelText.get_frect(center = (x,y))
            self.cameraSurface.blit(levelText, levelTextRect)
            x += (rect.width / 3)*0.5
            if not self.generatedButtons:
                self.buttons.append(Button((x,y),UI_Assets.BUTTON_32x32,"+", lambda j=i: self.player.upgrade(self.upgrades[j-1], self.upgradesLevel)))
        self.generatedButtons = True

    def draw(self, surface):
        self.general()
        for button in self.buttons:
            button.update(surface)

class MainMenu(Menu):
    def __init__(self, surface, left, top, size:tuple, enabled, gameState):
        super().__init__(surface, left, top, gameState, enabled=enabled, size=size)
        self.buttons.append(Button((self.rect.centerx, self.rect.centery), text="Play", func=self.newGame))   
        self.buttons.append(Button((self.rect.centerx, self.rect.centery + 90), text="Settings", func=self.settings))   
        self.buttons.append(Button((self.rect.centerx, self.rect.centery + 180), text="Exit", func=self.quitGame))   
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
        self.buttons.append(Button((self.rect.centerx + 325, self.rect.centery - 325), text="x", func=self.mainMenu))   
        self.buttons.append(Button((self.rect.centerx + 125, self.rect.centery - 50), text="upload", func=self.cursorUpload))   
        self.cursor = AssetsManager.Crosshair.Crosshair1
            

    def cursorUpload(self,event=None):
        
        cursorPath = filedialog.askopenfilename()
        if cursorPath:
            clock = pygame.time.Clock()
            cursor_image = pygame.image.load(cursorPath).convert_alpha()
            cursor_image = pygame.transform.scale(cursor_image, (32, 32))
            self.cursor = cursor_image
            hotspot = (cursor_image.get_width() // 2, cursor_image.get_height() // 2)
            pygame.mouse.set_cursor((hotspot[0], hotspot[1]), cursor_image)
            DataManager.dataJson['crosshair'] = cursorPath
            DataManager.saveData()

    
    def draw(self):
        super().draw()
        self.cameraSurface.blit(self.cursor, (125, 125))



  
