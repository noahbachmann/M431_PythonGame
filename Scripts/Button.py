import pygame
from Timer import *
import Settings
from AssetsManager import font, BUTTON_IMAGE

class Button(pygame.sprite.Sprite):
    def __init__(self, pos:tuple, image = None, text:str = None, func= None, size:tuple = None, groups = None):
        if groups:
            super().__init__(groups)
        self.func = func
        self.offset = pygame.display.get_window_size()
        self.offset = (self.offset[0] // 2 - Settings.WINDOW_SIZE // 2, self.offset[1] // 2 - Settings.WINDOW_SIZE // 2)
        if image:
            if size:
                self.image = pygame.transform.scale(image, size)
            else:
                self.image = image
        else:
            if size:
                self.image = pygame.transform.scale(BUTTON_IMAGE, size)
            else:
                self.image = BUTTON_IMAGE
        self.text = font.render(text, False, (0,0,0))
        self.textRect = self.text.get_frect(center = pos)
        self.cdTimer = Timer(0.5)
        self.rect = self.image.get_frect(center = pos)

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        surface.blit(self.text, self.textRect)

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