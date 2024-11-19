import pygame
from AssetsManager import font

class HUDController():
    def __init__(self, player):
        self.player = player
        self.goldText = font.render(str(self.player.gold), False, (240,240,240))        
        self.goldTextRect = self.goldText.get_frect(midtop = (800, 800))  

    def draw(self, surface):
        surface.blit(self.goldText, self.goldTextRect)

    def update(self, surface):
        self.goldText = font.render(str(self.player.gold), False, (240,240,240))
        self.draw(surface)