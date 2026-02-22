import pygame
from Scripts.Enemy import *
from Scripts.Timer import Timer
from Scripts.AssetsManager import Enemy_Explosion, Dark_Force, Arachnis, Brawler, Apex, Crypto, Moculus, Jinx, Audio
from random import *

class Spawner:
    def __init__(self, difficulty:str, player, groups):
        self.player = player
        self.enemyGroups = groups
        self.spawnPoints = []
        self.enemies = {
            "Brawler": {"class": BasicMelee, "weight": 40, "args": [2, 1, 3, 230, self.player,
            Brawler.BRAWLER_IDLE_1,{"idle":{"frames":[Brawler.BRAWLER_IDLE_1, Brawler.BRAWLER_IDLE_2, Brawler.BRAWLER_IDLE_3], "speed":8},
                                    "attack":{"frames":[Brawler.BRAWLER_BOOSTATTACK_1, Brawler.BRAWLER_BOOSTATTACK_2], "speed":8},
                                "death":{"frames":Enemy_Explosion.animationArray, "speed":10}}, self.enemyGroups,45,(64, 64)]},

            "Arachnis": {"class": BasicShooter, "weight": 30, "args": [2, 1, 4, 150, 2.8, self.player,
            Arachnis.ARACHNIS_1,{"idle":{"frames":[Arachnis.ARACHNIS_1,Arachnis.ARACHNIS_2], "speed":8},
                                "death":{"frames":Enemy_Explosion.animationArray, "speed":10}},self.enemyGroups, 420,0,(64, 64)]}, 

            "DarkForce": {"class": DoubleShooter, "weight": 10, "args": [2, 1, 4, 160, 3.5, self.player,
            Dark_Force.DARK_FORCE_1,{"idle":{"frames":[Dark_Force.DARK_FORCE_1,Dark_Force.DARK_FORCE_2], "speed":8},
                                "death":{"frames":Enemy_Explosion.animationArray, "speed":10}},self.enemyGroups, False, 430,0,(64, 64)]},

            "Apex": {"class": DoubleShooter, "weight": 0, "args": [4, 2, 5, 180, 2.2, self.player,
            Apex.APEX_IDLE_1,{"idle":{"frames":[Apex.APEX_IDLE_1,Apex.APEX_IDLE_2], "speed":8},
                                "death":{"frames":Enemy_Explosion.animationArray, "speed":10}},self.enemyGroups, True, 420,0,(64, 64)]},

            "Jinx": {"class": BasicShooter, "weight": 5, "args": [3, 1, 5, 160, 3.2, self.player,
            Jinx.JINX_1,{"idle":{"frames":Jinx.animationArray, "speed":8},
                                "death":{"frames":Enemy_Explosion.animationArray, "speed":10}},self.enemyGroups, 450,0,(64, 64)]}, 

            "Moculus": {"class": BasicShooter, "weight": 0, "args": [5, 2, 7, 160, 1.8, self.player,
            Moculus.MOCULUS_1,{"idle":{"frames":Moculus.animationArray, "speed":8},
                                "death":{"frames":Enemy_Explosion.animationArray, "speed":10}},self.enemyGroups, 500,0,(64, 64)]}, 
        } 

        self.miniBosses = {
            "Crypto": {
                "class": MiniBoss, "args": [20, 1, 100, 130, 3, self.player, Crypto.CRYPTO_1,{"idle":{"frames":[Crypto.CRYPTO_1,Crypto.CRYPTO_2,Crypto.CRYPTO_3,Crypto.CRYPTO_4,Crypto.CRYPTO_5], "speed":11},
                                "death":{"frames":Enemy_Explosion.animationArray, "speed":10}},self.enemyGroups, False, 250, 35,(128, 128)]},
            }

        self.spawnPoints.extend([(x, -200) for x in range(-200, 1200, 100)])
        self.spawnPoints.extend([(x, 1200) for x in range(-200, 1200, 100)])
        self.spawnPoints.extend([(-200, y) for y in range(-200, 1200, 100)])
        self.spawnPoints.extend([(1200, y) for y in range(-200, 1200, 100)])

        self.spawnRate = 4.0
        self.difficulty = difficulty
        self.spawnTimer = Timer(self.spawnRate, True, True, self.spawnEnemy)
        self.spawnMinibossTimer = Timer(100,True, True, self.spawnMiniboss)
        self.enemyUpgradeTimer = Timer(30, True, True, self.upgradeEnemy)
        self.upgraded = 0
        self.spawns = 2

    def update(self):
        self.spawnTimer.update()
        self.spawnMinibossTimer.update()
        self.enemyUpgradeTimer.update()

    def pause(self):
        self.spawnTimer.pause()
        self.spawnMinibossTimer.pause()
        self.enemyUpgradeTimer.pause()

    def resume(self):
        self.spawnTimer.resume()
        self.spawnMinibossTimer.resume()
        self.enemyUpgradeTimer.resume()
        
    def spawnEnemy(self):
        for x in range(self.spawns):
            rollNum = randint(1,100)
            currentWeight = 0
            for key, enemy in self.enemies.items():
                currentWeight += enemy["weight"]
                if rollNum <= currentWeight:
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
        self.upgraded += 1

        if self.upgraded % 2 == 0:
            if self.spawnRate > 0.8:
                self.spawnRate -= 0.3
                self.spawnTimer.duration = self.spawnRate

        if self.upgraded % 4 == 0:
            self.spawns += 1

        for key, enemy in self.enemies.items():
            if self.upgraded % 3 == 0:
                enemy["args"][0] += 1
            if self.upgraded % 6 == 0:
                enemy["args"][1] += 1

        if self.upgraded % 10 == 0:
            for key, enemy in self.miniBosses.items():
                enemy["args"][0] += 10

        if self.upgraded == 4:
            self.enemies["Moculus"]["weight"] = 6
            self.enemies["Apex"]["weight"] = 5

        if self.upgraded >= 4:
            self.enemies["Brawler"]["weight"] = 30
            self.enemies["Arachnis"]["weight"] = 25
            self.enemies["DarkForce"]["weight"] = 15
            self.enemies["Jinx"]["weight"] = 10

        if self.upgraded >= 9:
            self.enemies["Brawler"]["weight"] = 20
            self.enemies["Arachnis"]["weight"] = 20
            self.enemies["DarkForce"]["weight"] = 20
            self.enemies["Jinx"]["weight"] = 15
            self.enemies["Moculus"]["weight"] = 15
            self.enemies["Apex"]["weight"] = 10

    def SetDifficulty(self):
        if self.difficulty == "normal":
            self.spawnRate = 4.0