import pygame
import random

# Initialize Pygame
pygame.init()

# Set window dimensions
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

# Snake settings
snake_block = 10
snake_speed = 15
clock = pygame.time.Clock()

font_style = pygame.font.SysFont(None, 30)


def display_score(score):
    value = font_style.render("Score: " + str(score), True, white)
    screen.blit(value, [0, 0])


def draw_snake(snake_block, snake_list):
    for x, y in snake_list:
        pygame.draw.rect(screen, green, [x, y, snake_block, snake_block])


def game_loop():
    game_over = False
    game_close = False

    x1 = screen_width / 2
    y1 = screen_height / 2
    x1_change = 0
    y1_change = 0

    snake_list = []
    snake_length = 1

    food_x = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0
    food_y = round(random.randrange(0, screen_height - snake_block) / 10.0) * 10.0

    while not game_over:
        break


game_loop()
