import pygame
from math import ceil
from Settings import *
from AssetsManager import font, BUTTON_IMAGE, Heart_Assets
from Button import *
from UpgradesMenu import *

class HUDController:
    def __init__(self, player, hudSpritesGroup):
        self.player = player
        self.playerHealth = self.player.health
        self.pause = False
        self.hudSpritesGroup = hudSpritesGroup
        self.goldText = font.render(str(self.player.gold), False, (240,240,240))        
        self.goldTextRect = self.goldText.get_frect(midtop = (800, 800))  
        self.upgradeButton = Button((900,100),BUTTON_IMAGE, "Upgrades", self.toggleSettings, (64,64), hudSpritesGroup)
        self.upgradeMenu = UpgradesMenu(self.player)
        self.hearts = []
        self.showHealth()
    
    def draw(self, surface):
        self.upgradeButton.draw(surface)
        surface.blit(self.goldText, self.goldTextRect)
        for heart in self.hearts:
            heart.draw(surface)
        if self.pause:
            self.upgradeMenu.draw(surface)

    def update(self, surface):
        self.goldText = font.render(str(self.player.gold), False, (240,240,240))
        self.upgradeButton.update(surface)
        if self.playerHealth != self.player.health:
            self.takeDamage()
        self.draw(surface)

    def toggleSettings(self):
        self.pause = not self.pause

    def showHealth(self):
        x = 32
        y = 32
        maxHealth = self.player.maxHealth // 2
        for i in range(maxHealth):
            self.hearts.append(Heart((x,y),Heart_Assets.HEART_FULL, self.hudSpritesGroup, (32,32)))
            x += 64
        if self.player.maxHealth % 2 != 0:
            self.hearts.append(Heart((x,y),Heart_Assets.HALFHEART_FULL, self.hudSpritesGroup, (32,32)))
        
    def takeDamage(self):
        if self.player.maxHealth % 2 != 0 and self.player.health == self.player.maxHealth - 1:
            self.hearts[self.hearts.count -1].newImage(Heart_Assets.HALFHEART_EMPTY)
        elif self.player.health % 2 != 0:
            self.hearts[self.player.health // 2].newImage(Heart_Assets.HEART_HALFFULL)
        else:
            self.hearts[self.player.health // 2].newImage(Heart_Assets.HEART_EMPTY)
        self.playerHealth = self.player.health

class Heart(pygame.sprite.Sprite):
    def __init__(self, pos:tuple, image, groups, size:tuple = None ):
        super().__init__(groups)
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
    def __init__(self, pos:tuple, player, barImage, image, groups, size:tuple = None):
        super().__init__(groups)
        self.player = player
        if size:
            self.image = pygame.transform.scale(image, size)
            self.barImage = pygame.transform.scale(barImage, size)
            self.size = size
        else:
            self.image = image
            self.barImage = barImage
        self.rect = self.image.get_frect(centerleft=pos)

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        surface.blit(self.barImage, self.rect)
