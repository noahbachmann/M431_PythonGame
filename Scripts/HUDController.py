import pygame
from math import ceil
from Settings import *
from AssetsManager import font, BUTTON_IMAGE, Heart_Assets, Energybar_Assets
from Button import *
from GameMenus import *
from Player import *

class HUDController:
    def __init__(self, surface, player:Player, gameState, hudSpritesGroup):
        self.player = player
        self.playerHealth = self.player.health
        self.pause = False
        self.hudSpritesGroup = hudSpritesGroup
        self.goldText = font.render(str(self.player.gold), False, (240,240,240))        
        self.goldTextRect = self.goldText.get_frect(midtop = (800, 800))  
        self.upgradeButton = Button((900,100),BUTTON_IMAGE, "Upgrades", self.toggleSettings, (64,64))
        self.upgradeMenu = UpgradesMenu(surface, 200, 50, self.player, gameState)
        self.hearts = []
        self.energyBar = EnergyBar((WINDOW_SIZE/2 - 64, 32), self.player, Energybar_Assets.ENERGYBAR_ENERGY, Energybar_Assets.ENERGYBAR_BACK, (128,32))
        self.showHealth()
    
    def draw(self, surface):
        self.upgradeButton.draw(surface)
        self.energyBar.draw(surface)
        surface.blit(self.goldText, self.goldTextRect)
        for heart in self.hearts:
            heart.draw(surface)
        if self.pause:
            self.upgradeMenu.draw(surface)

    def update(self, surface):
        self.goldText = font.render(str(self.player.gold), False, (240,240,240))
        self.upgradeButton.update(surface)
        if self.playerHealth != self.player.health:
            if self.pause:
                self.healthUpgrade()
            else:
                self.takeDamage()
        self.draw(surface)

    def toggleSettings(self):
        self.pause = not self.pause

    def showHealth(self):
        x = 32
        y = 32
        maxHealth = self.player.maxHealth // 2
        for i in range(maxHealth):
            self.hearts.append(Heart((x,y),Heart_Assets.HEART_FULL, (32,32)))
            x += 64
        if self.player.maxHealth % 2 != 0:
            self.hearts.append(Heart((x,y),Heart_Assets.HALFHEART_FULL, (32,32)))
        
    def takeDamage(self):
        if self.player.maxHealth % 2 != 0 and self.player.health == self.player.maxHealth - 1:
            self.hearts[len(self.hearts)-1].newImage(Heart_Assets.HALFHEART_EMPTY)
        elif self.player.health % 2 != 0:
            self.hearts[self.player.health // 2].newImage(Heart_Assets.HEART_HALFFULL)
        else:
            self.hearts[self.player.health // 2].newImage(Heart_Assets.HEART_EMPTY)
        self.playerHealth = self.player.health
    
    def healthUpgrade(self):
        x = 32
        y = 32
        if self.player.maxHealth / 2 > len(self.hearts):
            if self.player.maxHealth == self.player.health:
                self.hearts.append(Heart((x+(64*len(self.hearts)),y),Heart_Assets.HALFHEART_FULL, (32,32)))
            else:
                self.hearts.append(Heart((x+(64*len(self.hearts)),y),Heart_Assets.HALFHEART_EMPTY, (32,32)))
        if self.player.health != self.playerHealth:
            if self.player.health % 2 == 0:
                self.hearts[(self.player.health // 2)-1].newImage(Heart_Assets.HEART_FULL)
            else:
                self.hearts[self.player.health // 2].newImage(Heart_Assets.HEART_HALFFULL)           
            if self.player.maxHealth % 2 == 0 and self.player.maxHealth != self.player.health:
                self.hearts[len(self.hearts)-1].newImage(Heart_Assets.HEART_EMPTY)
            self.playerHealth = self.player.health

class Heart(pygame.sprite.Sprite):
    def __init__(self, pos:tuple, image, size:tuple = None ):
        super().__init__()
        if size:
            self.image = pygame.transform.scale(image, size)
            self.size = size
        else:
            self.image = image
        self.rect = self.image.get_frect(center=pos)
    
    def newImage(self, image):
        if self.size:
            self.image = pygame.transform.scale(image, self.size)
        else:
            self.image = image 

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class EnergyBar(pygame.sprite.Sprite):
    def __init__(self, pos:tuple, player, barImage, image, size:tuple = None):
        super().__init__()
        self.player = player
        if size:
            self.image = pygame.transform.scale(image, size)
            self.barImage = pygame.transform.scale(barImage, size)
            self.size = size
        else:
            self.image = image
            self.barImage = barImage
        self.rect = self.image.get_frect(midleft=pos)

    def draw(self, surface):
        energyPercentage = self.player.boostAmount / self.player.boostTank
        barWidth = self.size[0] * energyPercentage
        surface.blit(self.image, self.rect)
        surface.blit(self.barImage, self.rect, (0,0,barWidth,self.size[0]))
