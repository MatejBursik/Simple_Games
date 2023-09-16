import pygame
from constants import *

class Laser:
    def __init__(self, x, y, direction, sprite):
        self.x = x
        self.y = y
        self.direction = direction
        self.sprite = sprite

        match self.direction:
            case "+x":
                pass
            case "-x":
                self.sprite = pygame.transform.rotate(self.sprite, 180)
            case "+y":
                self.sprite = pygame.transform.rotate(self.sprite, -90)
            case "-y":
                self.sprite = pygame.transform.rotate(self.sprite, 90)
            case _:
                print("Error (no laser direction)")

        self.terminate = False

        self.mask = pygame.mask.from_surface(self.sprite)

    def move(self):
        match self.direction:
            case "+x":
                self.x += VELOCITY*2
            case "-x":
                self.x -= VELOCITY*2
            case "+y":
                self.y += VELOCITY*2
            case "-y":
                self.y -= VELOCITY*2
            case _:
                print("Error (no laser direction)")
    
    def draw(self, window):
        if self.x > WIDTH+50 or self.x < 0-50 or self.y > HEIGHT+50 or self.y < 0-50:
            self.terminate = True

        window.blit(self.sprite, (self.x - self.sprite.get_width()//2, self.y - self.sprite.get_height()//2))
