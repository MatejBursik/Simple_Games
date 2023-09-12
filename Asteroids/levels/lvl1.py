import pygame
from constants import *
from player import *
from asteroid import *

def lvl1(window):
    running = True
    clock = pygame.time.Clock()

    player = Player(WIDTH//2,HEIGHT//1.5)

    # asteroids spawn data [x=, repeate]
    asteroids = []
    formulas = [
        ["y+5",3],
        ["-y+500",3],
        ["2*y",3],
        ["-0.1*y+200",3],
        ["0*y+100",3]
    ]
    
    bkgd = pygame.transform.rotate(pygame.image.load("assets//background//background.png").convert(),90)
    bkgd_y = 0

    counter = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return True
                
        # asteroid spawning
        if counter%15 == 0 and len(formulas) > 0:
            asteroids.append(Asteroid(formulas[0][0]))
            formulas[0][1] -= 1
            if formulas[0][1] == 0:
                formulas.pop(0)
        
        #actions
        player.control()
        player.explosion()
        """
        for ast in asteroids:
            ast.rotate()
        """

        # collisions player.mask.overlap(ast.mask,(ast.x - player.x, ast.y - player.y))
        for ast in asteroids:
            player.hit(ast)
            if collide(player,ast):
                player.health -= 1
                ast.health -= 1
        
        #background scrolling
        new_y = bkgd_y % bkgd.get_rect().height
        window.blit(bkgd, (0,new_y - bkgd.get_rect().height))
        if new_y < HEIGHT:
            window.blit(bkgd, (0,new_y))
        bkgd_y += 1

        #draw
        for ast in asteroids:
            if ast.terminate:
                asteroids.remove(ast)
                continue
            ast.explosion()
            ast.draw(window)
        player.draw(window)

        counter += 1
        pygame.display.update()
        clock.tick(FPS)
