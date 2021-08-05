import pygame
import random
import os


#init and windeos
pygame.init()
screen = pygame.display.set_mode((500, 600))

running = True

# loop
while running:
    # get input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # update game

        # display game
pygame.quit()
