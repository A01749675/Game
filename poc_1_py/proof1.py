import pygame, sys

from pygame.locals import *
pygame.init()

clock = pygame.time.Clock()

pygame.display.set_caption('Game')

WINDOW_SIZE = (1280, 720)

screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)

display = pygame.surface((300, 300))



while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()