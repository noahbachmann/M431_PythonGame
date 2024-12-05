import pygame
import sys
import Scripts.Settings
from Scripts.Round import *
from Scripts.GameMenus import *

pygame.init()
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
screenSize = screen.get_size()
if screenSize[1] < Scripts.Settings.WINDOW_SIZE:
    Scripts.Settings.WINDOW_SIZE = screenSize[1]
cameraSurface = pygame.Surface((Scripts.Settings.WINDOW_SIZE, Scripts.Settings.WINDOW_SIZE))
offset = (screenSize[0] // 2 - Scripts.Settings.WINDOW_SIZE // 2, screenSize[1] // 2 - Scripts.Settings.WINDOW_SIZE // 2)
pygame.display.set_caption("My Space Shooter")
gameState = {'gaming': "MainMenu", 'quit': False}

while not gameState['quit']:
    if gameState['gaming'] == "Gaming":
        round = Round(cameraSurface, screen, gameState)
        score = round.run()
        if score < 0:
            if gameState['quit']:
                pygame.quit()
                sys.exit()
            else:
                continue
        endGameMenu = EndGameMenu(cameraSurface, (Scripts.Settings.WINDOW_SIZE - 600) // 2, 50,(600,600), gameState, True, score)
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
        MainMenuGame = MainMenu(cameraSurface, (Scripts.Settings.WINDOW_SIZE - 650) // 2, 50,(650,650), True, gameState)
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
        SettingsMenuGame = SettingsMenu(cameraSurface, (Scripts.Settings.WINDOW_SIZE - 650) // 2,  50,(650,650), True, gameState)
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