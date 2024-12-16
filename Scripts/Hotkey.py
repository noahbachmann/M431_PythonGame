import pygame
import sys
import Scripts.DataManager

class Hotkeys:
    def closeGame():
        pygame.quit()
        sys.exit()



    def change_Hotkey_Up():
        print("Press a key to set the binding...")
        while True:  
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    Scripts.DataManager.dataJson['Hotkey_Up'] = event.key
                    Scripts.DataManager.saveData()
                    return  

    def change_Hotkey_Down():
        print("Press a key to set the binding...")
        while True:  
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    Scripts.DataManager.dataJson['Hotkey_Down'] = event.key
                    Scripts.DataManager.saveData()
                    return  
                
    def change_Hotkey_Left():
        print("Press a key to set the binding...")
        while True:  
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    Scripts.DataManager.dataJson['Hotkey_Left'] = event.key
                    Scripts.DataManager.saveData()
                    return  
                
    def change_Hotkey_Right():
        print("Press a key to set the binding...")
        while True:  
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    Scripts.DataManager.dataJson['Hotkey_Right'] = event.key
                    Scripts.DataManager.saveData()
                    return  
                
    def change_Hotkey_Boost():
        print("Press a key to set the binding...")
        while True:  
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    Scripts.DataManager.dataJson['Hotkey_Boost'] = event.key
                    Scripts.DataManager.saveData()
                    return  
                
                
    def change_Hotkey_close():
        print("Press a key to set the binding...")
        while True:  
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    Scripts.DataManager.dataJson['Hotkey_close'] = event.key
                    Scripts.DataManager.saveData()
                    return  
                



