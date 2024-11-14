import pygame

class Player:
    def __init__(self, x: float, y:float, image, size:tuple = None):
        self.direction = "top"
        self.speed = 100
        if size:
            self.image = pygame.transform.scale(image, size)
        else:
            self.image = image
        self.rect = self.image.get_frect(center=(x, y))

    def draw(self, surface):
        rotatedImage = self.getRotatedImage()
        surface.blit(rotatedImage, self.rect)

    def getRotatedImage(self):
        if self.direction == "top":
            return self.image 
        elif self.direction == "right":
            return pygame.transform.rotate(self.image, -90)
        elif self.direction == "bottom":
            return pygame.transform.rotate(self.image, 180)
        elif self.direction == "left":
            return pygame.transform.rotate(self.image, 90)
    
    def getDirection(self):
        if self.direction == "top":
            return pygame.math.Vector2(0, -1)
        elif self.direction == "right":
            return pygame.math.Vector2(1, 0)
        elif self.direction == "bottom":
            return pygame.math.Vector2(0, 1)
        elif self.direction == "left":
            return pygame.math.Vector2(-1, 0)

    def update(self, surface, dt):   
        self.rect.center += self.getDirection() * self.speed * dt
        self.draw(surface)