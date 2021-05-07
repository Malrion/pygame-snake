import pygame as pg
from random import randint

pg.init()
# Dislplay
side = 30
side1 = 30
w = 30
h = 25
FPS = 120
DISPLAYSURF = pg.display.set_mode((w * side, h * side))
# Color
K_BLUE = (21, 32, 229)
WHITE = (255, 255, 255)
YELLOW = (255, 193, 6)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
score = 0
game_running = 0

dirs = [pg.K_RIGHT, pg.K_DOWN, pg.K_LEFT, pg.K_UP]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
snake = [(7, 3), (7, 4)]
direction = 0


def place_apple():
    a = (randint(0, w - 1), randint(0, h - 1))
    while a in snake:
        a = (randint(0, w - 1), randint(0, h - 1))
    return a


apple = place_apple()


def check_collisions(FPS, score):
    head = snake[-1]
    for i in range(len(snake) - 1):
        if head == snake[i]:
            return 2
    if head[0] >= w or head[0] < 0:
        return 3
    if head[1] >= h or head[1] < 0:
        return 3
    if head == apple:
        score += 1
        FPS += FPS*1.5
        return 1
    return 0


clock = pg.time.Clock()
f = pg.font.SysFont('Avenir Heavy', 50, True)
f1 = pg.font.SysFont('Avenir Heavy', 65, True)

run = 1
while run:  # основной цикл игры
    speed_text = f.render("speed: "+str(round(FPS, 2)), 1, WHITE)
    move_text = f.render("move: "+str(direction), 1, WHITE)
    sc_text = f1.render(f"AI's score: {score}", 1, WHITE)
    head = snake[-1]
    clock.tick(FPS)
    for e in pg.event.get():
        if e.type == pg.QUIT:
            run = 0
        if e.type == pg.KEYDOWN:
            if game_running == 0:
                game_running = 1
            if e.key == pg.K_SPACE:  # начало игры
                game_running = 0
                snake = [(7, 3), (7, 4)]
                direction = 0
                apple = place_apple()
                score = 0
                FPS = 30
                pg.display.update()
    # check wall collisions
    if 1:
        if head[0] == w-1:
            direction = 1
        elif head[0] != w - 1 and head[1] < h - 1 and head[0] != 0:
            direction = 0
        if head[1] == h - 1:
            direction = 2
        elif head[0] != w - 1 and head[1] < h - 1 and head[0] != 0:
            direction = 0
        if head[0] == 0:
            direction = 3
        elif head[0] != w - 1 and head[1] < h - 1 and head[0] != 0:
            direction = 0
        if head[1] == 0 and head[0] != w-1:
            direction = 0
        # check apple collision
        if head[0] == apple[0] and apple[1] > head[1]:
            direction = 1
        elif head[0] != w - 1 and head[1] < h - 1 and head[0] != 0:
            direction = 0
    DISPLAYSURF.blit(sc_text, (5, 10))
    pg.display.update()
    if game_running == 2:  # Game over
        DISPLAYSURF.fill(BLACK)
        DISPLAYSURF.blit(f.render("Game over!", 1, BLACK),
                         (3 * side, 3 * side))
        DISPLAYSURF.blit(move_text, (5 * side, 5 * side))
        pg.display.update()
        game_running = 3
    if game_running == 3:
        continue
    snake.append((snake[-1][0] + dx[direction], snake[-1]
                 [1] + dy[direction]))  # переход головы
    coll = check_collisions(FPS, score)
    if coll >= 2:  # обработка столкновений
        game_running = 2
        pass
    elif coll == 1:
        FPS += 4*0.1
        # if FPS>5:
        #    score += round(FPS-4)
        # else:
        score += 1
        DISPLAYSURF.blit(sc_text, (5, 10))
        apple = place_apple()
        pg.display.update()
        pass
    elif coll == 0:
        snake.pop(0)
    DISPLAYSURF.fill(BLACK)
    for i in range(len(snake)):  # Draw snake and apple
        pg.draw.rect(DISPLAYSURF, GREEN, pg.Rect(
            snake[i][0] * side1, snake[i][1] * side1, side1, side1))
    DISPLAYSURF.blit(sc_text, (5, 10))
    pg.draw.rect(DISPLAYSURF, YELLOW, pg.Rect(
        apple[0] * side1, apple[1] * side1, side1, side1))
    DISPLAYSURF.blit(speed_text, (200, 200))
    DISPLAYSURF.blit(move_text, (200, 50))
    pg.display.update()
pg.quit()
