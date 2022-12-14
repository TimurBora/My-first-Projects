import pygame as pg
import random

WIDTH = 600
HEIGHT = 600
FPS = 60

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()

all_sprites = pg.sprite.Group()
balls = pg.sprite.Group()
platforms = pg.sprite.Group()

class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((100, 20))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.bottom = 550
        self.rect.centerx = WIDTH / 2
        self.speedx = 0

    def update(self):
        keystate = pg.key.get_pressed()
        self.rect.centerx += self.speedx
        self.speedx = 0
        if keystate[pg.K_LEFT]:
            self.speedx = -15
        if keystate[pg.K_RIGHT]:
            self.speedx = 15
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH


class Ball(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((20, 20))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * 0.85 / 2)
        pg.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.centerx = WIDTH / 2
        self.rect.centery = HEIGHT / 2 + 100
        self.speedx = random.choice([-3, 3])
        self.speedy = 3
        self.random = random.randint(0, 2)
        self.ball_showup = random.choice([0, 0, 1])

    def update(self):
        self.bounce()
        self.ball_showup = random.choice([0, 0, 1])
        self.collision()
        self.rect.centerx += self.speedx
        self.rect.centery += self.speedy

    def bounce(self):
        if self.rect.left < 0:
            self.random = random.randint(0, 2)
            self.speedx = 3 + self.random
        if self.rect.right > WIDTH:
            self.random = random.randint(0, 2)
            self.speedx = -3 - self.random
        if self.rect.top < 0:
            self.random = random.randint(0, 2)
            self.speedy = 3 + self.random
        if self.rect.bottom > HEIGHT:
            self.kill()

    def collision(self):
        hits = pg.sprite.collide_rect(player, self)
        if hits:
            self.speedy = -3
        hits = pg.sprite.groupcollide(balls, platforms, False, True)
        for hit in hits:
            hit.speedy = -hit.speedy
            if hit.ball_showup:
                ball = Ball()
                all_sprites.add(ball)
                balls.add(ball)
                hit.ball_showup = random.choice([0, 0, 1])
            platform.kill()
                


class Platform(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((50, 20))
        self.image.fill(random.choice([WHITE, GREEN, BLUE, RED]))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y

            
player = Player()
ball = Ball()
all_sprites.add(player)
all_sprites.add(ball)
balls.add(ball)

run = True
centerx = 100
centery = 100
platform_num = 0
while run:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    for i in range(1):
        if platform_num >= 80:
            break
        else:
            if centerx + 100 >= WIDTH:
                centerx = 100
                centery += 25
            platform = Platform(centerx, centery)
            platforms.add(platform)
            all_sprites.add(platform)
            centerx += 55
            platform_num += 1

    if len(platforms) == 0:
        platform_num = 0
        centerx = 100
        centery = 100
    


    all_sprites.update()
    screen.fill(BLACK)
    all_sprites.draw(screen)    
    pg.display.flip()
    
pg.quit()
