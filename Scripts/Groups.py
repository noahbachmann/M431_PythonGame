import pygame
from Settings import *

class AllSprites(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.offset = pygame.Vector2()

    def draw(self, surface):
        for sprite in self:
            surface.blit(sprite.image, sprite.rect)

    def update(self, surface, dt, playerOffset):
        for sprite in self:
            sprite.update(dt)
            offsetDifference = playerOffset - sprite.offset
            sprite.offset += offsetDifference
            if hasattr(sprite, 'isHeavy') and sprite.isHeavy and sprite.exploding:
                sprite.explosionPos -= offsetDifference
            else:
                sprite.rect.move_ip(-offsetDifference.x, -offsetDifference.y)
            surface.blit(sprite.image, sprite.rect)