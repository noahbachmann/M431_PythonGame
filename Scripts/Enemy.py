import pygame

class Enemy:
    def __init__(self, x: float, y:float, image, size:tuple = None):
        self.speed = 100
        if size:
            self.image = pygame.transform.scale(image, size)
        else:
            self.image = image
        self.rect = self.image.get_frect(center=(x, y))

    def draw(self, surface):
        surface.blit(self.image, self.rect)
    
    def update(self, surface, dt):
        self.rect.center += pygame.math.Vector2(1, 0) * self.speed * dt
        self.draw(surface)