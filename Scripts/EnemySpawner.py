import pygame
from Enemy import *
from Timer import Timer
from AssetsManager import ENEMY_IMAGE
from random import *

class Spawner:
    def __init__(self, difficulty:str, player, groups):
        self.player = player
        self.enemyGroups = groups
        self.spawnPoints = []
        self.enemies = [
            #self, *groups, health, damage, gold, speed, player, image, size:tuple = None
            {"class": BasicShooter, "weight": 50, "args": (2, 1, 1,5, 150, self.player,
            ENEMY_IMAGE,self.enemyGroups, 200, (64, 64))}, 
            {"class": BasicMelee, "weight": 50, "args": (2,1,3, 200, self.player,
            ENEMY_IMAGE, self.enemyGroups, (64, 64))},
            ]
        self.spawnPoints.extend([(x, 0) for x in range(0, 800, 100)])
        self.spawnPoints.extend([(x, 800) for x in range(0,800, 100)])
        self.spawnPoints.extend([(0, y) for y in range(0, 800, 100)])
        self.spawnPoints.extend([(800, y) for y in range(0, 800, 100)])
        self.spawnRate = 5
        self.difficulty = difficulty
        self.SetDifficulty()
        self.spawnTimer = Timer(self.spawnRate, True, True, self.SpawnEnemy)

    def update(self):
        self.spawnTimer.update()
        
    def SpawnEnemy(self):
        rollNum = randint(1,100)
        enemiesLength = len(self.enemies)
        currentWeight = 0
        for x in range(enemiesLength):
            currentWeight += self.enemies[x]["weight"] 
            if rollNum < currentWeight:
                self.enemies[x]["class"](
                    choice(self.spawnPoints),  
                    *self.enemies[x]["args"],                 
                )
                break

    def SetDifficulty(self):
        if self.difficulty == "normal":
            self.spawnRate = 2