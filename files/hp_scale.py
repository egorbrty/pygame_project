from functions import *


class Scale:
    """Шкала здоровья главного персонажа в верхнем правом углу"""

    def __init__(self, target):
        self.target = target
        self.value = self.target.start_hp
        self.last_value = self.value

        self.width = 500
        self.height = 30
        self.pos = (width - self.width - 100, 40)  # Верхняя правая точка

    def update(self, screen):
        pygame.draw.polygon(screen, (50, 50, 50),
                            ((self.pos[0], self.pos[1]),
                            (self.pos[0] + self.width, self.pos[1]),
                            (self.pos[0] + self.width - 10, self.pos[1] + self.height),
                            (self.pos[0] - 10, self.pos[1] + self.height)),
                            0)

        self.value -= (self.value - self.width * self.target.hp / self.target.start_hp) * 0.05
        if self.value > 0:
            pygame.draw.polygon(screen, (200, 200, 200),
                                ((self.pos[0], self.pos[1] - 2),
                                 (self.pos[0] + self.value, self.pos[1] - 2),
                                 (self.pos[0] - 10 + self.value, self.pos[1] + self.height + 2),
                                 (self.pos[0] - 10, self.pos[1] + self.height + 2)),
                                0)

        if self.target.hp > 0:
            green = 255 / self.target.start_hp * self.target.hp
            red = 255 - green
            color = (red, green, 0)  # Цвет шкалы здоровья
            value = self.width * self.target.hp / self.target.start_hp
            pygame.draw.polygon(screen, color,
                                ((self.pos[0], self.pos[1] - 2),
                                (self.pos[0] + value, self.pos[1] - 2),
                                (self.pos[0] - 10 + value, self.pos[1] + self.height + 2),
                                (self.pos[0] - 10, self.pos[1] + self.height + 2)),
                                0)
            self.last_value = value


    def replay(self):
        self.value = self.target.start_hp
        self.last_value = self.value


