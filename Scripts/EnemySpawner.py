import pygame
from Enemy import *
from Timer import Timer
from AssetsManager import Enemy_Explosion, Dark_Force, Arachnis, Brawler, Apex
from random import *

class Spawner:
    def __init__(self, difficulty:str, player, groups):
        self.player = player
        self.enemyGroups = groups
        self.spawnPoints = []
        self.enemies = {
            #health, damage, gold, speed, player, image, groups, size:tuple = None
            "Brawler": {"class": BasicMelee, "weight": 50, "args": (2, 1, 3, 200, self.player,
            Brawler.BRAWLER_IDLE_1,{"idle":{"frames":[Brawler.BRAWLER_IDLE_1, Brawler.BRAWLER_IDLE_2, Brawler.BRAWLER_IDLE_3], "speed":8},
                                "death":{"frames":Enemy_Explosion.animationArray, "speed":5}}, self.enemyGroups, (64, 64))},
            #health, damage, gold, speed, atkSpeed, player, image, groups, range=None, size:tuple = None
            "Arachnis": {"class": BasicShooter, "weight": 50, "args": (2, 1, 1, 150, 3.5, self.player,
            Arachnis.ARACHNIS_1,{"idle":{"frames":[Arachnis.ARACHNIS_1,Arachnis.ARACHNIS_2], "speed":8},
                                "death":{"frames":Enemy_Explosion.animationArray, "speed":5}},self.enemyGroups, 400, (64, 64))}, 
            #health, damage, gold, speed, atkSpeed, player, image, groups, swap, range=None, size:tuple = None
            "DarkForce": {"class": DoubleShooter, "weight": 0, "args": (2, 1, 2, 150, 4, self.player,
            Dark_Force.DARK_FORCE_1,{"idle":{"frames":[Dark_Force.DARK_FORCE_1,Dark_Force.DARK_FORCE_2], "speed":8},
                                "death":{"frames":Enemy_Explosion.animationArray, "speed":5}},self.enemyGroups, False, 400, (64, 64))},
              #health, damage, gold, speed, atkSpeed, player, image, groups, swap, range=None, size:tuple = None
            "Apex": {"class": DoubleShooter, "weight": 0, "args": (2, 1, 2, 150, 2, self.player,
            Apex.APEX_IDLE_1,{"idle":{"frames":[Apex.APEX_IDLE_1,Apex.APEX_IDLE_2], "speed":8},
                                "death":{"frames":Enemy_Explosion.animationArray, "speed":5}},self.enemyGroups, True, 400, (64, 64))},
            }     
        self.spawnPoints.extend([(x, -200) for x in range(-200, 1200, 100)])
        self.spawnPoints.extend([(x, 1200) for x in range(-200, 1200, 100)])
        self.spawnPoints.extend([(-200, y) for y in range(-200, 1200, 100)])
        self.spawnPoints.extend([(1200, y) for y in range(-200, 1200, 100)])
        self.spawnRate = 5
        self.difficulty = difficulty
        self.SetDifficulty()
        self.spawnTimer = Timer(self.spawnRate, True, True, self.spawnEnemy)
        self.enemyUpgradeTimer = Timer(30, True, True, self.upgradeEnemy)

    def update(self):
        self.spawnTimer.update()
        self.enemyUpgradeTimer.update()
        
    def spawnEnemy(self):
        rollNum = randint(1,100)
        currentWeight = 0
        for key, enemy in self.enemies.items():
            currentWeight += enemy["weight"]
            if rollNum < currentWeight:
                enemy["class"](
                    choice(self.spawnPoints),  
                    *enemy["args"]
                )
                break

    def upgradeEnemy(self):
        for key, enemy in self.enemies.items():
            if (key == "Brawler" or key == "Arachnis") and enemy["weight"] > 20:
                enemy["weight"] -= 2
            elif (key == "DarkForce" or key == "Apex") and enemy["weight"] < 20:
                enemy["weight"] += 2     

    def SetDifficulty(self):
        if self.difficulty == "normal":
            self.spawnRate = 3