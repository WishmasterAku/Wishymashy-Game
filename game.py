import pygame


class Game:
    
    def __init__(self):
        self.width = 800
        self.height = 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.running = True
        self.background_color = "black"
        self.clock = pygame.time.Clock()
        
        
    def start_game(self):
        
        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    return False
                    
                
                    
                    
                    
                    
            self.clock.tick(60)