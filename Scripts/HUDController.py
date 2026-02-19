import pygame
import Scripts.Settings
from Scripts.AssetsManager import font, font_32, karmaticArcadeFont, UI_Assets, Heart_Assets, Energybar_Assets, Heavy_Attack_Assets
from Scripts.Button import *
from Scripts.GameMenus import *
from Scripts.Player import *
import Scripts.Settings

class HUDController:
    def __init__(self, surface, player:Player, gameState, hudSpritesGroup):
        self.player = player
        self.playerHealth = self.player.health
        self.pause = False
        self.hudSpritesGroup = hudSpritesGroup
        self._cachedScore = self.player.score
        self._cachedGold = self.player.gold
        self.scoreText = karmaticArcadeFont.render(f"{self.player.score:07d}", True, (255,255,255))
        self.scoreTextRect = self.scoreText.get_frect(topleft = (16, 16))
        self.upgradeButton = Button((Scripts.Settings.WINDOW_SIZE - TILE_SIZE,TILE_SIZE),UI_Assets.BUTTON_32x32, func=self.toggleSettings, icon=UI_Assets.ICON_UPGRADE, size=(64,64))
        self.hudGoldText = font_32.render(f"$ {self.player.gold}", False, (255, 215, 0))
        self.hudGoldRect = self.hudGoldText.get_frect(topright=(Scripts.Settings.WINDOW_SIZE - TILE_SIZE*0.6, TILE_SIZE + 40))
        self.upgradeMenu = UpgradesMenu(surface, (Scripts.Settings.WINDOW_SIZE - 600) // 2, 225, self.player, gameState, self, size=(600, Scripts.Settings.WINDOW_SIZE-450))
        self.hearts = []
        self.heartBar = pygame.transform.scale(Heart_Assets.HEALTHBAR, (128, 44))
        self.heartBarRect = self.heartBar.get_frect(bottomleft = (16, Scripts.Settings.WINDOW_SIZE - 16))
        self.energyBar = EnergyBar((Scripts.Settings.WINDOW_SIZE/2, 16), self.player, Energybar_Assets.ENERGYBAR_ENERGY, Energybar_Assets.ENERGYBAR, (128,32), (80,8))
        self.heavyBar = pygame.transform.scale(Heavy_Attack_Assets.HEAVYATTACKBAR, (128,64))
        self.heavyBarRect = self.heavyBar.get_frect(bottomright = (Scripts.Settings.WINDOW_SIZE - 16, Scripts.Settings.WINDOW_SIZE - 16))
        self.heavyAnimation = HeavyBar((Scripts.Settings.WINDOW_SIZE - 16, Scripts.Settings.WINDOW_SIZE - 16), Heavy_Attack_Assets.HEAVY_ATTACK_CHARGE_13, self.player, Heavy_Attack_Assets.heavyAttackChargeArray, Heavy_Attack_Assets.heavyAttackUsedArray, (128,64))
        self.showHealth()
    
    def draw(self, surface, dt):
        if self.pause:
            self.upgradeMenu.draw(surface)
        else:
            surface.blit(self.heartBar, self.heartBarRect)
            surface.blit(self.heavyBar, self.heavyBarRect)
            self.energyBar.draw(surface)
            self.heavyAnimation.draw(surface, dt)
            surface.blit(self.scoreText, self.scoreTextRect)
            surface.blit(self.hudGoldText, self.hudGoldRect)
            for heart in self.hearts:
               heart.draw(surface)

    def update(self, surface, dt):
        if self.player.score != self._cachedScore:
            self._cachedScore = self.player.score
            self.scoreText = karmaticArcadeFont.render(f"{self.player.score:07d}", True, (255,255,255))
        if self.player.gold != self._cachedGold:
            self._cachedGold = self.player.gold
            self.hudGoldText = font.render(f"$ {self.player.gold}", False, (255, 215, 0))
        self.upgradeButton.update(surface)
        if self.playerHealth != self.player.health:
            if self.pause:
                self.healthUpgrade()
            else:
                self.takeDamage()
        self.draw(surface, dt)

    def toggleSettings(self):
        self.pause = True

    def showHealth(self):
        x = 78
        y = Scripts.Settings.WINDOW_SIZE - 34
        maxHealth = self.player.maxHealth // 2
        for i in range(maxHealth):
            self.hearts.append(Heart((x,y),Heart_Assets.HEART_FULL, (20,20)))
            x += 30
        if self.player.maxHealth % 2 != 0:
            self.hearts.append(Heart((x,y),Heart_Assets.HALFHEART_FULL, (20,20)))
        
    def takeDamage(self):
        if self.player.maxHealth % 2 != 0 and self.player.health == self.player.maxHealth - 1:
            self.hearts[len(self.hearts)-1].newImage(Heart_Assets.HALFHEART_EMPTY)
        elif self.player.health % 2 != 0:
            self.hearts[self.player.health // 2].newImage(Heart_Assets.HEART_HALFFULL)
        else:
            self.hearts[self.player.health // 2].newImage(Heart_Assets.HEART_EMPTY)
        self.playerHealth = self.player.health
    
    def healthUpgrade(self):
        x = 78
        y = Scripts.Settings.WINDOW_SIZE - 34
        if self.player.maxHealth / 2 > len(self.hearts):
            if self.player.maxHealth == self.player.health:
                self.hearts.append(Heart((x+(30*len(self.hearts)),y),Heart_Assets.HALFHEART_FULL, (20,20)))
            else:
                self.hearts.append(Heart((x+(30*len(self.hearts)),y),Heart_Assets.HALFHEART_EMPTY, (20,20)))
        if self.player.health != self.playerHealth:
            if self.player.health % 2 == 0:
                self.hearts[(self.player.health // 2)-1].newImage(Heart_Assets.HEART_FULL)
            else:
                self.hearts[self.player.health // 2].newImage(Heart_Assets.HEART_HALFFULL)           
            if self.player.maxHealth % 2 == 0 and self.player.maxHealth != self.player.health:
                self.hearts[len(self.hearts)-1].newImage(Heart_Assets.HEART_EMPTY)
            self.playerHealth = self.player.health

_heartCache = {}
def _getScaledHeart(image, size):
    key = id(image)
    if key not in _heartCache:
        _heartCache[key] = pygame.transform.scale(image, size)
    return _heartCache[key]

class Heart(pygame.sprite.Sprite):
    def __init__(self, pos:tuple, image, size:tuple = None ):
        super().__init__()
        if size:
            self.image = _getScaledHeart(image, size)
            self.size = size
        else:
            self.image = image
        self.rect = self.image.get_frect(center=pos)

    def newImage(self, image):
        if self.size:
            self.image = _getScaledHeart(image, self.size)
        else:
            self.image = image

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class EnergyBar(pygame.sprite.Sprite):
    def __init__(self, pos:tuple, player, barImage, image, size:tuple = None, barSize:tuple =None):
        super().__init__()
        self.player = player
        if size:
            self.image = pygame.transform.scale(image, size)
            self.barImage = pygame.transform.scale(barImage, barSize)
            self.size = size
            self.barSize = barSize
        else:
            self.image = image
            self.barImage = barImage
        self.rect = self.image.get_frect(center = pos)
        self.barRect = self.barImage.get_frect(center = (pos[0], pos[1]+2))

    def draw(self, surface):
        energyPercentage = self.player.boostAmount / self.player.boostTank
        barWidth = self.barSize[0] * energyPercentage
        surface.blit(self.image, self.rect)
        surface.blit(self.barImage, self.barRect, (0,0,barWidth,self.barSize[0]))

class HeavyBar(pygame.sprite.Sprite):
    def __init__(self, pos:tuple, image, player, rechargeArray, triggerArray, size):
        super().__init__()
        self.pos = pos
        self.size = size
        self.player = player
        self.scaledRechargeArray = [pygame.transform.scale(f, size) for f in rechargeArray]
        self.scaledTriggerArray = [pygame.transform.scale(f, size) for f in triggerArray]
        self.animationState = "charged"
        self.heavyState = "charged"
        self.frameIndex = 0
        self.defaultImage = pygame.transform.scale(image, self.size)
        self.image = self.defaultImage
        self.rect = self.image.get_frect(bottomright=self.pos)

    def draw(self, surface, dt):
        if self.player.heavyState == "recharging" and self.animationState == "charged":
            self.animationState = "used"
        self.animate(dt)
        surface.blit(self.image, self.rect)


    def animate(self, dt):
        if self.animationState == "charged":
            return
        if self.animationState == "used":
            self.frameIndex += 25*dt
            self.image = self.scaledTriggerArray[int(self.frameIndex) % len(self.scaledTriggerArray)]
            if int(self.frameIndex) != 0 and int(self.frameIndex) % len(self.scaledTriggerArray) == 0:
                self.animationState = "recharging"
                self.frameIndex = 0
        elif self.animationState == "recharging":
            self.frameIndex += (self.player.heavyCd/4.8)*dt
            self.image = self.scaledRechargeArray[int(self.frameIndex) % len(self.scaledRechargeArray)]
            if not self.player.heavyCdTimer.active:
                self.animationState = "charged"
                self.image = self.defaultImage
                self.frameIndex = 0