import pygame
import math
from Scripts.Timer import *
from Scripts.AssetsManager import *
from Scripts.Shot import *
from Scripts.Settings import *
import Scripts.DataManager

class Player(pygame.sprite.Sprite):
    def __init__(self, pos:tuple, camOffset:tuple, health, speed, boostStrength, boostAmount:float, attackGroups, collisionSprites, size:tuple = None, animationFrames = None):
        super().__init__()
        self.camOffset = camOffset
        self.moveOffset = pygame.math.Vector2(0,0)
        self.direction = pygame.math.Vector2(0,0)
        self.normalSpeed = speed
        self.speed = speed
        self.maxHealth = health
        self.health = health
        self.boostTank = boostAmount
        self.boostAmount = boostAmount
        self.boostStrength = boostStrength
        self.boosting = False
        self.attackGroups = attackGroups
        self.collisionSprites = collisionSprites
        self.damageTimer = Timer(0.5)
        self.damagingTimer = Timer(0.1, True, False, self.damaging)
        self.damageCount = 0
        self.atkSpeed = 0.5
        self.atkDamage = 1
        self.atkTimer = Timer(self.atkSpeed)
        self.heavyCd = 8
        self.heavyCdTimer = Timer(self.heavyCd)
        self.gold = 0
        self.score = 0
        self.frames = animationFrames
        self.frameIndex = 0
        self.animationState = "idle"
        self.hitHighscore = False
        self.heavyState = "charged"
        if size:
            self.image = pygame.transform.scale(Sunset.SUNSET_IDLE_1, size)
            self.size = size
        else:
            self.image = Sunset.SUNSET_IDLE_1
        self.savedImage = self.image
        self.rect = self.image.get_frect(center=pos)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self, surface, dt): 
        self.animate(dt)
        self.damagingTimer.update()
        mousePos = pygame.mouse.get_pos()
        mousePos = (mousePos[0] - self.camOffset[0], mousePos[1] - self.camOffset[1])
        mouse = pygame.mouse.get_pressed()
        keys = pygame.key.get_pressed()
        boostKeys = pygame.key.get_just_pressed()
        if boostKeys[Scripts.DataManager.dataJson['Hotkey_Boost']]:
            if not self.boosting and self.boostAmount > 0:
                self.boosting = True
                Audio.BOOST.play(-1)
        elif self.boosting and not keys[Scripts.DataManager.dataJson['Hotkey_Boost']]:
            self.boosting = False
            self.speed = self.normalSpeed
            Audio.BOOST.stop()
        if self.boosting:
            self.boostAmount -= dt
            if self.speed == self.normalSpeed and self.boostAmount > 0:
                self.speed += self.boostStrength
        elif self.boostAmount < self.boostTank:
            if self.boostAmount + dt > self.boostTank:
                self.boostAmount = self.boostTank
            else:
                self.boostAmount += dt
        if self.boostAmount <= 0:
            self.boosting = False
            self.speed = self.normalSpeed
            Audio.BOOST.stop()
        if self.boosting:
            if self.animationState != "boosting":
                self.animationState = "boosting"
        elif self.animationState == "boosting":
            self.animationState = "idle"
        self.direction.x = int(keys[Scripts.DataManager.dataJson['Hotkey_Right']]) - int(keys[Scripts.DataManager.dataJson['Hotkey_Left']])
        self.direction.y = int(keys[Scripts.DataManager.dataJson['Hotkey_Down']]) - int(keys[Scripts.DataManager.dataJson['Hotkey_Up']])
        angle = math.degrees(math.atan2(mousePos[1] - self.rect.centery, mousePos[0] - self.rect.centerx))
        self.image = pygame.transform.rotate(self.savedImage, -angle-90)
        if self.direction.length() > 0:
            self.direction = self.direction.normalize()
        check:pygame.math.Vector2 = self.moveOffset + (self.direction * self.speed * dt)
        halfSize = MAP_SIZE // 2 - TILE_SIZE // 2
        if -halfSize <= check.x <= halfSize:
            self.moveOffset.x = check.x
        if -halfSize <= check.y <= halfSize:
            self.moveOffset.y = check.y
        self.rect = self.image.get_frect(center=self.rect.center)
        if (mouse[0] or keys[Scripts.DataManager.dataJson['Hotkey_Attack']]) and not self.atkTimer.active:
            self.shoot(angle)  
            self.atkTimer.activate()
        if not self.heavyCdTimer.active:
            if self.heavyState != "charged":
                self.heavyState = "charged"
            if (mouse[2] or keys[pygame.K_f]):
                self.heavy(angle)
                self.heavyCdTimer.activate() 
        if self.score > Scripts.DataManager.dataJson["top5Highscores"][0] > 1000 and not self.hitHighscore:
            Audio.UNREAL.play()      
            self.hitHighscore = True
        self.atkTimer.update()
        self.heavyCdTimer.update()
        self.damageTimer.update()
        self.draw(surface)
        
    def shoot(self, angle):
        offset = pygame.math.Vector2(math.cos(math.radians(angle)), math.sin(math.radians(angle))) * self.rect.height / 2
        spawnPos = self.rect.center + offset
        Shot(spawnPos,self.atkDamage,500,1,angle,Player_Laser.PLAYER_LASER_1, self.attackGroups, playerOffset=self.moveOffset.copy(), size=(7,14),hitAnimation=Player_Laser.animationArray_laser_explosion)
        Audio.LASER_HIGH.play()

    def heavy(self, angle):
        offset = pygame.math.Vector2(math.cos(math.radians(angle)), math.sin(math.radians(angle))) * self.rect.height / 2
        spawnPos = self.rect.center + offset
        Heavy(spawnPos,2,200,angle,128,Heavy_Attack.HEAVY_ATTACK_LASER, Heavy_Attack.HEAVY_ATTACK_3, self.attackGroups, self.moveOffset.copy(), (8,8))
        self.heavyState = "recharging"

    def hit(self, damage):
        if self.damageTimer.active:
            return
        self.damageTimer.activate()
        self.damagingTimer.activate()
        self.health -= damage
        Audio.PLAYER_DAMAGE.play()           

    def damaging(self):
        self.damageCount += 1
        if not self.damageTimer.active:
            self.damageCount = 0
            self.damagingTimer.deactivate()
            return
        if self.damageCount % 2 == 0:
            self.image = pygame.transform.scale(self.frames[self.animationState]["frames"][int(self.frameIndex) % len(self.frames[self.animationState]["frames"])], self.size)
            self.savedImage = self.image
        else:
            self.image = pygame.transform.scale(Sunset.SUNSET_INVIS, self.size) 
            self.savedImage = self.image        

    def animate(self, dt):
        if self.damageTimer.active:
            return
        self.frameIndex += self.frames[self.animationState]["speed"]*dt
        if self.size:
            self.image = pygame.transform.scale(self.frames[self.animationState]["frames"][int(self.frameIndex) % len(self.frames[self.animationState]["frames"])], self.size)
            self.savedImage = self.image
        else:
            self.image = self.frames[self.animationState]["frames"][int(self.frameIndex) % len(self.frames[self.animationState]["frames"])]
            self.savedImage = self.image

    def upgrade(self, type:str, upgradesLevel):
        cost = 0
        match type:
            case "atkSpeed":
                cost = ((upgradesLevel[0]*20) + 40)
                if cost > self.gold or upgradesLevel[0] >= 10:
                    return
                self.atkSpeed += 5
                upgradesLevel[0] += 1
            case "atkDmg":
                cost = ((upgradesLevel[1]*40) + 80)
                if cost > self.gold or upgradesLevel[1] >= 10:
                    return
                self.atkDamage += 1
                upgradesLevel[1] += 1
            case "health":
                cost = ((upgradesLevel[2]*40) + 80)
                if cost > self.gold or upgradesLevel[2] >= 10:
                    return
                self.maxHealth += 1
                self.health += 1
                upgradesLevel[2] += 1
            case "heavyCd":
                cost = ((upgradesLevel[3]*15) + 30)
                if cost > self.gold or upgradesLevel[3] >= 10:
                    return
                self.heavyCd -= 0.5
                upgradesLevel[3] += 1
            case "boostTank":
                cost = ((upgradesLevel[4]*20) + 40)
                if cost > self.gold or upgradesLevel[4] >= 10:
                    return
                self.boostTank += 0.5
                upgradesLevel[4] += 1
            case "boostStrength":
                cost = ((upgradesLevel[5]*40) + 80)
                if cost > self.gold or upgradesLevel[5] >= 10:
                    return
                self.boostStrength += 10
                upgradesLevel[5] += 1
        self.gold -= cost
        Audio.COIN_UP.play()
            
                
