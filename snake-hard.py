# Import
import pygame
from random import randint
# Инициализация PYGAME
pygame.init()
# Settings display
FPS = 5.0
side = 30
WIDTH = 15
HEIGHT = 15
pygame.display.set_caption('Snake (HARD SPEED VERSION)')
# Color RGB
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
# Variables
clock = pygame.time.Clock()
sc = pygame.display.set_mode((WIDTH * side, HEIGHT * side))
sc.fill(GREEN)
pygame.display.update()
score = 0
moving = 'STOP'
game_run = 1
multiplier = 0
run = True
# Player
x = 50
y = 50
dirs = [pygame.K_RIGHT, pygame.K_DOWN, pygame.K_LEFT, pygame.K_UP]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
snake = [(7, 3), (7, 4)]
direction = 0
# Function

# Apple
def place_apple():
    a = (randint(0, WIDTH - 1), randint(0, HEIGHT - 1))
    while a in snake:
        a = (randint(0, WIDTH - 1), randint(0, HEIGHT - 1))
    return a


# Variables function
apple = place_apple()

# Colision snake
def check_collisions():
    head = snake[-1]
    for i in range(len(snake) - 1):
        if head == snake[i]:
            return 2
    if head[0] >= WIDTH or head[0] < 0:
        return 3
    if head[1] >= HEIGHT or head[1] < 0:
        return 3
    if head == apple:
        return 1
    return 0

while run:
    if game_run == 0:
        events = pygame.event.get()
        sc.fill(WHITE)
        print(pygame.font.get_fonts())
        font = pygame.font.SysFont("Calibri", 50)
        text1 = font.render("Game Over!", 2, BLACK)
        text2 = font.render("Ваш счет: " + str(score), 2, BLACK)
        sc.blit(text1, (85, HEIGHT * side / 2 - 120))
        sc.blit(text2, (85, HEIGHT * side / 2))
        pygame.display.update()
        for i in events:
            if i.type == pygame.QUIT:
                run = False
                exit()
    elif game_run == 1:
        events = pygame.event.get()
        for i in events:
            if i.type == pygame.QUIT:
                run = False
                exit()
            if i.type == pygame.KEYDOWN:
                for j in range(4):
                    if i.key == dirs[j] and direction != (j + 2) % 4:
                        direction = j

        snake.append((snake[-1][0] + dx[direction],
                     snake[-1][1] + dy[direction]))

        collision = check_collisions()
        if collision == 1:
            apple = place_apple()
            multiplier += 1
            score += 1 * multiplier
            FPS += 0.5
        elif collision == 2 or collision == 3:
            game_run = 0
        elif collision == 0:
            snake.pop(0)

        sc.fill(GREEN)
        for i in range(len(snake)):
            pygame.draw.rect(sc, BLUE, pygame.Rect(
                snake[i][0] * side, snake[i][1] * side, side, side))
        pygame.draw.rect(sc, RED, pygame.Rect(
            apple[0] * side, apple[1] * side, side, side))
        font = pygame.font.SysFont("Calibri", 35)
        text3 = font.render(str(score), 2, BLACK)
        text4 = font.render("FPS: " + str(FPS), 2, BLACK)
        sc.blit(text3, (0, HEIGHT * side / 2 - 232))
        sc.blit(text4, (160, HEIGHT * side / 2 - 232))
    pygame.display.update()
    clock.tick(FPS)

exit()
