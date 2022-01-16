from functions import *



class Pause(pygame.sprite.Sprite):
    mashion_sizes = (40, 40)  # позиция кнопки когда мышь наведена
    sizes = (30, 30)

    image_pause = load_image(f"data/pictures/pause.png", -1)

    def __init__(self, group):
        super().__init__(group)
        self.image = self.image_pause

        self.but_width = 30

        self.rect = self.image.get_rect()
        self.update(False)


    def update(self, mouse_is_on_button):
        if mouse_is_on_button:
            if self.but_width < self.mashion_sizes[0]:
                self.but_width += 1.5

        else:
            if self.but_width > self.sizes[0]:
                self.but_width -= 1.5

        self.rect.width = self.rect.height = self.but_width

        self.image = pygame.transform.scale(self.image_pause, (self.but_width, self.but_width))

        self.rect.x = width // 2 - self.but_width // 2
        self.rect.y = 40 - self.but_width // 2


class Button(pygame.sprite.Sprite):
    mashion_sizes = (width * 0.12, width * 0.12)  # позиция кнопки когда мышь наведена
    sizes = (width * 0.1, width * 0.1)

    def __init__(self, group, path, position):
        super().__init__(group)

        self.but_image = load_image(path, None)

        self.image = self.but_image

        self.but_width = self.sizes[0]

        self.x_position, self.y_position = position

        self.rect = self.image.get_rect()
        self.update((0, 0))

    def update(self, mouse_pos):
        mouse_is_on_button = self.rect.collidepoint(mouse_pos)
        if mouse_is_on_button:
            if self.but_width < self.mashion_sizes[0]:
                self.but_width += 1.5

        else:
            if self.but_width > self.sizes[0]:
                self.but_width -= 1.5

        self.rect.width = self.rect.height = self.but_width

        self.image = pygame.transform.scale(self.but_image, (self.but_width, self.but_width))

        self.rect.x = self.x_position - self.but_width // 2
        self.rect.y = self.y_position - self.but_width // 2

    def reset(self):
        self.but_width = self.sizes[0]

