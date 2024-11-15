import pygame
from Enemy import *
from Timer import Timer
from AssetsManager import ENEMY_IMAGE
from random import choice

class Spawner:
    def __init__(self, difficulty:str, groups):
        self.enemyGroups = groups
        self.spawnPoints = [(0,0), (0,100), (0,300), (0,400), (0, 500)]
        self.spawnRate = 5
        self.difficulty = difficulty
        self.SetDifficulty()
        self.spawnTimer = Timer(self.spawnRate, True, True, self.SpawnEnemy)

    def update(self):
        self.spawnTimer.update()
        
    def SpawnEnemy(self):
        Enemy(choice(self.spawnPoints), 3, 100, ENEMY_IMAGE, self.enemyGroups, (64, 64))

    def SetDifficulty(self):
        if self.difficulty == "normal":
            self.spawnRate = 3