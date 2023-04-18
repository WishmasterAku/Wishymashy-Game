import pygame


class Game:
    
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        self.running = True