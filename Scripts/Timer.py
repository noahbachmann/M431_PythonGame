from pygame.time import get_ticks

class Timer:
    def __init__(self, duration, repeat=False, autostart = False, func = None):
        self.duration = duration
        self.start_time = 0
        self.active = False
        self.repeat = repeat
        self.func = func
        if autostart:
            self.activate()

    def activate(self):
        self.active = True
        self.start_time = get_ticks()
    
    def deactivate(self):
        self.active = False
        self.start_time = 0      
    
    def update(self):
        if not self.active: return
        current_time = get_ticks()
        if current_time - self.start_time >= self.duration*1000:
            if self.func: 
                self.func()
            if self.repeat:
                self.start_time = current_time
            else:
                self.deactivate()