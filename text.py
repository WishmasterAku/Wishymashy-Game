import pygame

class Text:
    
    def __init__(self, content, font_name, font_size, color, x, y):
        self.content = content
        self.font = pygame.font.SysFont(font_name, font_size)
        self.color = color
        self.x = x
        self.y = y
        self.surface = self.font.render(self.content, True, self.color)