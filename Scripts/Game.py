import pygame
import sys
import time
from Settings import *
from Round import *
from GameMenus import *
#test
pygame.init()
cameraSurface = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
screenSize = screen.get_size()
offset = (screenSize[0] // 2 - WINDOW_WIDTH // 2, screenSize[1] // 2 - WINDOW_HEIGHT // 2)
pygame.display.set_caption("My Space Shooter")
gameState = {'gaming': "MainMenu", 'quit': False}



while not gameState['quit']:
    if gameState['gaming'] == "Gaming":
        round = Round(cameraSurface, screen)
        score = round.run()
        if score < 0:
            pygame.quit()
            sys.exit()
        endGameMenu = EndGameMenu(cameraSurface, 200, 50,(600,600), True, gameState, score)
        while endGameMenu.enabled: 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()    
            screen.fill((0,0,0))
            endGameMenu.draw()
            screen.blit(cameraSurface, cameraSurface.get_frect(center = (screenSize[0]//2, screenSize[1]//2)))
            pygame.display.update()

    elif gameState['gaming'] == "MainMenu":
        MainMenuGame = MainMenu(cameraSurface, 200, 50,(650,650), True, gameState)
        while MainMenuGame.enabled:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    continue 
            screen.fill((0,0,0))
            cameraSurface.fill((7, 0, 25))
            MainMenuGame.draw()
            screen.blit(cameraSurface, cameraSurface.get_frect(center = (screenSize[0]//2, screenSize[1]//2)))
            pygame.display.update()
            
    elif gameState['gaming'] == "Settings":
        SettingsMenuGame = SettingsMenu(cameraSurface, 200, 50,(650,650), True, gameState)
        while SettingsMenuGame.enabled:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:   
                    gameState['quit'] = True
                    pygame.quit()
                    sys.exit()
                    continue 
            screen.fill((0,0,0))
            cameraSurface.fill((7, 0, 25))
            SettingsMenuGame.draw()
            screen.blit(cameraSurface, cameraSurface.get_frect(center = (screenSize[0]//2, screenSize[1]//2)))
            pygame.display.update() 


pygame.quit()