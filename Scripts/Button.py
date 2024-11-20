import pygame

class Button(pygame.sprite.Sprite):
    def __init__(self, pos:tuple, image, groups, func= None, size:tuple = None):
        super().__init__(groups)
        self.func = func
        self.image = image
        self.rect = self.image.get_frect(topleft = pos)
        self.clicked = False

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self, surface):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0] and not self.clicked:
                self.func()
                self.clicked = True
        else:
            self.clicked = False    

        self.draw(surface)