import pygame as pg
import random

WIDTH = 1000
HEIGHT = 600
FPS = 1000

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()

all_sprites = pg.sprite.Group()

class Line(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((1, 1))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.speedy = 1
        self.speedx = 1

    def update(self):
        pg.draw.line(self.image, WHITE, self.rect.center, self.rect.center)
        self.rect.centerx += self.speedx
        self.rect.centery += self.speedy
        if self.rect.center[1] > HEIGHT:
            self.speedy = -1
        if self.rect.center[1] < 0:
            self.speedy = 1
        if self.rect.center[0] > WIDTH:
            self.speedx = -1
        if self.rect.center[0] < 0:
            self.speedx = 1


line = Line()
all_sprites.add(line)

run = True
while run:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
            
    all_sprites.update()
    all_sprites.draw(screen)
    
    pg.display.flip()

pg.quit()
