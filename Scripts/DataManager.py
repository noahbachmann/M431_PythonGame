import json
from AssetsManager import *
dataPath = 'data/data.txt'

dataJson = {
    'crosshair': Crosshair.Crosshair1
}



def saveData():
    with open('data/data.txt', 'w') as data_file:
        json.dump(dataJson, data_file)
    print(dataJson)


def loadData():
     with open('data/data.txt') as data_file:
         data =json.load(data_file)
         print(dataJson)




try: 
    with open('data/data.txt') as data_file:
        data =json.load(data_file)
        print(dataJson)

except:
    print("no data file created yet:/")