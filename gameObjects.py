import pygame

class GameObject:
    
    def __init__(self, x, y, width, height, image_path):
        image = pygame.image.load(image_path)
        
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = pygame.image.load(image_path)