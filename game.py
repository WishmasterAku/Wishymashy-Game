import pygame


class Game:
    
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        self.running = True
        self.background_color = "black"
        self.clock = pygame.time.Clock()
        
        
    def game_start(self):
        
        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    return
                else:
                    return
                    
                    
                    
                    
            self.clock.tick(60)