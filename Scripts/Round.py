import pygame
import platform
import asyncio
from random import randint

from Scripts.Player import *
from Scripts.HUDController import *
from Scripts.EnemySpawner import *
from Scripts.AssetsManager import *
from Scripts.Groups import AllSprites


class Round:
    def __init__(self, surface, screen, gameState):
        self.screen = screen  
        self.cameraSurface = surface
        self.gameState = gameState
        screenSize = screen.get_size()
        self.offset = (screenSize[0] // 2 - Scripts.Settings.WINDOW_SIZE // 2, screenSize[1] // 2 - Scripts.Settings.WINDOW_SIZE // 2)
        self.clock = pygame.time.Clock()
        self.allSprites = AllSprites()
        self.hudSprites = pygame.sprite.Group()
        self.enemySprites = pygame.sprite.Group()
        self.playerShotSprites = pygame.sprite.Group()
        self.collisionSprites = pygame.sprite.Group()
        self.border = []
        self.stars = []
        self.player = Player((Scripts.Settings.WINDOW_SIZE // 2, Scripts.Settings.WINDOW_SIZE // 2), self.offset, 6, 200, 120, 2,
                            (self.allSprites,self.playerShotSprites), self.collisionSprites, (64, 64),
                            {"idle":{"frames": Sunset.animationArray_idle, "speed": 8}, "boosting":{"frames": Sunset.animationArray_boost, "speed": 8}})
        self.hudController = HUDController(self.cameraSurface, self.player, gameState, self.allSprites)
        self.enemySpawner = Spawner("normal", self.player, (self.allSprites, self.enemySprites))
        self.running = True
    
    async def run(self):
        self.createBackground()
        self.createBorder()
        _prevPause = False
        _win = platform.window
        while self.running:
            await asyncio.sleep(0)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    return 0
                if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            self.hudController.pause = not self.hudController.pause
                            continue

            if _win is not None and not _win.gameFocused and not self.hudController.pause:
                self.hudController.pause = True

            if self.hudController.pause != _prevPause:
                if self.hudController.pause:
                    self.enemySpawner.pause()
                    if self.player.boosting:
                        self.player.boosting = False
                        self.player.speed = self.player.normalSpeed
                        Audio.BOOST.stop()
                else:
                    self.enemySpawner.resume()
                _prevPause = self.hudController.pause

            dt = min(self.clock.tick(60) / 1000, 0.05)

            if self.hudController.pause:
                for sprite in self.enemySprites.sprites():
                    if hasattr(sprite, 'animationState') and sprite.animationState == "death":
                        sprite.update(dt)
                self.hudController.update(self.cameraSurface, dt)
                self.drawToScreen()
                if not self.running:
                    return 0
                continue
        
            else:
                self.cameraSurface.fill((7, 0, 25))
                self.collisions()
                if self.player.health <= 0:
                    self.running = False
                    Audio.GAME_END.play()
                    return self.player.score          
                self.enemySpawner.update()
                self.allSprites.update(self.cameraSurface, dt, self.player.moveOffset)
                self.player.update(self.cameraSurface, dt)
                self.hudController.update(self.cameraSurface,dt)
                self.drawToScreen()
        
    def collisions(self):
        for shot in self.playerShotSprites:
            if hasattr(shot, 'collided') and shot.collided:
                continue       
            enemies = pygame.sprite.spritecollide(shot, self.enemySprites, False)
            for enemy in enemies:
                if enemy not in shot.collidedEnemies and enemy.isEnemy and enemy.animationState != "death":
                    shot.hit(enemy)
                    enemy.hit(shot.damage)
        enemies = pygame.sprite.spritecollide(self.player, self.enemySprites, False)
        if enemies:
            if enemies.count == 1 and (hasattr(enemies[0], 'collided') and enemies[0].collided):
                pass
            else:
                self.player.hit(enemies[0].damage)
                for enemy in enemies:
                    if not enemy.isEnemy:
                        enemy.hit()

    def drawToScreen(self):
        screenSize = self.screen.get_size()
        self.screen.blit(self.cameraSurface, self.cameraSurface.get_frect(center = (screenSize[0]//2,screenSize[1]//2)))
        pygame.display.update()

    def createBackground(self):
        mapThird = MAP_SIZE // 3
        tileHalf = TILE_SIZE // 2
        startPos = -(mapThird) * 1.5 + tileHalf
        endBound = MAP_SIZE - (mapThird // 2)

        currentPointX = currentPointY = startPos
        randomNum = randint(1, 20)
        x = 1
        while currentPointY < endBound:
            while currentPointX < endBound:
                if x == randomNum:
                    star_img = pygame.transform.scale(STAR_IMAGE, (32, 32)).copy()
                    star_img.set_alpha(int(255 * 0.7))
                    self.stars.append(ImageSprite((currentPointX + randint(-16,16), currentPointY + randint(-16,16)), self.allSprites, star_img))
                    randomNum = randint(4,20)
                    x = 1
                else:
                    x += 1
                currentPointX += TILE_SIZE
            currentPointX = startPos
            currentPointY += TILE_SIZE
    
    def createBorder(self):
        mapThird = MAP_SIZE // 3
        tileHalf = TILE_SIZE // 2
        leftX = -(mapThird) - tileHalf
        rightX = MAP_SIZE - mapThird + tileHalf
        currentPoint = leftX

        while currentPoint < MAP_SIZE - mapThird + TILE_SIZE:
            self.border.append(BorderSprite((currentPoint, leftX), (self.allSprites, self.collisionSprites), BORDER_BLOCK, (64,64)))
            self.border.append(BorderSprite((currentPoint, rightX), (self.allSprites, self.collisionSprites), BORDER_BLOCK, (64,64)))
            if not (currentPoint == leftX or currentPoint == rightX):
                self.border.append(BorderSprite((leftX, currentPoint), (self.allSprites, self.collisionSprites), BORDER_BLOCK, (64,64)))
                self.border.append(BorderSprite((rightX, currentPoint), (self.allSprites, self.collisionSprites), BORDER_BLOCK, (64,64)))
            currentPoint += TILE_SIZE

class ImageSprite(pygame.sprite.Sprite):
    def __init__(self, pos:tuple, groups, image, size:tuple=None):
        super().__init__(groups)
        if size:
            self.image = pygame.transform.scale(image, size)
        else:
            self.image = image
        self.rect = self.image.get_frect(center=pos)
        self.offset = pygame.math.Vector2(0,0)
    
    def draw(self, surface):
	    surface.blit(self.image, self.rect)

class BorderSprite(ImageSprite):
    def __init__(self, pos, groups, image, size = None):
        super().__init__(pos, groups, image, size)