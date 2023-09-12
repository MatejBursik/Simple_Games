import pygame
from constants import *
from menus import *
from button import *

from levels.level import *
from levels.lvl1 import *
from levels.lvl2 import *
from levels.lvl3 import *
from levels.lvl4 import *
from levels.lvl5 import *

pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT),pygame.NOFRAME)
clock = pygame.time.Clock()

buttons = [
    Button(WIDTH*0.25, HEIGHT*0.2, pygame.image.load("assets//buttons//lvl1.png")),
    Button(WIDTH*0.25, HEIGHT*0.35, pygame.image.load("assets//buttons//lvl2.png")),
    Button(WIDTH*0.25, HEIGHT*0.5, pygame.image.load("assets//buttons//lvl3.png")),
    Button(WIDTH*0.25, HEIGHT*0.65, pygame.image.load("assets//buttons//lvl4.png")),
    Button(WIDTH*0.25, HEIGHT*0.8, pygame.image.load("assets//buttons//lvl5.png"))
]

running = startMenu(window)

while running:
    # draw buttons
    pygame.draw.rect(window, (0, 0, 0), pygame.Rect(0, 0, WIDTH, HEIGHT))
    for btn in buttons:
        btn.draw(window)

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # level choosing by pressing button
            for i,button in enumerate(buttons):
                if button.rect.collidepoint(event.pos):
                    match i+1:
                        case 1:
                            running = lvl1(window)
                        case 2:
                            running = lvl2(window)
                        case 3:
                            running = lvl3(window)
                        case 4:
                            running = lvl4(window)
                        case 5:
                            running = lvl5(window)
                        case _:
                            print("Error (no lvl)")
    
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()