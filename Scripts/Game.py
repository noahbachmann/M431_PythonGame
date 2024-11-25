import pygame
import sys
import time
from Settings import *
from Round import *
from GameMenus import *

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("My Space Shooter")
gameState = {'gaming': False, 'quit': False}



while not gameState['quit']:
    if gameState['gaming']:
        round = Round()
        score = round.run()
        if score < 0:
            gameState['quit'] = True
            continue
        endGameMenu = EndGameMenu(200, 50,(600,600), True, gameState, score)
        while endGameMenu.enabled: 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameState['quit'] = True
                    continue       
            endGameMenu.draw()
            pygame.display.update(),

    if not gameState['gaming']:
        MainMenuGame = MainMenu(250, 250,(650,650), True, gameState, 5)
        while MainMenuGame.enabled:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameState['quit'] = True
                    continue 
                screen.fill((7, 0, 25))
                MainMenuGame.draw()
                pygame.display.update()
         

pygame.quit()