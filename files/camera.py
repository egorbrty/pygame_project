from functions import *
from pygame import Rect


class Camera:
    # зададим начальный сдвиг камеры
    def __init__(self):
        self.x = 0
        self.y = 0

    def update(self, target, level_width, level_height):
        center_x = target.rect.x + SIZE_OF_BLOCK // 2
        center_y = target.rect.y + SIZE_OF_BLOCK // 2

        self.x = width // 2 - center_x
        self.y = height // 2 - center_y

        if self.x > 0:
            self.x = 0
        elif center_x + width // 2 > level_width:
            self.x = width - level_width

        if self.y > 0:
            self.y = 0
        elif self.y < height - level_height:
            self.y = height - level_height

    def move_camera(self, obj):
        obj.rect.x += self.x
        obj.rect.y += self.y

    def move_back(self, obj):
        obj.rect.x -= self.x
        obj.rect.y -= self.y
