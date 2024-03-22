import pygame as py
import time
import random

py.init()
SCREEN_HEIGHT = 500
SCREEN_WIDTH = 700
GAME_OVER = False
BLUE = (0, 0, 255)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
X1 = SCREEN_WIDTH / 2
Y1 = SCREEN_HEIGHT / 2
X1_change = 0
Y1_change = 0
SNAKE_SPEED = 10
SNAKE_BLOCK = 10
DISPLAY = py.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
py.display.set_caption("Snake game")
clock = py.time.Clock()
font_style = py.font.SysFont("comicsansms", 30)
score_style = py.font.SysFont("bahnschrift", 25)


def Message(msg, color):
    msgs = font_style.render(msg, True, color)
    DISPLAY.blit(msgs, [100, 100])


def draw_snake(snake_block, snake_list):
    for x in snake_list:
        py.draw.rect(DISPLAY, BLUE, [x[0], x[1], snake_block, snake_block])


def Score(score_pass):
    print(score_pass)
    value = score_style.render("Your Score : " + str(score_pass), True, WHITE)
    DISPLAY.blit(value, [0, 0])


def game_loop():
    GAME_OVER = False
    GAME_CLOSE = False
    BLUE = (0, 0, 255)
    RED = (255, 0, 0)
    X1 = SCREEN_WIDTH / 2
    Y1 = SCREEN_HEIGHT / 2
    X1_change = 0
    Y1_change = 0

    SNAKE_LIST = []
    Length_of_snake = 1

    food_x = round(random.randrange(0, SCREEN_WIDTH - SNAKE_BLOCK) / 10.0) * 10.0
    food_y = round(random.randrange(0, SCREEN_HEIGHT - SNAKE_BLOCK) / 10.0) * 10.0

    while not GAME_OVER:
        while GAME_CLOSE == True:
            DISPLAY.fill(BLUE)
            Message("Press Q for Quit! Press R for Restart!", RED)
            py.display.update()
            for event in py.event.get():
                if event.type == py.KEYDOWN:
                    if event.key == py.K_q:
                        GAME_OVER = True
                        GAME_CLOSE = False
                        py.quit()
                    if event.key == py.K_r:
                        game_loop()

        for event in py.event.get():
            print(event)
            if event.type == py.QUIT:
                GAME_OVER = True
            elif event.type == py.KEYDOWN:
                if event.key == py.K_LEFT:
                    X1_change = -SNAKE_BLOCK
                    Y1_change = 0
                elif event.key == py.K_RIGHT:
                    X1_change = SNAKE_BLOCK
                    Y1_change = 0
                elif event.key == py.K_UP:
                    X1_change = 0
                    Y1_change = -SNAKE_BLOCK
                elif event.key == py.K_DOWN:
                    X1_change = 0
                    Y1_change = SNAKE_BLOCK

        X1 += X1_change
        Y1 += Y1_change
        if X1 >= SCREEN_WIDTH or X1 <= 0 or Y1 >= SCREEN_HEIGHT or Y1 <= 0:
            GAME_CLOSE = True

        DISPLAY.fill((0, 0, 0))
        py.draw.rect(DISPLAY, BLUE, [X1, Y1, SNAKE_BLOCK, SNAKE_BLOCK])
        py.draw.rect(DISPLAY, RED, [food_x, food_y, SNAKE_BLOCK, SNAKE_BLOCK])
        SNAKE_HEAD = []
        SNAKE_HEAD.append(X1)
        SNAKE_HEAD.append(Y1)
        SNAKE_LIST.append(SNAKE_HEAD)
        if len(SNAKE_LIST) > Length_of_snake:
            del SNAKE_LIST[0]
        for x in SNAKE_LIST[:-1]:
            if x == SNAKE_HEAD:
                GAME_CLOSE = True
        draw_snake(SNAKE_BLOCK, SNAKE_LIST)
        Score(Length_of_snake - 1)
        py.display.update()
        if X1 == food_x and Y1 == food_y:
            food_x = (
                round(random.randrange(0, SCREEN_WIDTH - SNAKE_BLOCK) / 10.0) * 10.0
            )
            food_y = (
                round(random.randrange(0, SCREEN_HEIGHT - SNAKE_BLOCK) / 10.0) * 10.0
            )
            Length_of_snake += 1

        clock.tick(SNAKE_SPEED)
    py.display.update()
    py.quit()


game_loop()
