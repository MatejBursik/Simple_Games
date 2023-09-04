import pygame
from constants import *
from button import *

def startMenu(window):
    running = True
    clock = pygame.time.Clock()
    button = Button(WIDTH*0.4, HEIGHT*0.45, pygame.image.load("assets//buttons//start.png"))
    button.draw(window)
    pygame.display.update()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button.rect.collidepoint(event.pos):
                    return True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return True
                if event.key == pygame.K_ESCAPE:
                    return  False     
        
        clock.tick(FPS)
        