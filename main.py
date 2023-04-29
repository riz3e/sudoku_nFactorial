import pygame
import random

pygame.init()
# Settings
screen_size = 600, 500 #450, 450
game_caption = ' '
zero = (66, 17)
# Colors

BorderColor = 0,0,0
BlockColor = 79, 88, 92
BackgroundColor = 255,255,255
HPbarColor = 200, 50, 50
PCNameBackColor = 100, 100, 100
MoveColor = 18, 33, 42
Red = 255, 105, 97
Green = 140, 200, 140
Blue = 138, 208, 240

#
def plus_set(a: tuple, b: tuple):
    a = list(a)
    b = list(b)
    return a[0] + b[0], a[1] + b[1]
def grid(Screen):
    global zero, BorderColor
    # Horizontal grid BOLD

    pygame.draw.line(Screen, BorderColor,
                     zero, plus_set(zero, (450, 0)),
                     width=3)
    pygame.draw.line(Screen, BorderColor,
                     plus_set(zero, (0, 150)), plus_set(zero, (450, 150)),
                     width=3)
    pygame.draw.line(Screen, BorderColor,
                     plus_set(zero, (0, 300)), plus_set(zero, (450, 300)),
                     width=3)
    pygame.draw.line(Screen, BorderColor,
                     plus_set(zero, (0, 450)), plus_set(zero, (450, 450)),
                     width=3)
    # Vertical grid BOLD
    pygame.draw.line(Screen, BorderColor,
                     zero, plus_set(zero, (0, 450)),
                     width=3)
    pygame.draw.line(Screen, BorderColor,
                     plus_set(zero, (150, 0)), plus_set(zero, (150, 450)),
                     width=3)
    pygame.draw.line(Screen, BorderColor,
                     plus_set(zero, (300, 0)), plus_set(zero, (300, 450)),
                     width=3)
    pygame.draw.line(Screen, BorderColor,
                     plus_set(zero, (450, 0)), plus_set(zero, (450, 450)),
                     width=3)
    # Horizontal grid
    pygame.draw.line(Screen, BorderColor,
                     plus_set(zero, (0, 50)),
                     plus_set(zero, (450, 50)),
                     width=2)
    pygame.draw.line(Screen, BorderColor,
                     plus_set(zero, (0, 100)),
                     plus_set(zero, (450, 100)),
                     width=2)
    pygame.draw.line(Screen, BorderColor,
                     plus_set(zero, (0, 200)),
                     plus_set(zero, (450, 200)),
                     width=2)
    pygame.draw.line(Screen, BorderColor,
                     plus_set(zero, (0, 250)),
                     plus_set(zero, (450, 250)),
                     width=2)
    pygame.draw.line(Screen, BorderColor,
                     plus_set(zero, (0, 200)),
                     plus_set(zero, (450, 200)),
                     width=2)
    pygame.draw.line(Screen, BorderColor,
                     plus_set(zero, (0, 350)),
                     plus_set(zero, (450, 350)),
                     width=2)
    pygame.draw.line(Screen, BorderColor,
                     plus_set(zero, (0, 400)),
                     plus_set(zero, (450, 400)),
                     width=2)
    # Vertical grid
    pygame.draw.line(Screen, BorderColor,
                     plus_set(zero, (50, 0)),
                     plus_set(zero, (50, 450)),
                     width=2)
    pygame.draw.line(Screen, BorderColor,
                     plus_set(zero, (100, 0)),
                     plus_set(zero, (100, 450)),
                     width=2)
    pygame.draw.line(Screen, BorderColor,
                     plus_set(zero, (200, 0)),
                     plus_set(zero, (200, 450)),
                     width=2)
    pygame.draw.line(Screen, BorderColor,
                     plus_set(zero, (250, 0)),
                     plus_set(zero, (250, 450)),
                     width=2)
    pygame.draw.line(Screen, BorderColor,
                     plus_set(zero, (350, 0)),
                     plus_set(zero, (350, 450)),
                     width=2)
    pygame.draw.line(Screen, BorderColor,
                     plus_set(zero, (400, 0)),
                     plus_set(zero, (400, 450)),
                     width=2)


Screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption(game_caption)

Run = True
Start = True
Game = True

while Run:
    mouse_pos = -1, -1
    Screen.fill(BackgroundColor)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            Run = False

        if event.type == pygame.KEYDOWN:
            key = event.key
            if key == pygame.K_ESCAPE and Game:
                Game = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()

    if Game:
        if Start:
            pass

        mouse_pos = None
        # Grid
        grid(Screen)

        # if PA.hp == 0 or PB.hp == 0:
        #     Game = False

    if not Game:

        Game = True
        Start = True

    pygame.display.update()
