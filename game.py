import pygame
from gameObjects import GameObject
from player import Player

class Game:
    
    def __init__(self):
        self.width = 800
        self.height = 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.running = True
        self.background_color = "black"
        self.clock = pygame.time.Clock()
        
        self.background = GameObject(0, 0, self.width, self.height, "images/background.png")
        self.player = Player(100, 100, 50, 50, "images/player.png", 5)
        
    def draw_objects(self):
        self.screen.fill(self.background_color)
        self.screen.blit(self.background.image, (self.background.x, self.background.y))
        self.screen.blit(self.player.image, (self.player.x, self.player.y))
        
        pygame.display.update()   
        
    def move_objects(self, moving_player):
        self.player.movement(moving_player, self.height, self.width)
        
    def start_game(self):
        
        moving_player = 0
        
        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    return
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        moving_player = "right"
                    elif event.key == pygame.K_LEFT:
                        moving_player = "left"
                    elif event.key == pygame.K_UP:
                        moving_player = "up"
                    elif event.key == pygame.K_DOWN:
                        moving_player = "down"
                        
                        
                    
                    
                
                    
            self.move_objects(moving_player)
            self.draw_objects()
                    
                    
            self.clock.tick(60)