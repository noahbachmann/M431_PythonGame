import pygame
import sys
import time
from Settings import *
from Round import *
from GameMenus import *

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("My Space Shooter")
gameState = {'gaming': "MainMenu", 'quit': False}



while not gameState['quit']:
    if gameState['gaming'] == "Gaming":
        round = Round()
        score = round.run()
        if score < 0:
            gameState['quit'] = True
            continue
        endGameMenu = EndGameMenu(200, 50,(600,600), True, gameState, score)
        while endGameMenu.enabled: 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    continue       
            endGameMenu.draw()
            pygame.display.update()

    if gameState['gaming'] == "MainMenu":
        MainMenuGame = MainMenu(200, 50,(650,650), True, gameState)
        while MainMenuGame.enabled:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    continue 
            screen.fill((7, 0, 25))
            MainMenuGame.draw()
            pygame.display.update()
            
    if gameState['gaming'] == "Settings":
        SettingsMenuGame = SettingsMenu(200, 50,(650,650), True, gameState)
        while SettingsMenuGame.enabled:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:   
                    gameState['quit'] = True
                    pygame.quit()
                    sys.exit()
                    continue 
            screen.fill((7, 0, 25))
            SettingsMenuGame.draw()
            pygame.display.update() 


pygame.quit()