import pygame
from Enemy import *
from Timer import Timer
from AssetsManager import Apex, Arachnis, Brawler, Enemy_Explosion
from random import *

class Spawner:
    def __init__(self, difficulty:str, player, groups):
        self.player = player
        self.enemyGroups = groups
        self.spawnPoints = []
        self.enemies = [
            #self, pos:tuple, health, damage, gold, speed, atkSpeed, player, image, groups, range=None, size:tuple = None
            {"class": BasicShooter, "weight": 50, "args": (2, 1, 1, 150, 5, self.player,
            Arachnis.ARACHNIS_1,{"idle":{"frames":[Arachnis.ARACHNIS_1,Arachnis.ARACHNIS_2], "speed":8},
                                "death":{"frames":Enemy_Explosion.animationArray, "speed":5}},self.enemyGroups, 400, (64, 64))}, 
            #self, pos:tuple, health, damage, gold, speed, player, image, groups, size:tuple = None
            {"class": BasicMelee, "weight": 50, "args": (2, 1, 3, 200, self.player,
            Brawler.BRAWLER_IDLE_1,{"idle":{"frames":[Brawler.BRAWLER_IDLE_1, Brawler.BRAWLER_IDLE_2, Brawler.BRAWLER_IDLE_3], "speed":8},
                                "death":{"frames":Enemy_Explosion.animationArray, "speed":5}}, self.enemyGroups, (64, 64))},
            ]
        self.spawnPoints.extend([(x, -200) for x in range(-200, 1200, 100)])
        self.spawnPoints.extend([(x, 1200) for x in range(-200, 1200, 100)])
        self.spawnPoints.extend([(-200, y) for y in range(-200, 1200, 100)])
        self.spawnPoints.extend([(1200, y) for y in range(-200, 1200, 100)])
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