import pygame
from Scripts.Enemy import *
from Scripts.Timer import Timer
from Scripts.AssetsManager import Enemy_Explosion, Dark_Force, Arachnis, Brawler, Apex, Crypto,Moculus, Jinx, Audio
from random import *

class Spawner:
    def __init__(self, difficulty:str, player, groups):
        self.player = player
        self.enemyGroups = groups
        self.spawnPoints = []
        self.enemies = {
            #health, damage, gold, speed, player, image, groups, size:tuple = None
            "Brawler": {"class": BasicMelee, "weight": 35, "args": [2, 1, 3, 220, self.player,
            Brawler.BRAWLER_IDLE_1,{"idle":{"frames":[Brawler.BRAWLER_IDLE_1, Brawler.BRAWLER_IDLE_2, Brawler.BRAWLER_IDLE_3], "speed":8},
                                    "attack":{"frames":[Brawler.BRAWLER_BOOSTATTACK_1, Brawler.BRAWLER_BOOSTATTACK_2], "speed":8},
                                "death":{"frames":Enemy_Explosion.animationArray, "speed":10}}, self.enemyGroups,45,(64, 64)]},
            #health, damage, gold, speed, atkSpeed, player, image, groups, range=None, size:tuple = None
            "Arachnis": {"class": BasicShooter, "weight": 35, "args": [2, 1, 1, 150, 3.5, self.player,
            Arachnis.ARACHNIS_1,{"idle":{"frames":[Arachnis.ARACHNIS_1,Arachnis.ARACHNIS_2], "speed":8},
                                "death":{"frames":Enemy_Explosion.animationArray, "speed":10}},self.enemyGroups, 400,0,(64, 64)]}, 
            #health, damage, gold, speed, atkSpeed, player, image, groups, swap, range=None, size:tuple = None
            "DarkForce": {"class": DoubleShooter, "weight": 15, "args": [2, 1, 2, 150, 4, self.player,
            Dark_Force.DARK_FORCE_1,{"idle":{"frames":[Dark_Force.DARK_FORCE_1,Dark_Force.DARK_FORCE_2], "speed":8},
                                "death":{"frames":Enemy_Explosion.animationArray, "speed":10}},self.enemyGroups, False, 430,0,(64, 64)]},
              #health, damage, gold, speed, atkSpeed, player, image, groups, swap, range=None, size:tuple = None
            "Apex": {"class": DoubleShooter, "weight": 0, "args": [2, 1, 2, 150, 2, self.player,
            Apex.APEX_IDLE_1,{"idle":{"frames":[Apex.APEX_IDLE_1,Apex.APEX_IDLE_2], "speed":8},
                                "death":{"frames":Enemy_Explosion.animationArray, "speed":10}},self.enemyGroups, True, 420,0,(64, 64)]},
                                #health, damage, gold, speed, atkSpeed, player, image, groups, range=None, size:tuple = None
            "Jinx": {"class": BasicShooter, "weight": 5, "args": [2, 1, 2, 150, 3, self.player,
            Jinx.JINX_1,{"idle":{"frames":Jinx.animationArray, "speed":8},
                                "death":{"frames":Enemy_Explosion.animationArray, "speed":10}},self.enemyGroups, 450,0,(64, 64)]}, 
            #health, damage, gold, speed, atkSpeed, player, image, groups, range=None, size:tuple = None
            "Moculus": {"class": BasicShooter, "weight": 10, "args": [2, 1, 2, 180, 1.5, self.player,
            Moculus.MOCULUS_1,{"idle":{"frames":Moculus.animationArray, "speed":8},
                                "death":{"frames":Enemy_Explosion.animationArray, "speed":10}},self.enemyGroups, 380,0,(64, 64)]}, 
           
            } 
        self.miniBosses = {
            "Crypto": {
                "class": MiniBoss, "args": [15, 1, 75, 120, 3, self.player, Crypto.CRYPTO_1,{"idle":{"frames":[Crypto.CRYPTO_1,Crypto.CRYPTO_2,Crypto.CRYPTO_3,Crypto.CRYPTO_4,Crypto.CRYPTO_5], "speed":11},
                                "death":{"frames":Enemy_Explosion.animationArray, "speed":10}},self.enemyGroups, False, 200, 35,(128, 128)]},
            }
        self.spawnPoints.extend([(x, -200) for x in range(-200, 1200, 100)])
        self.spawnPoints.extend([(x, 1200) for x in range(-200, 1200, 100)])
        self.spawnPoints.extend([(-200, y) for y in range(-200, 1200, 100)])
        self.spawnPoints.extend([(1200, y) for y in range(-200, 1200, 100)])
        self.spawnRate = 5
        self.difficulty = difficulty
        self.SetDifficulty()
        self.spawnTimer = Timer(self.spawnRate, True, True, self.spawnEnemy)
        self.spawnMinibossTimer = Timer(60*2,True, True, self.spawnMiniboss)
        self.enemyUpgradeTimer = Timer(30, True, True, self.upgradeEnemy)
        self.upgraded = 0
        self.spawns = 2

    def update(self):
        self.spawnTimer.update()
        self.spawnMinibossTimer.update()
        self.enemyUpgradeTimer.update()
        
    def spawnEnemy(self):
        for x in range(self.spawns):
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
    
    def spawnMiniboss(self):
        x = choice(list(self.miniBosses.values()))
        x["class"]((0, -200), *x["args"])
        Audio.MINIBOSS_SPAWN.play()

    def upgradeEnemy(self):
        for key, enemy in self.enemies.items():
            if (key == "Brawler" or key == "Arachnis") and enemy["weight"] > 16:
                enemy["weight"] -= 2
            elif (key == "DarkForce" or key == "Apex" or key == "Jinx" or key == "Moculus") and enemy["weight"] < 17:
                enemy["weight"] += 2 
            if self.upgraded != 0:
                if self.upgraded % 3 == 0:
                    enemy["args"][0] += 1
                    enemy["args"][1] += 1
                if self.upgraded % 4 == 0:
                    if self.spawnRate > 1:
                        self.spawnRate -= 0.5
                    elif self.spawnRate > 0.5:
                        self.spawnRate -= 0.1
                    else:
                        self.spawns += 1

        if self.upgraded % 10:
            for key, enemy in self.miniBosses.items():
                    enemy["args"][0] += 5
        self.upgraded += 1      

    def SetDifficulty(self):
        if self.difficulty == "normal":
            self.spawnRate = 4
