#
#   proto.py is my previous proj on pygame I used now as an pygame syntax tip, nevermind
#
import pygame
import random

pygame.init()

# Resolution
screen_size = 800, 800
Screen = pygame.display.set_mode(screen_size)

# Game title
pygame.display.set_caption(' ')

# Colors
BorderColor = 180, 182, 185
BlockColor = 79, 88, 92
BackgroundColor = 0, 0, 0
HPbarColor = 200, 50, 50
PCNameBackColor = 100, 100, 100
MoveColor = 18, 33, 42
Red = 255, 105, 97
Green = 140, 200, 140
Blue = 138, 208, 240
#

x = random.randint(0, 7) * 100
y = random.randint(0, 6) * 100
x1 = random.randint(0, 7) * 100
y1 = random.randint(0, 6) * 100
x2 = random.randint(0, 7) * 100
y2 = random.randint(0, 6) * 100
S = 100
block = set()  # blocked cells


# Player: .x, .y, .hp
class Player:  # hp, x, y
    hp = 100

    def __init__(self, x, y, hit):
        self.x = x
        self.y = y
        self.punch = hit


def player_attack(A, B):  # attack players
    A.hp = A.hp - B.punch


# Players
PA = Player(x * 100, y * 100, 10)
PB = Player(x1 * 100, y1 * 100, 20)
PC = Player(x2 * 100, y2 * 100, 0)
PC.hp = -1  # immortal
#

Queue = 1


def Draw_text():
    if Queue == 0:
        Text = 'Red player'
    elif Queue == 1:
        Text = 'Green player'
    elif Queue == -1:
        Text = 'Blue player'
    Font = pygame.font.Font(None, 50)
    Font1 = pygame.font.Font(None, 17)
    Que = Font.render(Text, True, (255, 255, 255))
    Hp = Font1.render('Red player HP', True, 20)
    Hp1 = Font1.render('Green player HP', True, 20)
    Hp2 = Font1.render('Blue player', True, 20)
    Screen.blit(Que, (300, 730))
    Screen.blit(Hp, (PA.x + 12, PA.y + 10))
    Screen.blit(Hp1, (PB.x + 8, PB.y + 10))
    Screen.blit(Hp2, (PC.x + 20, PC.y + 10))


def draw_map():  # Draw map
    for xi in range(0, 800, S):
        for yi in range(0, 701, S):
            pygame.draw.line(Screen, BorderColor, (xi, 0), (xi, yi))
            pygame.draw.line(Screen, BorderColor, (0, yi), (800, yi))


