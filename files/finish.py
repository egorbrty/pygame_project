from functions import *


pygame.init()
screen = pygame.display.set_mode(size)


class Cup(pygame.sprite.Sprite):
    sizes = (SIZE_OF_BLOCK * 0.6, SIZE_OF_BLOCK * 0.6)

    cup_image = load_image(r"data\pictures\finish\cup.png", -1)

    cup_image = pygame.transform.scale(cup_image, sizes)

    def __init__(self, group, x_position, y_position):
        super().__init__(group)
        self.image = Cup.cup_image

        self.x_position = x_position
        self.y_position = y_position

        self.rect = self.image.get_rect()
        self.rect.x = x_position * SIZE_OF_BLOCK + SIZE_OF_BLOCK * 0.2
        self.rect.y = y_position * SIZE_OF_BLOCK + SIZE_OF_BLOCK * 0.4

    def update(self, camera):
        camera.move_camera(self)

    def replay(self, *args):
        self.rect.x = self.x_position * SIZE_OF_BLOCK + SIZE_OF_BLOCK * 0.2
        self.rect.y = self.y_position * SIZE_OF_BLOCK + SIZE_OF_BLOCK * 0.4
