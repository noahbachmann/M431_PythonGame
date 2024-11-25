import pygame
from Button import *
from Player import *

class Menu:
    def __init__(self, surface, left, top, color = None, enabled = False, size:tuple = None):
        self.cameraSurface = surface
        self.left = left
        self.top = top
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

class EndGameMenu(Menu):
    def __init__(self, surface, left, top, size:tuple, enabled, gameState, score):
        super().__init__(surface, left, top, enabled=enabled, size=size)
        self.gameState = gameState
        self.buttons.append(Button((self.rect.centerx, self.rect.centery), text="Play Again", func=self.newGame))
        self.buttons.append(Button((self.rect.centerx, self.rect.centery + 96), text="Main Menu", func=self.mainMenu))
        self.buttons.append(Button((self.rect.centerx, self.rect.centery + 192), text="Quit", func=self.quitGame))
        self.texts.append((font.render(str(score), False, (0,0,0)), None))
        self.texts[0] = (self.texts[0][0], self.texts[0][0].get_frect(center=(self.rect.centerx, self.rect.centery - 96)))
    
    def newGame(self):
        self.enabled = False

    def mainMenu(self):
        self.enabled = False
        self.gameState['gaming'] = False
    
    def quitGame(self):
        self.enabled = False
        self.gameState['quit'] = True

class UpgradesMenu(Menu):
    def __init__(self, surface, left, top, player, color = None, size:tuple = None):
        super().__init__(surface,left,top,color,size=size)
        self.player = player
        self.left = left
        self.top = top
        self.upgrades = ["atkSpeed", "atkDmg", "health", "heavyCd", "boostTank", "boostStrength"]
        self.upgradesLevel = [0,0,0,0,0,0]
        self.generatedButtons = False

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
                self.buttons.append(Button((x,y),BUTTON_IMAGE,"+", lambda j=i: self.player.upgrade(self.upgrades[j-1], self.upgradesLevel)))
        self.generatedButtons = True

    def draw(self, surface):
        self.general()
        for button in self.buttons:
            button.update(surface)