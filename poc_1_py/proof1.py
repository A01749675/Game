import pygame, sys

from pygame.locals import *
pygame.init()

clock = pygame.time.Clock()

pygame.display.set_caption('Game')

WINDOW_SIZE = (1280, 720)

screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)

display = pygame.surface((300, 300))
unit1_image = pygame.image.load('player.png').convert()
unit1_image.set_colorkey(0, 0, 0)
grass_image = pygame.image.load('grass.png').convert()
TILE_SIZE = grass_image.get_height()
dirt_image = pygame.image.load('dirt.png').convert()
dirt_image.set_colorkey(0, 0, 0)

background_object = [[0.25, [120, 10, 70, 400]], [0.25, [280, 30, 40, 400]], [0.5, [30, 40, 40, 400]], [0.5, [130, 90, 100, 400]], [0.5, [300, 80, 120, 400]]]

def load_map(path):
    f = open(path + '.txt', 'r')
    data = f.read()
    f.close()
    data = data.split('\n')
    game_map = []
    for row in data:
        game_map.append(list(row))
    return game_map

game_map = load_map('map')



while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()