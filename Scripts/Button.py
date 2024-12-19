import pygame
import time
from Scripts.Timer import *
from Scripts.AssetsManager import font, UI_Assets, Audio
import Scripts.Settings
import Scripts.DataManager

class Button(pygame.sprite.Sprite):
    def __init__(self, pos:tuple, image = None, text:str = None, func= None, size:tuple = None, groups = None, icon = None, keyText = False):
        if groups:
            super().__init__(groups)
        self.pos = pos
        self.func = func
        self.offset = pygame.display.get_window_size()
        self.offset = (self.offset[0] // 2 - Scripts.Settings.WINDOW_SIZE // 2, self.offset[1] // 2 - Scripts.Settings.WINDOW_SIZE // 2)
        if image:
            if size:
                self.image = pygame.transform.scale(image, size)
            else:
                self.image = image
        else:
            if size:
                self.image = pygame.transform.scale(UI_Assets.BUTTON_32x32, size)
            else:
                self.image = pygame.transform.scale(UI_Assets.BUTTON_32x32, (64,64))
        if icon:
            self.icon = pygame.transform.scale(icon, (48, 48))
            self.iconRect = self.icon.get_frect(center = pos)
        else:
            self.icon = None
        self.keyText = keyText
        if self.keyText:
            self.text = text
            self.textRect = None
        elif text:
            self.text = font.render(text, False, (0,0,0))
            self.textRect = self.text.get_frect(center = pos)
        else:
            self.text = None
        self.cdTimer = Timer(0.3)
        self.rect = self.image.get_frect(center = pos)

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        if self.text:
            if self.keyText:
                textInfo = None
                if self.text == 'Up':
                    textInfo = font.render(pygame.key.name(Scripts.DataManager.dataJson['Hotkey_Up']), False, (0,0,0))
                elif self.text == 'Down':
                    textInfo = font.render(pygame.key.name(Scripts.DataManager.dataJson['Hotkey_Down']), False, (0,0,0))
                elif self.text == 'Left':
                    textInfo = font.render(pygame.key.name(Scripts.DataManager.dataJson['Hotkey_Left']), False, (0,0,0))
                elif self.text == 'Right':
                    textInfo = font.render(pygame.key.name(Scripts.DataManager.dataJson['Hotkey_Right']), False, (0,0,0))
                elif self.text == 'Boost':
                    textInfo = font.render(pygame.key.name(Scripts.DataManager.dataJson['Hotkey_Boost']), False, (0,0,0))
                elif self.text == 'close':
                    textInfo = font.render(pygame.key.name(Scripts.DataManager.dataJson['Hotkey_close']), False, (0,0,0))
                elif self.text == 'Attack':
                    textInfo = font.render(pygame.key.name(Scripts.DataManager.dataJson['Hotkey_Attack']), False, (0,0,0))
                elif self.text == 'HeavyAttack':
                    textInfo = font.render(pygame.key.name(Scripts.DataManager.dataJson['Hotkey_HeavyAttack']), False, (0,0,0))
                self.textRect = textInfo.get_frect(center = self.pos)
                surface.blit(textInfo, self.textRect)
            else:
                surface.blit(self.text, self.textRect)
        if self.icon:
            surface.blit(self.icon, self.iconRect)

    def update(self, surface, dt = None):
        mousePos = pygame.mouse.get_pos()
        mousePos = (mousePos[0] - self.offset[0], mousePos[1] - self.offset[1])
        if self.rect.collidepoint(mousePos):
            if pygame.mouse.get_pressed()[0] and not self.cdTimer.active:
                time.sleep(0.15)
                self.func()
                Audio.BUTTON_PRESS.play()
                self.cdTimer.activate()
        
        if self.cdTimer.active:
            self.cdTimer.update()

        self.draw(surface)