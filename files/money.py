from functions import *


class Money(pygame.sprite.Sprite):
    sizes = (width * 0.04, width * 0.04)
    images = []

    for i in range(10):
        image = load_image(f"data/pictures/coin/coin{i + 1}.png", -1)
        image_rect = image.get_rect()
        image = pygame.transform.scale(image, sizes)

        images.append(image)

    def __init__(self, group, number):
        super().__init__(group)
        self.number = number
        self.font = pygame.font.Font(None, 60)

        self.image = self.images[0]
        self.process = 0

        self.rect = self.image.get_rect()

        self.rect.x = 20
        self.rect.y = 20

        self.value = number

    def __iadd__(self, money):
        self.number += money
        return self

    def update(self, screen):
        if self.value < self.number:
            self.value += 30 / fps

        text = self.font.render(str(int(self.value)), True, (255, 231, 0))

        self.process += 10
        if self.process // fps >= len(self.images):
            self.process = 0
        self.image = self.images[self.process // fps]

        screen.blit(text, (self.rect.x + self.rect.width + 20, self.rect.y + self.rect.height * 0.2))
