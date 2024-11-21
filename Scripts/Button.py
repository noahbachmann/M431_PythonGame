import pygame
from Timer import *
from AssetsManager import font

class Button(pygame.sprite.Sprite):
    def __init__(self, pos:tuple, image, groups, text:str = None, func= None, size:tuple = None):
        super().__init__(groups)
        self.func = func
        self.image = image
        self.text = font.render(text, False, (0,0,0))
        self.textRect = self.text.get_frect(center = (pos))
        self.cdTimer = Timer(0.5)
        self.rect = self.image.get_frect(center = pos)

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        surface.blit(self.text, self.textRect)

    def update(self, surface, dt = None):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0] and not self.cdTimer.active:
                self.func()
                self.cdTimer.activate()
        
        if self.cdTimer.active:
            self.cdTimer.update()

        self.draw(surface)