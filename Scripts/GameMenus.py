import pygame
from Button import *
from Player import *

class Menu:
    def __init__(self, left, top):
        self.displaySurface = pygame.display.get_surface()
        self.left = left
        self.top = top
        self.buttons = []
        self.texts = []
        self.rect = pygame.FRect(self.left, self.top, 600, 900)

    def draw(self):
        pygame.draw.rect(self.displaySurface, (240,240,240), self.rect, 0, 0)
        for button in self.buttons:
            button.update(self.displaySurface)
        for text, textRect in self.texts:
            self.displaySurface.blit(text, textRect)

class EndGameMenu(Menu):
    def __init__(self, left, top, gameState, score):
        super().__init__(left, top)
        self.ending = True
        self.gameState = gameState
        self.buttons.append(Button((self.rect.centerx, self.rect.centery), text="Play Again", func=self.newGame))
        self.buttons.append(Button((self.rect.centerx, self.rect.centery + 96), text="Main Menu", func=self.mainMenu))
        self.buttons.append(Button((self.rect.centerx, self.rect.centery + 192), text="Quit", func=self.quitGame))
        self.texts.append((font.render(str(score), False, (0,0,0)), None))
        self.texts[0] = (self.texts[0][0], self.texts[0][0].get_frect(center=(self.rect.centerx, self.rect.centery - 96)))
    
    def newGame(self):
        self.ending = False

    def mainMenu(self):
        self.ending = False
        self.gameState['gaming'] = False
    
    def quitGame(self):
        self.ending = False
        self.gameState['quit'] = True