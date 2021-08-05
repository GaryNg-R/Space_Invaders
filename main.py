import pygame
import random
import os

FPS = 60
WHITE = (255, 255, 255)
WIDTH = 500
HEIGHT = 600

#init and windeos
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

running = True

# loop
while running:
    clock.tick(FPS)
    # get input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # update game

    # display game
    screen.fill(WHITE)
    pygame.display.update()

pygame.quit()
