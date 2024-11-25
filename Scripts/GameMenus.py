import pygame
from Button import *

class Menu:
    def __init__(self, left, top, color = None, enabled = False, size:tuple = None):
        self.displaySurface = pygame.display.get_surface()
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
        pygame.draw.rect(self.displaySurface, self.color, self.rect, 0, 0)
        for button in self.buttons:
            button.update(self.displaySurface)
        for text, textRect in self.texts:
            self.displaySurface.blit(text, textRect)

class EndGameMenu(Menu):
    def __init__(self, left, top, size:tuple, enabled, gameState, score):
        super().__init__(left, top, enabled=enabled, size=size)
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


class MainMenu(Menu):
    def __init__(self, left, top, size:tuple, enabled, gameState, score):
        super().__init__(left, top, enabled=enabled, size=size)
        self.gameState = gameState

        
        self.buttons.append(Button((self.rect.centerx, self.rect.centery), text="Play", func=self.newGame))   
        self.buttons.append(Button((self.rect.centerx, self.rect.centery + 90), text="Settings", func=self.quitGame))   
        self.buttons.append(Button((self.rect.centerx, self.rect.centery + 180), text="Exit", func=self.quitGame))   
        self.texts.append((font.render(str("My Space Shooter"), False, (0,0,0)), None))
        self.texts[0] = (self.texts[0][0], self.texts[0][0].get_frect(center=(self.rect.centerx, self.rect.centery - 90)))


    def newGame(self):
        self.enabled = False
        self.gameState['gaming'] = True


    def mainMenu(self):
        self.enabled = False
        self.gameState['gaming'] = False
    
    def quitGame(self):
        self.enabled = False
        self.gameState['quit'] = True