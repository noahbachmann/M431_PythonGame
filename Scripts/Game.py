import pygame
import sys
import time
from Settings import *
from Round import *

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("My Space Shooter")
gameState = {'gaming': True, 'quit': False}
while not gameState['quit']:
    if gameState['gaming']:
        round = Round()
        score = round.run()
        if score < 0:
            gameState['quit'] = True
            continue
        endGameMenu = EndGameMenu(200, 50, gameState, score)
        while endGameMenu.ending: 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameState['quit'] = True
                    continue       
            endGameMenu.draw()
            pygame.display.update()

pygame.quit()