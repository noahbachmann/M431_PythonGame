import pygame
from AssetsManager import font

class UpgradesMenu:
    def __init__(self, player):
        self.player = player
        self.displaySurface = pygame.display.get_surface()
        self.left = 200
        self.top = 50
        self.upgrades = ["atkSpeed", "atkDmg", "health", "heavyCd", "boostTank", "boostStrength"]
        self.upgradesLevel = [0,0,0,0,0,0]

    def general(self):
        rect = pygame.FRect(self.left, self.top, 600, 900)
        pygame.draw.rect(self.displaySurface, (240,240,240), rect, 0, 0)
        for i in range(1,7):
           x = rect.left + (rect.width / 3)
           y = rect.top + (rect.height /12) * (i*2 - 1) 
           upgradeText = font.render(self.upgrades[i-1], False, (0,0,0))
           upgradeTextRect = upgradeText.get_frect(center = (x,y))
           self.displaySurface.blit(upgradeText, upgradeTextRect)
           x += (rect.width / 3)*1.5
           levelText = font.render(f"{str(self.upgradesLevel[i-1])} +", False, (0,0,0))
           levelTextRect = levelText.get_frect(center = (x,y))
           self.displaySurface.blit(levelText, levelTextRect)

    def draw(self):
        self.general()