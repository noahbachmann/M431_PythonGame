import pygame

class GameWorld:
    def __init__(self):
        self.objects = []
    
    def add_object(self, obj):
        self.objects.append(obj)
    
    def remove_object(self, obj):
        self.objects.remove(obj)
    
    def update(self, surface, dt):
        surface.fill((0, 0, 0))
        for obj in self.objects:
            obj.update(surface, dt)
    
    def draw(self, surface):
        for obj in self.objects:
            obj.draw(surface)