import pygame
import sys
import Scripts.Settings
from Scripts.Round import *
from Scripts.GameMenus import *
import sys 
import time
import Scripts.DataManager
import Scripts.AssetsManager
import json

pygame.init()
Scripts.DataManager.loadData()
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
screenSize = screen.get_size()
if screenSize[1] < Scripts.Settings.WINDOW_SIZE:
    Scripts.Settings.WINDOW_SIZE = screenSize[1]
cameraSurface = pygame.Surface((Scripts.Settings.WINDOW_SIZE, Scripts.Settings.WINDOW_SIZE))
offset = (screenSize[0] // 2 - Scripts.Settings.WINDOW_SIZE // 2, screenSize[1] // 2 - Scripts.Settings.WINDOW_SIZE // 2)
pygame.display.set_caption("My Space Shooter")
gameState = {'gaming': "MainMenu", 'quit': False}

if Scripts.DataManager.dataJson['customCrosshair'] == True:
    crosshair_path = Scripts.DataManager.dataJson['crosshair']
    cursor_image = pygame.image.load(crosshair_path).convert_alpha()  
    cursor_image = pygame.transform.scale(cursor_image, (32, 32))  
    hotspot = (cursor_image.get_width() // 2, cursor_image.get_height() // 2)
    pygame.mouse.set_cursor((hotspot[0], hotspot[1]), cursor_image)
if Scripts.DataManager.dataJson['customCrosshair'] == False:
        classicCrosshair = Scripts.AssetsManager.Crosshair.Crosshair1
        cursor_image = pygame.transform.scale(classicCrosshair, (32, 32))
        classicCrosshair = cursor_image
        hotspot = (cursor_image.get_width() // 2, cursor_image.get_height() // 2)
        pygame.mouse.set_cursor((hotspot[0], hotspot[1]), cursor_image) 


while not gameState['quit']:
    if gameState['gaming'] == "Gaming":
        time.sleep(0.3)
        round = Round(cameraSurface, screen, gameState)
        score = round.run()
        if score > Scripts.DataManager.dataJson['highScore']:
            Scripts.DataManager.dataJson['highScore'] = score
            Scripts.DataManager.saveData()

        if score < 0:
            if gameState['quit']:
                Scripts.DataManager.saveData()
                pygame.quit()
                sys.exit()
            else:
                continue
        endGameMenu = EndGameMenu(cameraSurface, (Scripts.Settings.WINDOW_SIZE - 600) // 2, 50,(600,600), gameState, True, score)
        while endGameMenu.enabled: 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Scripts.DataManager.saveData()
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
sys.exit()