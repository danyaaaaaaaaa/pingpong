import pygame
import time
import os

pygame.init()

FPS = 30

PATH = os.path.dirname(__file__) + os.sep

win_width = 1000
win_height = 700

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, imageS, width, height, x,y, speed):
        super().__init__()
        self.image = pygame.image.load(imageS)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def show(self):
        wind.blit(self.image, (self.rect.x, self.rect.y))

"""class Raketka1(GameSprite):
    def dvizenie:
        self.rect.x = self.x
        self.rect.y = self.y

        keys = pygame.key.get_pressed()
        if keys [pygame.K_w] == True:
            self.y -= 10
        if keys [pygame.K_w] == True:
            self.y += 10

class Raretka2(GameSprite):
    def dvizenie:
        self.rect.x = self.x
        self.rect.y = self.y
        
        keys = pygame.key.get_pressed()
        if keys [pygame.K_UP] == True:
            self.y -= 10
        if keys [pygame.K_DOWN] == True:
            self.y += 10
"""
class Racket(GameSprite):
    def __init__(self, image, w,h, x,y, speed, keyup, keydown):
        super().__init__(image, w,h, x,y, speed)
        self.keyup = keyup
        self.keydown = keydown

    def move(self):
        keys = pygame.key.get_pressed()
        
        if keys[self.keydown] == True:
            self.rect.y += self.speed
        if keys[self.keyup] == True:
            self.rect.y -= self.speed

class Ball(GameSprite):
    def __init__(self, image, w,h, x,y, speed):
        super().__init__(image, w,h, x,y, speed, )
        self.directionX = 1
        self.directionY = 1
    def move1(self):
        self.rect.x += self.speed * self.directionX
        self.rect.y += self.speed * self.directionY
        if self.rect.y < win_height - 50 or self.rect.y < 0:
            self.directionY *= -1
        if pygame.sprite.collide_rect(self, raketka) or pygame.sprite.collide_rect(self, raketka2):
            self.directionX *= -1


wind = pygame.display.set_mode((win_width, win_height))
back = GameSprite(PATH + 'pukikaki.jpg', win_width, win_height, 0,0, 0)

raketka = Racket(PATH + "raketka.png", 10, 100, 10, 0, 10, pygame.K_w, pygame.K_s)
raketka2 = Racket(PATH + "raketka.png", 10, 100, 980, 0, 10, pygame.K_UP, pygame.K_DOWN)
ball = Ball(PATH + "balllll-removebg-preview.png", 50, 50, 500, 250, 10)



clock = pygame.time.Clock()
game = True

while game == True:
    events = pygame.event.get()
    for e in events:
        if e.type == pygame.QUIT:
            game = False

    back.show()

    raketka.move()
    raketka.show()
    raketka2.move()
    raketka2.show()
    ball.show()
    ball.move1()





    clock.tick(FPS)
    pygame.display.update()