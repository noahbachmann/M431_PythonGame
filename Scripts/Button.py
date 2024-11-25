import pygame
from Timer import *
from AssetsManager import font, BUTTON_IMAGE

class Button(pygame.sprite.Sprite):
    def __init__(self, pos:tuple, image = None, text:str = None, func= None, size:tuple = None, groups = None):
        if groups:
            super().__init__(groups)
        self.func = func
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
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0] and not self.cdTimer.active:
                self.func()
                self.cdTimer.activate()
        
        if self.cdTimer.active:
            self.cdTimer.update()

        self.draw(surface)