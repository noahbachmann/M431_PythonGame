import pygame
from AssetsManager import font, BUTTON_IMAGE
from Button import *
from UpgradesMenu import *

class HUDController():
    def __init__(self, player, hudSpritesGroup):
        self.player = player
        self.pause = False
        self.hudSpritesGroup = hudSpritesGroup
        self.goldText = font.render(str(self.player.gold), False, (240,240,240))        
        self.goldTextRect = self.goldText.get_frect(midtop = (800, 800))  
        self.upgradeButton = Button((900,100),BUTTON_IMAGE,hudSpritesGroup, "Upgrades", self.toggleSettings, (64,64))
        self.upgradeMenu = UpgradesMenu(self.player)
    
    def draw(self, surface):
        self.upgradeButton.draw(surface)
        surface.blit(self.goldText, self.goldTextRect)

    def update(self, surface):
        self.goldText = font.render(str(self.player.gold), False, (240,240,240))
        self.upgradeButton.update(surface)
        self.draw(surface)

    def toggleSettings(self):
        self.pause = not self.pause
        if self.pause:
            self.upgradeMenu.draw()