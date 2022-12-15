import pygame as pg
import random
import math
import sys

WIDTH = 600
HEIGHT = 600
FPS = 19

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()

def grid():
    x = 0
    y = 0
    for i in range(30):
        pg.draw.line(screen, WHITE, (x, 0), (x, HEIGHT))
        x += 20
        pg.draw.line(screen, WHITE, (0, y), (WIDTH, y))
        y += 20

class Square:
    def __init__(self, x, y, color, width):
        self.x = x
        self.y = y
        self.color = color
        self.width = width

    def draw_it(self):
        pg.draw.rect(screen, self.color, (self.x, self.y, self.width, self.width))

class Snake:
    def __init__(self, length, color):
        self.square = []
        self.length = length
        self.color = color
        self.direction = 'RIGHT'
        x = 0
        y = 0
        for i in range(length):
            self.square.append(Square(x, y, color, 20))
            x -= 20

    def draw_it(self):
        for i in range(len(self.square)):
            self.square[i].draw_it()
            
    def move_it(self):
        for i in range(len(self.square)-1, 0, -1):
            self.square[i].x = self.square[i-1].x
            self.square[i].y = self.square[i-1].y
        match self.direction:
            case 'RIGHT':
                self.square[0].x += 20
            case 'LEFT':
                self.square[0].x -= 20
            case 'UP':
                self.square[0].y -= 20
            case 'DOWN':
                self.square[0].y += 20
        if self.square[0].x > WIDTH:
            self.square[0].x = 20
        if self.square[0].x < 0:
            self.square[0].x = WIDTH - 20
        if self.square[0].y > HEIGHT:
            self.square[0].y = 20
        if self.square[0].y < 0:
            self.square[0].y = HEIGHT - 20

    def check_food(self):
        if self.square[0].x == apple.x and self.square[0].y == apple.y:
            apple_xy()
            self.square.append(Square(-100, -100, GREEN, 20))
            
    def check_die(self):
        for i in range(1, len(self.square), 1):
            if self.square[0].x == self.square[i].x and self.square[0].y == self.square[i].y:
                for j in range(len(self.square)-1, self.length-1, -1):
                    del self.square[j]
                apple_xy()
                break

def apple_xy():
    random_x = random.randint(0, 29)
    random_y = random.randint(0, 29)
    apple.x = random_x * 20
    apple.y = random_y * 20
    for i in range(len(snake.square)):
        if snake.square[i].x == apple.x and snake.square[i].y == apple.y:
            apple_xy()
        

snake = Snake(10, GREEN)    
apple = Square(-100, -100, RED, 20)
apple_xy()

run = True
while run:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RIGHT and not snake.direction == 'LEFT':
                snake.direction = 'RIGHT'
            if event.key == pg.K_LEFT and not snake.direction == 'RIGHT':
                snake.direction = 'LEFT'
            if event.key == pg.K_UP and not snake.direction == 'DOWN':
                snake.direction = 'UP'
            if event.key == pg.K_DOWN and not snake.direction == 'UP':
                snake.direction = 'DOWN'

    snake.move_it()
    snake.check_die()
    snake.check_food()
    snake.draw_it()
    apple.draw_it()
    pg.display.update()
    screen.fill(BLACK)
    grid()
    
sys.exit()
