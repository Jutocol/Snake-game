import pygame
import random
pygame.init()

width = 800
height = 600

game_display = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
snake_block = 10
snake_speed = 30

x1 = width / 2
y1 = height / 2

x1_change = 0
y1_change = 0
game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
keys = pygame.key.get_pressed()

if keys[pygame.K_LEFT]:
    x1_change = -snake_block
    y1_change = 0
elif keys[pygame.K_RIGHT]:
    x1_change = snake_block
    y1_change = 0
elif keys[pygame.K_UP]:
    y1_change = -snake_block
    x1_change = 0
elif keys[pygame.K_DOWN]:
    y1_change = snake_block
    x1_change = 0
x1 += x1_change
y1 += y1_change
game_display.fill(black)
pygame.draw.rect(game_display, white, [x1, y1, snake_block, snake_block])
pygame.display.update()
if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
    game_over = True
clock = pygame.time.Clock()
clock.tick(snake_speed)
pygame.quit()
quit()
