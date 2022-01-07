from functions import *
import pygame


pygame.init()
screen = pygame.display.set_mode(size)


class Stone(pygame.sprite.Sprite):
    sizes = (SIZE_OF_BLOCK, SIZE_OF_BLOCK)

    image = load_image(r"data\pictures\textures\stone.png", -1)
    image = pygame.transform.scale(image, sizes)

    def __init__(self, group, x_position, y_position):
        super().__init__(group)
        self.image = Stone.image

        self.x_position = x_position
        self.y_position = y_position

        self.rect = self.image.get_rect()
        self.rect.x = x_position * SIZE_OF_BLOCK
        self.rect.y = y_position * SIZE_OF_BLOCK

    def update(self, camera):
        camera.move_camera(self)

    def replay(self):
        self.rect.x = self.x_position * SIZE_OF_BLOCK
        self.rect.y = self.y_position * SIZE_OF_BLOCK

    def get_speed(self, speed, maximum_speed, left):
        return speed


class Grass(pygame.sprite.Sprite):
    sizes = (SIZE_OF_BLOCK, SIZE_OF_BLOCK)

    image = load_image(r"data\pictures\textures\grass.jpg", -1)
    image = pygame.transform.scale(image, sizes)

    def __init__(self, group, x_position, y_position):
        super().__init__(group)
        self.image = Grass.image

        self.x_position = x_position
        self.y_position = y_position

        self.rect = self.image.get_rect()
        self.rect.x = x_position * SIZE_OF_BLOCK
        self.rect.y = y_position * SIZE_OF_BLOCK

    def update(self, camera):
        camera.move_camera(self)

    def replay(self):
        self.rect.x = self.x_position * SIZE_OF_BLOCK
        self.rect.y = self.y_position * SIZE_OF_BLOCK

    def get_speed(self, speed, maximum_speed, left):
        return speed


class Sand(pygame.sprite.Sprite):
    sizes = (SIZE_OF_BLOCK, SIZE_OF_BLOCK)

    image = load_image(r"data\pictures\textures\sand.jpg", None)
    image = pygame.transform.scale(image, sizes)

    def __init__(self, group, x_position, y_position):
        super().__init__(group)
        self.image = Sand.image

        self.x_position = x_position
        self.y_position = y_position

        self.rect = self.image.get_rect()
        self.rect.x = x_position * SIZE_OF_BLOCK
        self.rect.y = y_position * SIZE_OF_BLOCK

    def update(self, camera):
        camera.move_camera(self)

    def replay(self):
        self.rect.x = self.x_position * SIZE_OF_BLOCK
        self.rect.y = self.y_position * SIZE_OF_BLOCK

    def get_speed(self, speed, maximum_speed, left):
        return round(speed * 0.75)

class Ice(pygame.sprite.Sprite):
    sizes = (SIZE_OF_BLOCK, SIZE_OF_BLOCK)

    image = load_image(r"data\pictures\textures\ice.jpg", None)
    image = pygame.transform.scale(image, sizes)

    def __init__(self, group, x_position, y_position):
        super().__init__(group)
        self.image = Ice.image

        self.x_position = x_position
        self.y_position = y_position

        self.rect = self.image.get_rect()
        self.rect.x = x_position * SIZE_OF_BLOCK
        self.rect.y = y_position * SIZE_OF_BLOCK

    def update(self, camera):
        camera.move_camera(self)

    def replay(self):
        self.rect.x = self.x_position * SIZE_OF_BLOCK
        self.rect.y = self.y_position * SIZE_OF_BLOCK

    def get_speed(self, speed, maximum_speed, left):
        if abs(speed) == maximum_speed:
            return speed
        if left:
            return -maximum_speed // 2
        else:
            return maximum_speed // 2

