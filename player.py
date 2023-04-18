import pygame

class Player(GameObject):
    
    def __init__(self, x, y, width, height, image_path, speed):
        super().__init__(x, y, width, height, image_path)
        self.speed = speed
        
        
    def movement(self, direction, max_height, max_width):
        if direction == "right":
            if self.x + self.width + self.speed < max_width:
                self.x += self.speed
        if direction == "left":
            if self.x - self.speed > 0:
                self.x -= self.speed
        if direction == "up":
            if self.y - self.speed > 0:
                self.y -= self.speed
        if direction == "down":
            if self.y + self.height + self.speed < max_height:
                self.y += self.speed