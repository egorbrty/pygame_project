from functions import *


class Decoration(pygame.sprite.Sprite):
    sizes = (SIZE_OF_BLOCK // 2, SIZE_OF_BLOCK // 2)

    def __init__(self, group, x_position, y_position, path):
        super().__init__(group)
        self.image = load_image(path, -1)
        self.image = pygame.transform.scale(self.image, self.sizes)

        self.x_position = x_position
        self.y_position = y_position

        self.rect = self.image.get_rect()
        self.rect.x = x_position * SIZE_OF_BLOCK + SIZE_OF_BLOCK * 0.25
        self.rect.y = y_position * SIZE_OF_BLOCK + SIZE_OF_BLOCK * 0.5

    def update(self, camera):
        print(self.rect)
        camera.move_camera(self)

    def replay(self, *args):
        self.rect.x = self.x_position * SIZE_OF_BLOCK + SIZE_OF_BLOCK * 0.25
        self.rect.y = self.y_position * SIZE_OF_BLOCK + SIZE_OF_BLOCK * 0.5
