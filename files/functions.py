import os
import sys
import pygame


def load_image(name, colorkey=None):
    # если файл не существует, то выходим
    if not os.path.isfile(name):
        print(f"Файл с изображением '{name}' не найден")
        sys.exit()
    image = pygame.image.load(name)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


SIZE_OF_BLOCK = 140
MAIN_HERO_HEIGHT = 100
MAIN_HERO_SPEED = 300

fps = 150
GRAVITY = 2000
JUMP = 1200
size = width, height = 1350, 700