class Heavy(pygame.sprite.Sprite):
    def __init__(self, pos:tuple, damage, speed, angle, explosionSize, image, explosionImage, groups, playerOffset:pygame.math.Vector2 = pygame.math.Vector2(0,0), size:tuple = None):
        super().__init__(groups)
        self.isHeavy = True
        self.exploding = False
        self.damage = damage
        self.speed = speed
        self.direction = pygame.math.Vector2(
            math.cos(math.radians(angle)), 
            math.sin(math.radians(angle))
        ).normalize()
        self.explosionSize = explosionSize
        self.explosionImage = explosionImage
        self.explosionPos:pygame.math.Vector2 = pygame.math.Vector2(0,0)
        self.currentSize = 4
        self.savedSize = 0
        self.collidedEnemies = set()
        if size:
            self.image = pygame.transform.scale(image, size)
        else:
            self.image = image
        self.image = pygame.transform.rotate(self.image, -angle-90)
        self.rect = self.image.get_frect(center=pos)
        self.offset = playerOffset

    def draw(self, surface):
        surface.blit(self.image, self.rect)
    
    def update(self, dt):  
        if self.exploding:
            self.savedSize += dt * 200
            self.currentSize = int(self.savedSize) + 4
            self.image = pygame.transform.scale(self.explosionImage, (self.currentSize, self.currentSize))
            self.rect = self.image.get_frect(center = (self.explosionPos.x, self.explosionPos.y))
        else:
            self.rect.center += self.direction * self.speed * dt
        if self.currentSize > self.explosionSize:
            self.kill()
    
    def hit(self, enemy):
        self.collidedEnemies.add(enemy)
        if not self.exploding:
            self.exploding = True
            self.explosionPos = pygame.math.Vector2(self.rect.center)
            Audio.EXPLOSION.play()