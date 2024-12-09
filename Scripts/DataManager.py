import json
import os
import AssetsManager

dataPath = 'data/data.txt'


dataJson = {
    'crosshair': "Placeholder",
    'highScore': 0
}

def saveData():
    if not os.path.exists('data'):
        os.makedirs('data')

   
    with open(dataPath, 'w') as data_file:
        json.dump(dataJson, data_file, indent=4)  
    print(f"Data saved: {dataJson}")

def loadData():
    global dataJson  
    try:
        with open(dataPath, 'r') as data_file:
            dataJson = json.load(data_file)  #
            print("Data loaded: ", dataJson)
    except FileNotFoundError:
        print("No data file created yet, using defaults.")
    except json.JSONDecodeError:
        print("Error decoding JSON data. Using defaults.")

loadData()
saveData()  
