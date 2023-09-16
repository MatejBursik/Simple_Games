import pygame
from constants import *
from player import *
from enemy import *
from asteroid import *

def lvl1(window):
    running = True
    clock = pygame.time.Clock()

    player = Player(WIDTH//2,HEIGHT//1.5)
    
    

    # asteroids spawn data [x=, repeate]
    asteroids = []
    asteroid_path = [
        ["y+5",3],
        ["-y+500",3],
        ["2*y",3],
        ["-0.1*y+200",3],
        ["0*y+100",3]
    ]

    # enemy spawn data [position, direction, travel_end]
    enemies = []
    enemy_path = [
        [WIDTH//2, "+y", HEIGHT//4],
        [HEIGHT//2, "+x", WIDTH//4],
        [HEIGHT//2, "-x", WIDTH//4]
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
        if counter%30 == 0 and len(asteroid_path) > 0:
            asteroids.append(Asteroid(asteroid_path[0][0]))
            asteroid_path[0][1] -= 1
            if asteroid_path[0][1] == 0:
                asteroid_path.pop(0)

        # enemy spawning
        if counter%100 == 0 and len(enemy_path) > 0:
            enemies.append(Enemy(enemy_path[0][0], enemy_path[0][1], enemy_path[0][2]))
            enemy_path.pop(0)
        
        # actions
        player.control()
        player.explosion()
        for enemy in enemies:
            enemy.move()
            enemy.explosion()
        """
        for ast in asteroids:
            ast.rotate()
        """

        # collisions (asteroids & player)
        for ast in asteroids:
            player.hit(ast)
            if collide(player,ast):
                player.health -= 1
                ast.health -= 1

        # collisions (enemy & player)
        for enemy in enemies:
            enemy.hit(player)
            player.hit(enemy)

        # background scrolling
        new_y = bkgd_y % bkgd.get_rect().height
        window.blit(bkgd, (0,new_y - bkgd.get_rect().height))
        if new_y < HEIGHT:
            window.blit(bkgd, (0,new_y))
        bkgd_y += 1

        # draw
        for ast in asteroids:
            if ast.terminate:
                asteroids.remove(ast)
                continue
            ast.explosion()
            ast.draw(window)
        for enemy in enemies:
            enemy.draw(window)
        player.draw(window)

        counter += 1
        pygame.display.update()
        clock.tick(FPS)
