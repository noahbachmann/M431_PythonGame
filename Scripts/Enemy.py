import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos:tuple, health, damage, speed, image, groups, size:tuple = None):
        super().__init__(groups)
        self.health = health
        self.damage = damage
        self.speed = speed
        if size:
            self.image = pygame.transform.scale(image, size)
        else:
            self.image = image
        self.rect = self.image.get_frect(center=pos)

    def draw(self, surface):
        surface.blit(self.image, self.rect)
    
    def update(self, surface, dt):
        self.rect.center += pygame.math.Vector2(1, 0) * self.speed * dt
        self.draw(surface)
    
    def hit(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.kill()
            del self