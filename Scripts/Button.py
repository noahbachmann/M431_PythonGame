import pygame
from Scripts.Timer import *
from Scripts.AssetsManager import font, UI_Assets
import Scripts.Settings

class Button(pygame.sprite.Sprite):
    def __init__(self, pos:tuple, image = None, text:str = None, func= None, size:tuple = None, groups = None, icon = None):
        if groups:
            super().__init__(groups)
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
        if text:
            self.text = font.render(text, False, (0,0,0))
            self.textRect = self.text.get_frect(center = pos)
        else:
            self.text = None
        self.cdTimer = Timer(0.3)
        self.rect = self.image.get_frect(center = pos)

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        if self.text:
            surface.blit(self.text, self.textRect)
        if self.icon:
            surface.blit(self.icon, self.iconRect)

    def update(self, surface, dt = None):
        mousePos = pygame.mouse.get_pos()
        mousePos = (mousePos[0] - self.offset[0], mousePos[1] - self.offset[1])
        if self.rect.collidepoint(mousePos):
            if pygame.mouse.get_pressed()[0] and not self.cdTimer.active:
                self.func()
                self.cdTimer.activate()
        
        if self.cdTimer.active:
            self.cdTimer.update()

        self.draw(surface)