import json
import os
import pygame

localAppData = os.getenv('LOCALAPPDATA')
desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
game_folder = os.path.join(desktop_path, 'M431_SpaceGame')
img_folder = os.path.join(game_folder, 'imgs')
dataPath = os.path.join(game_folder, 'data.json')

dataJson = {
    'crosshair': "Placeholder",
    'customCrosshair': False,
    "top5Highscores": [0, 0, 0, 0, 0],
    'Hotkey_Up': pygame.K_w,
    'Hotkey_Down': pygame.K_s,
    'Hotkey_Left': pygame.K_a,
    'Hotkey_Right': pygame.K_d,
    'Hotkey_Boost': pygame.K_LSHIFT,
    'Hotkey_close': pygame.K_j
}

def saveData():
    if not os.path.exists(game_folder):
        os.makedirs(game_folder)
    
    if not os.path.exists(img_folder):
        os.makedirs(img_folder)

    with open(dataPath, 'w') as data_file:
        json.dump(dataJson, data_file, indent=4)  

def loadData():
    global dataJson  
    try:
        with open(dataPath, 'r') as data_file:
            dataJson = json.load(data_file)  
    except FileNotFoundError:
        print(f"No data file found at {dataPath}, using defaults.")
    except json.JSONDecodeError:
        print("Error decoding JSON data. Using defaults.")


def resetHotkeys():
    dataJson['Hotkey_Up'] = pygame.K_w
    dataJson['Hotkey_Down'] = pygame.K_s
    dataJson['Hotkey_Left'] = pygame.K_a
    dataJson['Hotkey_Right'] = pygame.K_d
    dataJson['Hotkey_Boost'] = pygame.K_LSHIFT
    dataJson['Hotkey_close'] = pygame.K_j
    saveData()



loadData()
saveData()
