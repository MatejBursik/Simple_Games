import pygame, math
from constants import *

class Asteroid(pygame.sprite.Sprite):
    def __init__(self, x_formula, health=3):
        self.x_formula = str(x_formula)
        self.y = 0
        self.x = eval(self.x_formula.replace("y",str(self.y)))
        self.health = health
        self.sprite = pygame.image.load("assets//asteroid.png")
        self.angle = 15
        
        self.explosions = []
        self.current_explosion = 0
        self.dead = False
        self.terminate = False
        self.explosions.append(pygame.image.load("assets//explosion//explosion1.png"))
        self.explosions.append(pygame.image.load("assets//explosion//explosion2.png"))
        self.explosions.append(pygame.image.load("assets//explosion//explosion3.png"))
        self.explosions.append(pygame.image.load("assets//explosion//explosion4.png"))
        self.explosions.append(pygame.image.load("assets//explosion//explosion5.png"))
        self.explosions.append(pygame.image.load("assets//explosion//explosion6.png"))
        self.explosions.append(pygame.image.load("assets//explosion//explosion7.png"))

        self.mask = pygame.mask.from_surface(self.sprite)

    def rotate(self):
        if not self.dead:
            self.sprite = pygame.transform.rotate(self.sprite, self.angle)

    def explosion(self):
        if self.health == 0:
            self.dead = True
        if len(self.explosions) == self.current_explosion:
            print("remove from existance")

    def draw(self,window):
        if self.dead:
            if self.current_explosion < len(self.explosions)-1:
                self.current_explosion += 0.2
                self.sprite = self.explosions[int(self.current_explosion)]
            else:
                self.terminate = True

        if self.x > WIDTH+50 or self.x < 0-50 or self.y > HEIGHT+50 or self.y < 0-50:
            self.terminate = True
        
        if self.current_explosion < len(self.explosions)-1:
            window.blit(self.sprite, (self.x - self.sprite.get_width()//2, self.y - self.sprite.get_height()//2))
        
        if not self.dead:
            self.y += VELOCITY//2
            self.x = eval(self.x_formula.replace("y",str(self.y)))
            self.mask = pygame.mask.from_surface(self.sprite)
        