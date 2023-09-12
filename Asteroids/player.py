import pygame
from constants import *
from laser import *

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, health = 5):
        self.x = x
        self.y = y
        self.health = health
        self.sprites = []
        self.current_sprite = 0
        self.animate = False
        
        self.sprites.append(pygame.image.load("assets//ship//ship(stationary).png"))
        self.sprites.append(pygame.image.load("assets//ship//ship(a1).png"))
        self.sprites.append(pygame.image.load("assets//ship//ship(a2).png"))
        self.sprites.append(pygame.image.load("assets//ship//ship(a3).png"))

        self.explosions = []
        self.current_explosion = 0
        self.dead = False
        self.explosions.append(pygame.image.load("assets//explosion//explosion1.png"))
        self.explosions.append(pygame.image.load("assets//explosion//explosion2.png"))
        self.explosions.append(pygame.image.load("assets//explosion//explosion3.png"))
        self.explosions.append(pygame.image.load("assets//explosion//explosion4.png"))
        self.explosions.append(pygame.image.load("assets//explosion//explosion5.png"))
        self.explosions.append(pygame.image.load("assets//explosion//explosion6.png"))
        self.explosions.append(pygame.image.load("assets//explosion//explosion7.png"))

        self.mask = pygame.mask.from_surface(self.sprites[0])

        self.laser_img = pygame.image.load("assets//laser(green).png")
        self.lasers = []
        self.laser_cool_down = 0

    def shoot(self):
        if self.laser_cool_down == 0 and not self.dead:            
            self.lasers.append(Laser(self.x, self.y, "-y", self.laser_img))
            self.laser_cool_down = 10

    def control(self):
        if not self.dead:
            self.animate = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w] and self.y > 0:
                self.y -= VELOCITY
                self.animate = True
            elif keys[pygame.K_s] and (HEIGHT - self.sprites[0].get_rect().height) > self.y:
                self.y += VELOCITY
                self.animate = True
            if keys[pygame.K_a] and self.x > 0:
                self.x -= VELOCITY
                self.animate = True
            elif keys[pygame.K_d] and (WIDTH - self.sprites[0].get_rect().width) > self.x:
                self.x += VELOCITY
                self.animate = True
            if keys[pygame.K_v]:
                self.shoot()

            self.mask = pygame.mask.from_surface(self.sprites[0])
        else:
            if self.current_explosion > len(self.explosions)-1:
                self.y = -50
                self.x = -50
                self.mask = pygame.mask.from_surface(self.sprites[0])

    def explosion(self):
        if self.health == 0:
            self.dead = True
        if len(self.explosions) == self.current_explosion:
            print("remove from existance")

    def hit(self, obj):
        for laser in self.lasers:
            if collide(laser, obj):
                obj.health -= 1
    
    def draw(self, window):
        if self.dead:
            if self.current_explosion < len(self.explosions)-1:
                self.current_explosion += 0.2
                sprite = self.explosions[int(self.current_explosion)]
        else:
            if self.animate:
                self.current_sprite += 0.5
                if self.current_sprite > len(self.sprites)-1:
                    self.current_sprite = 1
            else:
                self.current_sprite = 0

            sprite = self.sprites[int(self.current_sprite)]
        
        if self.current_explosion < len(self.explosions)-1:
            if self.laser_cool_down > 0:
                self.laser_cool_down -= 1
            for laser in self.lasers:
                if laser.terminate:
                    self.lasers.remove(laser)
                    continue
                laser.move()
                laser.draw(window)
            window.blit(sprite, (self.x - sprite.get_width()//2, self.y - sprite.get_height()//2))
