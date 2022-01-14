import os
import sys
import pygame
import random


SIZE_OF_BLOCK = 150

MAIN_HERO_HEIGHT = 100
MAIN_HERO_SPEED = 400

BATTLE_DROID_HEIGHT = 75
BATTLE_DROID_SPEED = 125

fps = 90
GRAVITY = 2000
JUMP = 1150
scale_width = 100

size = width, height = 1350, 700


pygame.init()
pygame.font.init()
pygame.display.set_caption('Space wars')
screen = pygame.display.set_mode(size)


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
    chance = x / y * 10
    x = random.randint(1, 100)
    return x <= chance


def health_scale(screen, target):
    '''Отображает шкалу здоровья цели'''
    if target.is_alive():
        pygame.draw.rect(screen, (100, 100, 100),
                         ((target.rect.x + target.rect.width // 2 - scale_width // 2,
                           target.rect.bottom - target.height - 20),
                          (scale_width, 5)),
                         0)
        green = 255 / target.start_hp * target.hp
        red = 255 - green

        color = (red, green, 0)  # Цвет шкалы здоровья
        pygame.draw.rect(screen, color,
                         ((target.rect.x + target.rect.width // 2 - scale_width // 2,
                           target.rect.bottom - target.height - 20),
                          (scale_width / target.start_hp * target.hp, 5)),
                         0)


