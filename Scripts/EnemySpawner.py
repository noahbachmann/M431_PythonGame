import pygame
from Enemy import *
from Timer import Timer
from AssetsManager import ENEMY_IMAGE
from random import choice

class Spawner:
    def __init__(self, difficulty:str, player, groups):
        self.player = player
        self.enemyGroups = groups
        self.spawnPoints = [(0,0), (0,100), (0,300), (0,400), (0, 500)]
        self.spawnRate = 5
        self.difficulty = difficulty
        self.SetDifficulty()
        self.spawnTimer = Timer(self.spawnRate, True, True, self.SpawnEnemy)

    def update(self):
        self.spawnTimer.update()
        
    def SpawnEnemy(self):
        #Enemy(choice(self.spawnPoints), 3, 1, 80, self.player, ENEMY_IMAGE, self.enemyGroups, (64, 64))
        BasicShooter(choice(self.spawnPoints), 2, 1, 1, 150, self.player, ENEMY_IMAGE, self.enemyGroups, 300, (64,64))

    def SetDifficulty(self):
        if self.difficulty == "normal":
            self.spawnRate = 3