import pygame.font

from functions import *


class Message(pygame.sprite.Sprite):
    def __init__(self):
        self.messages = []
        self.font = pygame.font.Font(None, 20)

    def add(self, text, color, x, y):
        """Показывает надпись в точке x, y"""
        self.messages.append([text, color, x, y, 0])

    def draw(self, screen, camera):
        for i in self.messages:
            text = self.font.render(i[0], True, i[1])

            i[4] += 1
            i[3] -= 100 / fps

            delta_x, delta_y = camera.get_delta()
            i[2] -= delta_x
            i[3] -= delta_y

            screen.blit(text, (i[2] - text.get_width() // 2, i[3]))

        self.messages = list(filter(lambda s: s[4] < fps, self.messages))

    def replay(self):
        self.messages.clear()