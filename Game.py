import pygame
import sys
import Scripts.Settings
from Scripts.Round import *
from Scripts.GameMenus import *
import sys 
import time
import Scripts.DataManager
import Scripts.AssetsManager

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
background = BACKGROUND_IMAGE

def drawFunction():
    screen.blit(background, background.get_frect(center = (screen.get_frect().center)))
    screen.blit(cameraSurface, cameraSurface.get_frect(center = (screenSize[0]//2, screenSize[1]//2)))
    pygame.display.update()

def endGame():
    Scripts.DataManager.saveData()
    pygame.quit()
    sys.exit()

cursor_image = None
if Scripts.DataManager.dataJson['customCrosshair'] == True:
    crosshair_path = Scripts.DataManager.dataJson['crosshair']
    cursor_image = pygame.transform.scale(pygame.image.load(crosshair_path).convert_alpha(), (32, 32))  
else:
    cursor_image = pygame.transform.scale(Scripts.AssetsManager.Crosshair.Crosshair1, (32, 32))
pygame.mouse.set_cursor((cursor_image.get_width() // 2, cursor_image.get_height() // 2), cursor_image)

while not gameState['quit']:
    if gameState['gaming'] == "Gaming":
        time.sleep(0.3)
        round = Round(cameraSurface, screen, gameState)
        score = round.run()
        
        Scripts.DataManager.saveData(score)

        if score < 0:
            if gameState['quit']:
                endGame()
            else:
                continue
        endGameMenu = EndGameMenu(cameraSurface, (Scripts.Settings.WINDOW_SIZE - 600) // 2, (Scripts.Settings.WINDOW_SIZE - 600) // 2,(600,600), gameState, True, score)
        while endGameMenu.enabled: 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    endGame()   
            screen.fill((0,0,0))
            endGameMenu.draw()
            drawFunction()

    elif gameState['gaming'] == "MainMenu":
        MainMenuGame = MainMenu(cameraSurface, (Scripts.Settings.WINDOW_SIZE - 650) // 2, (Scripts.Settings.WINDOW_SIZE - 600) // 2,(650,650), True, gameState)
        while MainMenuGame.enabled:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    endGame()
            screen.fill((0,0,0))
            cameraSurface.fill((7, 0, 25))
            MainMenuGame.draw()
            drawFunction()

    elif gameState['gaming'] == "Stats":
        statsMenu = StatsMenu(cameraSurface, (Scripts.Settings.WINDOW_SIZE - 650) // 2, (Scripts.Settings.WINDOW_SIZE - 600) // 2,(650,650), True, gameState)
        while statsMenu.enabled:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    endGame()
            screen.fill((0,0,0))
            cameraSurface.fill((7, 0, 25))
            statsMenu.draw()
            drawFunction()
            
    elif gameState['gaming'] == "Settings":
        SettingsMenuGame = SettingsMenu(cameraSurface, (Scripts.Settings.WINDOW_SIZE - 650) // 2,  (Scripts.Settings.WINDOW_SIZE - 600) // 2,(650,650), True, gameState)
        while SettingsMenuGame.enabled:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:   
                    gameState['quit'] = True
                    endGame()
            screen.fill((0,0,0))
            cameraSurface.fill((7, 0, 25))
            SettingsMenuGame.draw()
            drawFunction()

endGame()