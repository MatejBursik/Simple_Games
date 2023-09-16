import pygame, random
from constants import *
from laser import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self, position, direction, travel_end, health = 5):
        self.direction = direction
        match self.direction:
            case "+x":
                rotate = -90
                self.y = position
                self.x = 0
            case "-x":
                rotate = 90
                self.y = position
                self.x = WIDTH
            case "+y":
                rotate = 180
                self.y = 0
                self.x = position
            case _:
                print("Error (no enemy direction)")

        self.travel_end = travel_end
        self.travel_dist = 0
        self.health = health
        self.sprites = []
        self.current_sprite = 0
        self.animate = False
        
        self.sprites.append(pygame.transform.rotate(pygame.image.load("assets//enemy(stationary).png"),rotate))
        self.sprites.append(pygame.transform.rotate(pygame.image.load("assets//enemy(a1).png"),rotate))
        self.sprites.append(pygame.transform.rotate(pygame.image.load("assets//enemy(a2).png"),rotate))

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

        self.mask = pygame.mask.from_surface(self.sprites[0])

        self.laser_img = pygame.image.load("assets//laser(red).png")
        self.lasers = []
        self.laser_cool_down = 0

    def shoot(self):
        if self.laser_cool_down == 0 and not self.dead:            
            self.lasers.append(Laser(self.x, self.y, self.direction, self.laser_img))
            self.laser_cool_down = 30

    def move(self):
        if not self.dead:
            self.animate = False
            if self.travel_end > self.travel_dist:
                self.animate = True
                match self.direction:
                    case "+x":
                        self.x += VELOCITY
                        self.travel_dist += VELOCITY
                    case "-x":
                        self.x -= VELOCITY
                        self.travel_dist += VELOCITY
                    case "+y":
                        self.y += VELOCITY
                        self.travel_dist += VELOCITY
                    case _:
                        print("Error (no enemy direction)")

            self.mask = pygame.mask.from_surface(self.sprites[0])
        else:
            if self.current_explosion > len(self.explosions)-1:
                self.terminate = True

    def explosion(self):
        if self.health == 0:
            self.dead = True
        if len(self.explosions) == self.current_explosion:
            print("remove from existance")

    def hit(self, obj):
        for laser in self.lasers:
            if collide(laser, obj):
                obj.health -= 1
                laser.terminate = True
    
    def draw(self, window):
        # enemy draw
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
            window.blit(sprite, (self.x - sprite.get_width()//2, self.y - sprite.get_height()//2))

        # laser draw
        self.shoot()
        if self.laser_cool_down > 0:
            self.laser_cool_down -= 1
        for laser in self.lasers:
            if laser.terminate:
                self.lasers.remove(laser)
                continue
            laser.move()
            laser.draw(window)
