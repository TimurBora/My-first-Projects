import pygame as pg
import random
import math

WIDTH = 600
HEIGHT = 600

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

size_player = [10, 100]
size_ball = [20, 20]
CENTER = [WIDTH / 2, HEIGHT / 2]

pg.init()
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('GAME')
clock = pg.time.Clock()
FPS = 30

class Player1(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((size_player))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.left = 25
        self.rect.centery = HEIGHT / 2 
        self.speedy = 0
        self.score = 0
        
    def update(self):
        self.speedy = 0
        keystate = pg.key.get_pressed()
        if keystate[pg.K_w]:
            self.speedy = -15
        elif keystate[pg.K_s]:
            self.speedy = 15
        self.rect.y += self.speedy
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT


class Player2(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((size_player))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.left = WIDTH - 25
        self.rect.centery = WIDTH / 2
        self.speedy = 0
        self.score = 0

    def update(self):
        self.speedy = 0
        keystate = pg.key.get_pressed()
        if keystate[pg.K_UP]:
            self.speedy = -15
        elif keystate[pg.K_DOWN]:
            self.speedy = 15
        self.rect.y += self.speedy
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        

class Ball(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface(size_ball)
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH / 2
        self.rect.y = HEIGHT / 2
        self.speed_hard = 5
        self.speedx = random.choice([-self.speed_hard, self.speed_hard])
        self.speedy = random.randrange(-self.speed_hard, self.speed_hard)

    def update(self):
        self.bounce()
        self.rect.x += self.speedx
        self.rect.y += self.speedy

    def bounce(self):
        if self.rect.top < 0:
            self.speed_hard += 0.5
            self.speedy = self.speed_hard
        if self.rect.bottom > HEIGHT:
            self.speed_hard += 0.5
            self.speedy = -self.speed_hard


player1 = Player1()
player2 = Player2()
ball = Ball()
balls = pg.sprite.Group()
balls.add(ball)
all_sprites = pg.sprite.Group()
all_sprites.add(ball)
all_sprites.add(player1)
all_sprites.add(player2)


def check_win():
    global ball
    if ball.rect.right > WIDTH:
        player1.score += 1
        ball = Ball()
        all_sprites.add(ball)
        balls.add(ball)
    if ball.rect.left < 0:
        player2.score += 1
        ball = Ball()
        all_sprites.add(ball)
        balls.add(ball)


def draw_text(surf, text, size, x, y):
    font = pg.font.SysFont('arial', size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)
    

run = True
while run:
    clock.tick(FPS)
    text_score = f'{player1.score} : {player2.score}'
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
            
    check_win()
    hit = pg.sprite.spritecollide(player1, balls, False)
    if hit:
        ball.speed_hard += 0.5
        ball.speedx = ball.speed_hard
        ball.speedy = random.choice([-ball.speed_hard + random.randrange(-5, 0), ball.speed_hard + random.randrange(0, 5)])
    hit = pg.sprite.spritecollide(player2, balls, False)
    if hit:
        ball.speed_hard += 0.5
        ball.speedx = -ball.speed_hard
        ball.speedy = random.choice([-ball.speed_hard + random.randrange(-5, 0), ball.speed_hard + random.randrange(0, 5)])

    all_sprites.update()
    screen.fill(BLACK)
    all_sprites.draw(screen)
    draw_text(screen, text_score, 50, WIDTH / 2, 10)
    
    pg.display.flip()
        
pg.quit()


















        
        
