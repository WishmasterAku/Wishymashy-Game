import pygame
from gameObjects import GameObject
from player import Player
from text import Text

class Game:
    
    def __init__(self):
        self.width = 800
        self.height = 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.running = True
        self.background_color = "black"
        self.clock = pygame.time.Clock()
        
        self.background = GameObject(0, 0, self.width, self.height, "images/green_terminal.png")
        self.target_text = Text("Target", "Arial", 20, "white", 75, 150)
        self.player = Player(100, 100, 50, 50, "images/player.png", 2)
        
        self.target = GameObject(75,100,50, 50, "images/17.png")     
               
    def draw_objects(self):
        self.screen.fill(self.background_color)
        self.screen.blit(self.background.image, (self.background.x, self.background.y))
        self.screen.blit(self.player.image, (self.player.x, self.player.y))
        self.screen.blit(self.target.image, (self.target.x, self.target.y))
        self.screen.blit(self.target_text.surface, (self.target_text.x, self.target_text.y))     
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
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        moving_player = 0                      
                        
            self.move_objects(moving_player)
            self.draw_objects()                    
                    
            self.clock.tick(60)