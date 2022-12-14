import pygame as pg
import random

WIDTH = 1000
HEIGHT = 600
FPS = 60

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()

all_sprites = pg.sprite.Group()
class Winter(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((10, 10))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.centery = -10
        self.rect.centerx = random.randint(0, WIDTH)
        self.speedy = 3
        self.speedx = random.choice([-4, 4])
        self.timer_change = 0

    def update(self):
        if self.rect.left < 0:
            self.speedx = 4
        if self.rect.right > WIDTH:
            self.speedx = -4
        if self.rect.bottom > HEIGHT:
            self.speedy = 0
            self.speedx = 0
        self.rect.centery += self.speedy
        self.rect.centerx += self.speedx
        self.change()

    def change(self):
        if self.timer_change > 5:
            self.speedx = random.choice([-3, 3])
            self.timer_change = 0
        else:
            self.timer_change += 1

timer_showup = 0
run = True
while run:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    if timer_showup > 15:
        winter = Winter()
        all_sprites.add(winter)
        all_sprites.update()
    else:
        timer_showup += 1
    screen.fill(BLACK)
    all_sprites.draw(screen)
    pg.display.flip()

pg.quit()