def Players(mouse_pos, PA, PB, PC):  # Player move
    global Queue
    if mouse_pos is not None:
        if Queue == 1:
            # if key == pygame.K_a and PB.x > 0:  # A
            if PB.x - S <= mouse_pos[0] <= PB.x and PB.y <= mouse_pos[1] <= PB.y + S and PB.x > 0:
                PB.x -= S
                Queue = 0
                if PB.x == PA.x and PA.y == PB.y:
                    player_attack(PA, PB)
                    PB.x += S
                elif PC.x == PB.x and PC.y == PB.y:
                    PB.x += S
                    Queue = 1
                elif str(PB.x) + "," + str(PB.y) in block:
                    PB.x += S
                    Queue = 1
            # elif key == pygame.K_d and PB.x < 800 - S:  # D
            elif PB.x + S <= mouse_pos[0] <= PB.x + 2 * S and PB.y <= mouse_pos[1] <= PB.y + S and PB.x < 800 - S:
                PB.x += S
                Queue = 0
                if PB.x == PA.x and PA.y == PB.y:
                    player_attack(PA, PB)
                    PB.x -= S
                elif PC.x == PB.x and PC.y == PB.y:
                    PB.x -= S
                    Queue = 1
                elif str(PB.x) + "," + str(PB.y) in block:
                    PB.x -= S
                    Queue = 1
            elif PB.x <= mouse_pos[0] <= PB.x + S and PB.y - S <= mouse_pos[1] <= PB.y and PB.y > 0:
                PB.y -= S
                Queue = 0
                if PB.x == PA.x and PA.y == PB.y:
                    player_attack(PA, PB)
                    PB.y += S
                elif PC.x == PB.x and PC.y == PB.y:
                    PB.y += S
                    Queue = 1
                elif str(PB.x) + "," + str(PB.y) in block:
                    PB.y += S
                    Queue = 1
            elif PB.x <= mouse_pos[0] <= PB.x + S and PB.y + S <= mouse_pos[1] <= PB.y + 2 * S and PB.y < 701 + S * 2:
                PB.y += S
                Queue = 0
                if PB.x == PA.x and PA.y == PB.y:
                    player_attack(PA, PB)
                    PB.y -= S
                elif PC.x == PB.x and PC.y == PB.y:
                    PB.y -= S
                    Queue = 1
                elif str(PB.x) + "," + str(PB.y) in block:
                    PB.y -= S
                    Queue = 1
            elif PB.x + S <= mouse_pos[0] <= PB.x + S * 2 and PB.y + S <= mouse_pos[1] <= PB.y + 2 * S and PB.y < 701 - S * 2 and PB.x < 800 - S:
                PB.y += S
                PB.x += S
                Queue = 0
                if PB.x == PA.x and PB.y == PA.y:
                    # PA.hp = player_attack(PA, PB)
                    Queue = 1
                    PB.y -= S
                    PB.x -= S
                elif PC.x == PB.x and PC.y == PB.y:
                    PB.y -= S
                    PB.x -= S
                    Queue = 1
                elif str(PB.x) + "," + str(PB.y) in block:
                    PB.y -= S
                    PB.x -= S
                    Queue = 1
            elif PB.x + S <= mouse_pos[0] <= PB.x + S * 2 and PB.y - S <= mouse_pos[1] <= PB.y and PB.y > 0 and PB.x < 800 - S:
                PB.y -= S
                PB.x += S
                Queue = 0
                if PB.x == PA.x and PB.y == PA.y:
                    Queue = 1
                    PB.y += S
                    PB.x -= S
                elif PC.x == PB.x and PC.y == PB.y:
                    PB.y += S
                    PB.x -= S
                    Queue = 1
                elif str(PB.x) + "," + str(PB.y) in block:
                    PB.y += S
                    PB.x -= S
                    Queue = 1
            elif PB.x - S <= mouse_pos[0] <= PB.x and PB.y + S <= mouse_pos[1] <= PB.y + 2 * S and PB.y < 701 - S * 2 and PB.x > 0:
                PB.y += S
                PB.x -= S
                Queue = 0
                if PB.x == PA.x and PB.y == PA.y:
                    # PA.hp = player_attack(PA, PB)
                    Queue = 1
                    PB.y -= S
                    PB.x += S
                elif PC.x == PB.x and PC.y == PB.y:
                    PB.y -= S
                    PB.x += S
                    Queue = 1
                elif str(PB.x) + "," + str(PB.y) in block:
                    PB.y -= S
                    PB.x += S
                    Queue = 1
            elif PB.x - S <= mouse_pos[0] <= PB.x and PB.y - S <= mouse_pos[1] <= PB.y and PB.y > 0 and PB.x > 0:
                PB.y -= S
                PB.x -= S
                Queue = 0
                if PB.x == PA.x and PB.y == PA.y:
                    # PA.hp = player_attack(PA, PB)
                    Queue = 1
                    PB.y += S
                    PB.x += S
                elif PC.x == PB.x and PC.y == PB.y:
                    PB.y += S
                    PB.x += S
                    Queue = 1
                elif str(PB.x) + "," + str(PB.y) in block:
                    PB.y += S
                    PB.x += S
                    Queue = 1

        elif Queue == 0:
            if PA.x - S <= mouse_pos[0] <= PA.x and PA.y <= mouse_pos[1] <= PA.y + S and PA.x > 0:
                PA.x -= S
                Queue = -1
                if PB.x == PA.x and PB.y == PA.y:
                    player_attack(PB, PA)
                    PA.x += S
                elif PC.x == PA.x and PC.y == PA.y:
                    PA.x += S
                    Queue = 0
                elif str(PA.x) + "," + str(PA.y) in block:
                    PA.x += S
                    Queue = 0
            elif PA.x + S <= mouse_pos[0] <= PA.x + 2 * S and PA.y <= mouse_pos[1] <= PA.y + S and PA.x < 800 - S:
                PA.x += S
                Queue = -1
                if PB.x == PA.x and PB.y == PA.y:
                    player_attack(PB, PA)
                    PA.x -= S
                elif PC.x == PA.x and PC.y == PA.y:
                    PA.x -= S
                    Queue = 0
                elif str(PA.x) + "," + str(PA.y) in block:
                    PA.x -= S
                    Queue = 0
            elif PA.x <= mouse_pos[0] <= PA.x + S and PA.y - S <= mouse_pos[1] <= PA.y and PA.y > 0:
                PA.y -= S
                Queue = -1
                if PB.x == PA.x and PB.y == PA.y:
                    player_attack(PB, PA)
                    PA.y += S
                elif PC.x == PA.x and PC.y == PA.y:
                    PA.y += S
                    Queue = 0
                elif str(PA.x) + "," + str(PA.y) in block:
                    PA.y += S
                    Queue = 0
            elif PA.x <= mouse_pos[0] <= PA.x + S and PA.y + S <= mouse_pos[1] <= PA.y + 2 * S and PA.y < 701 - S * 2:
                PA.y += S
                Queue = -1
                if PB.x == PA.x and PB.y == PA.y:
                    player_attack(PB, PA)
                    PA.y -= S
                elif PC.x == PA.x and PC.y == PA.y:
                    PA.y -= S
                    Queue = 0
                elif str(PA.x) + "," + str(PA.y) in block:
                    PA.y -= S
                    Queue = 0
            elif PA.x + S <= mouse_pos[0] <= PA.x + 2 * S and PA.y + S <= mouse_pos[1] <= PA.y + 2 * S and PA.y < 701 - S * 2 and PA.x < 800 - S:
                PA.y += S
                PA.x += S
                Queue = -1
                if PB.x == PA.x and PB.y == PA.y:
                    player_attack(PB, PA)
                    PA.y -= S
                    PA.x -= S
                elif PC.x == PA.x and PC.y == PA.y:
                    PA.y -= S
                    PA.x -= S
                    Queue = 0
                elif str(PA.x) + "," + str(PA.y) in block:
                    PA.y -= S
                    PA.x -= S
                    Queue = 0
            elif PA.x - S <= mouse_pos[0] <= PA.x and PA.y - S <= mouse_pos[1] <= PA.y and PA.y > 0 and PA.x > 0:
                PA.y -= S
                PA.x -= S
                Queue = -1
                if PB.x == PA.x and PB.y == PA.y:
                    player_attack(PB, PA)
                    PA.y += S
                    PA.x += S
                elif PC.x == PA.x and PC.y == PA.y:
                    PA.y += S
                    PA.x += S
                    Queue = 0
                elif str(PA.x) + "," + str(PA.y) in block:
                    PA.y += S
                    PA.x += S
                    Queue = 0
            elif PA.x + S <= mouse_pos[0] <= PA.x + 2 * S and PA.y - S <= mouse_pos[1] <= PA.y and PA.y > 0 and PA.x < 800 - S:
                PA.y -= S
                PA.x += S
                Queue = -1
                if PB.x == PA.x and PB.y == PA.y:
                    player_attack(PB, PA)
                    PA.y += S
                    PA.x -= S
                elif PC.x == PA.x and PC.y == PA.y:
                    PA.y += S
                    PA.x -= S
                    Queue = 0
                elif str(PA.x) + "," + str(PA.y) in block:
                    PA.y += S
                    PA.x -= S
                    Queue = 0
            elif PA.x - S <= mouse_pos[0] <= PA.x and PA.y + S <= mouse_pos[1] <= PA.y + 2 * S and PA.y < 701 - S * 2 and PA.x > 0:
                PA.y += S
                PA.x -= S
                Queue = -1
                if PB.x == PA.x and PB.y == PA.y:
                    player_attack(PB, PA)
                    PA.y -= S
                    PA.x += S
                elif PC.x == PA.x and PC.y == PA.y:
                    PA.y -= S
                    PA.x += S
                    Queue = 0
                elif str(PA.x) + "," + str(PA.y) in block:
                    PA.y -= S
                    PA.x += S
                    Queue = 0

        elif Queue == -1:
            recent_block = PC.x, PC.y
            if PC.x - S <= mouse_pos[0] <= PC.x and PC.y <= mouse_pos[1] <= PC.y + S and PC.x > 0:
                PC.x -= S
                Queue = 1
                if PC.x == PA.x and PC.y == PA.y or PB.x == PC.x and PB.y == PC.y:
                    PC.x += S
                    Queue = -1
            elif PC.x + S <= mouse_pos[0] <= PC.x + 2 * S and PC.y <= mouse_pos[1] <= PC.y + S and PC.x < 800 - S:
                PC.x += S
                Queue = 1
                if PC.x == PA.x and PC.y == PA.y or PB.x == PC.x and PB.y == PC.y:
                    PC.x -= S
                    Queue = -1
            elif PC.x <= mouse_pos[0] <= PC.x + S and PC.y - S <= mouse_pos[1] <= PC.y and PC.y > 0:
                PC.y -= S
                Queue = 1
                if PC.x == PA.x and PC.y == PA.y or PB.x == PC.x and PB.y == PC.y:
                    PC.y += S
                    Queue = -1
            elif PC.x <= mouse_pos[0] <= PC.x + S and PC.y + S <= mouse_pos[1] <= PC.y + 2 * S and PC.y < 701 - S * 2:
                PC.y += S
                Queue = 1
                if PC.x == PA.x and PC.y == PA.y or PB.x == PC.x and PB.y == PC.y:
                    PC.y -= S
                    Queue = -1
            elif PC.x + S <= mouse_pos[0] <= PC.x + 2 * S and PC.y + S <= mouse_pos[1] <= PC.y + 2 * S and PC.y < 701 - S * 2 and PC.x < 800 - S:
                PC.y += S
                PC.x += S
                Queue = 1
                if PC.x == PA.x and PC.y == PA.y or PB.x == PC.x and PB.y == PC.y:
                    PC.y -= S
                    PC.x -= S
                    Queue = -1
            elif PC.x - S <= mouse_pos[0] <= PC.x and PC.y - S <= mouse_pos[1] <= PC.y and PC.y > 0 and PC.x > 0:
                PC.y -= S
                PC.x -= S
                Queue = 1
                if PC.x == PA.x and PC.y == PA.y or PB.x == PC.x and PB.y == PC.y:
                    PC.y += S
                    PC.x += S
                    Queue = -1
            elif PC.x + S <= mouse_pos[0] <= PC.x + 2 * S and PC.y - S <= mouse_pos[1] <= PC.y and PC.y > 0 and PC.x < 800 - S:
                PC.y -= S
                PC.x += S
                Queue = 1
                if PC.x == PA.x and PC.y == PA.y or PB.x == PC.x and PB.y == PC.y:
                    PC.y += S
                    PC.x -= S
                    Queue = -1
            elif PC.x - S <= mouse_pos[0] <= PC.x and PC.y + S <= mouse_pos[1] <= PC.y + 2 * S and PC.y < 701 - S * 2 and PC.x > 0:
                PC.y += S
                PC.x -= S
                Queue = 1
                if PC.x == PA.x and PC.y == PA.y or PB.x == PC.x and PB.y == PC.y:
                    PC.y -= S
                    PC.x += S
                    Queue = -1
            if recent_block != (PC.x, PC.y):
                block.add(str(recent_block[0]) + "," + str(recent_block[1]))

        P = mouse_pos, PA.x, PA.y, PB.x, PB.y, PC.x, PC.y
        return P


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
            Start = False
            Queue = 1
            threexy = set()
            while len(threexy) != 3:
                threexy.add(str(random.randint(0, 7)) + str(random.randint(0, 6)))
            threexy = list(threexy)
            PA.x = int(threexy[0][0]) * 100
            PB.x = int(threexy[1][0]) * 100
            PC.x = int(threexy[2][0]) * 100
            PA.y = int(threexy[0][1]) * 100
            PB.y = int(threexy[1][1]) * 100
            PC.y = int(threexy[2][1]) * 100
            block = set()
        P = Players(mouse_pos, PA, PB, PC)
        key = None
        mouse_pos = None
        if Queue == 0:  # PA
            pygame.draw.rect(Screen, MoveColor, ((PA.x - S, PA.y - S), (S + 1, S + 1)))
            pygame.draw.rect(Screen, MoveColor, ((PA.x - S, PA.y + S), (S + 1, S + 1)))
            pygame.draw.rect(Screen, MoveColor, ((PA.x + S, PA.y - S), (S + 1, S + 1)))
            pygame.draw.rect(Screen, MoveColor, ((PA.x + S, PA.y + S), (S + 1, S + 1)))
            pygame.draw.rect(Screen, MoveColor, ((PA.x + S, PA.y), (S + 1, S + 1)))
            pygame.draw.rect(Screen, MoveColor, ((PA.x - S, PA.y), (S + 1, S + 1)))
            pygame.draw.rect(Screen, MoveColor, ((PA.x, PA.y - S), (S + 1, S + 1)))
            pygame.draw.rect(Screen, MoveColor, ((PA.x, PA.y + S), (S + 1, S + 1)))

        elif Queue == 1:  # PB
            pygame.draw.rect(Screen, MoveColor, ((PB.x - S, PB.y - S), (S + 1, S + 1)))
            pygame.draw.rect(Screen, MoveColor, ((PB.x - S, PB.y + S), (S + 1, S + 1)))
            pygame.draw.rect(Screen, MoveColor, ((PB.x + S, PB.y - S), (S + 1, S + 1)))
            pygame.draw.rect(Screen, MoveColor, ((PB.x + S, PB.y + S), (S + 1, S + 1)))
            pygame.draw.rect(Screen, MoveColor, ((PB.x + S, PB.y), (S + 1, S + 1)))
            pygame.draw.rect(Screen, MoveColor, ((PB.x - S, PB.y), (S + 1, S + 1)))
            pygame.draw.rect(Screen, MoveColor, ((PB.x, PB.y - S), (S + 1, S + 1)))
            pygame.draw.rect(Screen, MoveColor, ((PB.x, PB.y + S), (S + 1, S + 1)))

        if PC.hp < 0:
            for cell in block:
                pygame.draw.rect(Screen, BlockColor, ((int(cell.split(",")[0]), int((cell.split(",")[1]))), (S + 1, S + 1)))
            pygame.draw.rect(Screen, Blue, ((PC.x, PC.y), (S + 1, S + 1)))
        if Queue == -1:  # PC
            pygame.draw.rect(Screen, MoveColor, ((PC.x - S, PC.y - S), (S + 1, S + 1)))
            pygame.draw.rect(Screen, MoveColor, ((PC.x - S, PC.y + S), (S + 1, S + 1)))
            pygame.draw.rect(Screen, MoveColor, ((PC.x + S, PC.y - S), (S + 1, S + 1)))
            pygame.draw.rect(Screen, MoveColor, ((PC.x + S, PC.y + S), (S + 1, S + 1)))
            pygame.draw.rect(Screen, MoveColor, ((PC.x + S, PC.y), (S + 1, S + 1)))
            pygame.draw.rect(Screen, MoveColor, ((PC.x - S, PC.y), (S + 1, S + 1)))
            pygame.draw.rect(Screen, MoveColor, ((PC.x, PC.y - S), (S + 1, S + 1)))
            pygame.draw.rect(Screen, MoveColor, ((PC.x, PC.y + S), (S + 1, S + 1)))
        if PA.hp > 0 and PB.hp > 0:
            defHpA = PA.hp
            pygame.draw.rect(Screen, Red, ((PA.x, PA.y), (S + 1, S + 1)))
            defHpB = PB.hp
            pygame.draw.rect(Screen, Green, ((PB.x, PB.y), (S + 1, S + 1)))
            pygame.draw.rect(Screen, HPbarColor, ((PA.x, PA.y + 6), (defHpA, 20)))
            pygame.draw.rect(Screen, HPbarColor, ((PB.x, PB.y + 6), (defHpB, 20)))
            pygame.draw.rect(Screen, PCNameBackColor, ((PC.x, PC.y + 6), (100, 20)))
        pygame.draw.rect(Screen, BackgroundColor, ((0, 700), (800, 100)))
        draw_map()
        Draw_text()
        if PA.hp == 0 or PB.hp == 0:
            Game = False

    if not Game:
        threexy = set()
        while len(threexy) != 3:
            threexy.add(str(random.randint(0, 7)) + str(random.randint(0, 6)))
        threexy = list(threexy)
        PA.x = int(threexy[0][0]) * 100
        PB.x = int(threexy[1][0]) * 100
        PC.x = int(threexy[2][0]) * 100
        PA.y = int(threexy[0][1]) * 100
        PB.y = int(threexy[1][1]) * 100
        PC.y = int(threexy[2][1]) * 100

        PA.hp = 100
        PB.hp = 100
        PC.hp = -1

        Game = True
        Start = True

    pygame.display.update()
