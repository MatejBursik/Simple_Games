import pygame
from constants import *
from player import *
from asteroid import *

def lvl2(window):
    running = True
    clock = pygame.time.Clock()

    player = Player(WIDTH//2,HEIGHT//1.5)
    asteroid = Asteroid(WIDTH//2,HEIGHT//2)
    
    bkgd = bkgd = pygame.transform.rotate(pygame.image.load("assets//background//backgroundLight.png").convert(),90)
    bkgd_y = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return True
                
        #actions
        player.control()
        #asteroid.rotate()

        #background scrolling
        new_y = bkgd_y % bkgd.get_rect().height
        window.blit(bkgd, (0,new_y - bkgd.get_rect().height))
        if new_y < HEIGHT:
            window.blit(bkgd, (0,new_y))
        bkgd_y += 1

        #draw
        asteroid.draw(window)
        player.draw(window)

        pygame.display.update()
        clock.tick(FPS)