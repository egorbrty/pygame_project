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


def hit(x, y):
    """При ударе в функцию поступает информация о вероятности критического удара врага и броне гравного персонажа.
    Функция на основе генератора псевдослучайнгых чисел определяет, попал ли враг по персонажу. Если True, то функция
    вызывается вновь и определяет, критический удар или нет
    Первый аргумент - меткость или вероятность критического удара
    Второй аргумент - ловкость или броня"""
    return True


SIZE_OF_BLOCK = 150

MAIN_HERO_HEIGHT = 100
MAIN_HERO_SPEED = 400

BATTLE_DROID_HEIGHT = 75
BATTLE_DROID_SPEED = 125

fps = 100
GRAVITY = 2000
JUMP = 1150
size = width, height = 1350, 700
