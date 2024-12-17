import pygame
import sys
import Scripts.DataManager

class Hotkeys:
    def closeGame():
        pygame.quit()
        sys.exit()



    def change_Hotkey_Up():
        while True:  
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return  
                    Scripts.DataManager.dataJson['Hotkey_Up'] = event.key
                    Scripts.DataManager.saveData()
                    return  

    def change_Hotkey_Down():
        while True:  
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return
                    Scripts.DataManager.dataJson['Hotkey_Down'] = event.key
                    Scripts.DataManager.saveData()
                    return  

    def change_Hotkey_Left():
        while True:  
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return
                    Scripts.DataManager.dataJson['Hotkey_Left'] = event.key
                    Scripts.DataManager.saveData()
                    return  

    def change_Hotkey_Right():
        while True:  
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return
                    Scripts.DataManager.dataJson['Hotkey_Right'] = event.key
                    Scripts.DataManager.saveData()
                    return  

    def change_Hotkey_Boost():
        while True:  
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return
                    Scripts.DataManager.dataJson['Hotkey_Boost'] = event.key
                    Scripts.DataManager.saveData()
                    return  

    def change_Hotkey_close():
        while True:  
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return
                    Scripts.DataManager.dataJson['Hotkey_close'] = event.key
                    Scripts.DataManager.saveData()
                    return  

                



