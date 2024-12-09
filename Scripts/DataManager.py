import json
import os

localAppData = os.getenv('LOCALAPPDATA')
desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
game_folder = os.path.join(desktop_path, 'M431_SpaceGame')
img_folder = os.path.join(game_folder, 'imgs')
dataPath = os.path.join(game_folder, 'data.json')

dataJson = {
    'crosshair': "Placeholder",
    'customCrosshair': False,
    'highScore': 0
}

def saveData():
    if not os.path.exists(game_folder):
        os.makedirs(game_folder)
        print(f"Folder created at: {game_folder}")
    
    if not os.path.exists(img_folder):
        os.makedirs(img_folder)
        print(f"Image folder created at: {img_folder}")

    with open(dataPath, 'w') as data_file:
        json.dump(dataJson, data_file, indent=4)  
    print(f"Data saved to: {dataPath}")
    print(f"Data: {dataJson}")

def loadData():
    global dataJson  
    try:
        with open(dataPath, 'r') as data_file:
            dataJson = json.load(data_file)  
            print(f"Data loaded from: {dataPath}")
            print(f"Data: {dataJson}")
    except FileNotFoundError:
        print(f"No data file found at {dataPath}, using defaults.")
    except json.JSONDecodeError:
        print("Error decoding JSON data. Using defaults.")

loadData()
saveData()
