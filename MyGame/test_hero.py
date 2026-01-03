from symtable import Class

import pygame

from main import sprite_image, sprite_rect

pygame.init()

width = 800
height = 800
clock = pygame.time.Clock()
fps = 60

display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Platformer2")

run = True
while run:
    clock.tick(fps)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
pygame.quit()


bg_image = pygame.image.load("images/bg15.png")
bg_rect = bg_image.get_rect()


clock = pygame.time.Clock()
fps = 60


class Hero:
    def __init__(self):
        self.image = pygame.image.load("images/player1.png")
        self.image = pygame.transform.scale(self.image, (35, 70))
        self.rect = self.image.get_rect()
    def update(self):
        display.blit(self.image, self.rect)

hero = Hero()