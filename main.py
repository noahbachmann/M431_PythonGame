import pygame
import sys
import time
import Scripts.Settings
from Scripts.Round import *
from Scripts.GameMenus import *
import Scripts.DataManager
import Scripts.AssetsManager
import asyncio

pygame.init()
    
async def main():
	await asyncio.sleep(0)
	screen = pygame.display.set_mode((1024,1024))
	screenSize = screen.get_size()
	if screenSize[1] < Scripts.Settings.WINDOW_SIZE:
		Scripts.Settings.WINDOW_SIZE = screenSize[1]
	cameraSurface = pygame.Surface((Scripts.Settings.WINDOW_SIZE, Scripts.Settings.WINDOW_SIZE))
	offset = (screenSize[0] // 2 - Scripts.Settings.WINDOW_SIZE // 2, screenSize[1] // 2 - Scripts.Settings.WINDOW_SIZE // 2)
	pygame.display.set_caption("My Space Shooter")
	gameState = False
	def drawFunction():
		screen.blit(cameraSurface, cameraSurface.get_frect(center = (screenSize[0]//2, screenSize[1]//2)))
		pygame.display.update()

	def endGame():
		pygame.quit()
		sys.exit()

	cursor_image = pygame.transform.scale(Scripts.AssetsManager.Crosshair.Crosshair1, (32, 32))
	pygame.mouse.set_cursor((cursor_image.get_width() // 2, cursor_image.get_height() // 2), cursor_image)
	gameState = 'menu'

	while True:
		if gameState == 'menu':
			MainMenuGame = MainMenu(cameraSurface, (Scripts.Settings.WINDOW_SIZE - 500) // 2, (Scripts.Settings.WINDOW_SIZE - 300) // 2,(500,300), True, gameState)
			while MainMenuGame.enabled:
					await asyncio.sleep(0)
					events = pygame.event.get()
					for event in events:
						if event.type == pygame.QUIT:
							endGame()
					MainMenuGame.handle_events(events)
					screen.fill((0,0,0))
					cameraSurface.fill((7, 0, 25))
					MainMenuGame.draw()
					drawFunction()

		gameState = 'game'
		round = Round(cameraSurface, screen, gameState)
		score = await round.run()
		if score > 1000:
			await Scripts.DataManager.submitScore(score)
		endGameMenu = EndGameMenu(cameraSurface, (Scripts.Settings.WINDOW_SIZE - 400) // 2, (Scripts.Settings.WINDOW_SIZE - 400) // 2,(400,400), gameState, True, score)
		while endGameMenu.enabled:
				await asyncio.sleep(0)
				events = pygame.event.get()
				for event in events:
					if event.type == pygame.QUIT:
						endGame()
				endGameMenu.handle_events(events)
				screen.fill((0,0,0))
				endGameMenu.draw()
				drawFunction()

	endGame()

asyncio.run(main())