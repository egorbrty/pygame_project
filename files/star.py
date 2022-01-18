import pygame.sprite

from functions import *


class Star(pygame.sprite.Sprite):
    sizes = (SIZE_OF_BLOCK * 0.2, SIZE_OF_BLOCK * 0.2)

    image = load_image('data/pictures/star.png', -1)
    image = pygame.transform.scale(image, sizes)

    def __init__(self, group, x_position, y_position):
        """Третья звездочка"""
        super().__init__(group)

        self.x_position = x_position
        self.y_position = y_position

        self.rect = self.image.get_rect()
        self.rect.x = x_position * SIZE_OF_BLOCK + SIZE_OF_BLOCK * 0.4
        self.rect.y = y_position * SIZE_OF_BLOCK + SIZE_OF_BLOCK * 0.5

    def update(self, camera):
        camera.move_camera(self)

    def replay(self, *args):
        self.rect.x = self.x_position * SIZE_OF_BLOCK + SIZE_OF_BLOCK * 0.4
        self.rect.y = self.y_position * SIZE_OF_BLOCK + SIZE_OF_BLOCK * 0.5
