import pygame

class Target:
    def __init__(self, x, y, image, size = None):
        self.x = x
        self.y = y
        if size:
            self.image = pygame.transform.scale(image, size)
        else:
            self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))