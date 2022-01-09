from functions import *


pygame.init()
screen = pygame.display.set_mode(size)


class Stone(pygame.sprite.Sprite):
    sizes = (SIZE_OF_BLOCK, SIZE_OF_BLOCK)

    image1 = load_image(r"data\pictures\textures\stone\stone.png", -1)
    image2 = load_image(r"data\pictures\textures\stone\stone2.png", -1)

    start_size = image1.get_height()
    koeff = SIZE_OF_BLOCK / start_size

    image1 = pygame.transform.scale(image1, sizes)
    sizes = (image2.get_height() * koeff,) * 2
    image2 = pygame.transform.scale(image2, sizes)

    def __init__(self, group, x_position, y_position):
        super().__init__(group)
        self.image = Stone.image1

        self.x_position = x_position
        self.y_position = y_position

        self.rect = self.image.get_rect()
        self.rect.x = x_position * SIZE_OF_BLOCK
        self.rect.y = y_position * SIZE_OF_BLOCK

        self.shaking = 0

    def update(self, camera):
        if self.shaking:
            self.shaking += 100 / fps
            if int(self.shaking) % 2:
                self.image = self.image1
            else:
                self.image = self.image2
        else:
            self.rect.x = self.x_position * SIZE_OF_BLOCK
            self.rect.y = self.y_position * SIZE_OF_BLOCK
        if self.shaking > 50:
            self.shaking = 0

        camera.move_camera(self)

    def replay(self, *args):
        self.rect.x = self.x_position * SIZE_OF_BLOCK
        self.rect.y = self.y_position * SIZE_OF_BLOCK
        self.shaking = 0

    def get_speed(self, speed, maximum_speed, left):
        return speed

    def shot(self):
        self.shaking = 1


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

    def replay(self, *args):
        self.rect.x = self.x_position * SIZE_OF_BLOCK
        self.rect.y = self.y_position * SIZE_OF_BLOCK

    def get_speed(self, speed, maximum_speed, left):
        return speed

    def shot(self):
        pass


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

    def replay(self, *args):
        self.rect.x = self.x_position * SIZE_OF_BLOCK
        self.rect.y = self.y_position * SIZE_OF_BLOCK

    def get_speed(self, speed, maximum_speed, left):
        return round(speed * 0.75)

    def shot(self):
        pass

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

    def replay(self, *args):
        self.rect.x = self.x_position * SIZE_OF_BLOCK
        self.rect.y = self.y_position * SIZE_OF_BLOCK

    def get_speed(self, speed, maximum_speed, left):
        if abs(speed) == maximum_speed:
            return speed
        if left:
            return -maximum_speed // 2
        else:
            return maximum_speed // 2

    def shot(self):
        pass

class BreakingWall(pygame.sprite.Sprite):
    sizes = (SIZE_OF_BLOCK, SIZE_OF_BLOCK)

    images = []

    for i in range(9):
        image = load_image(f"data/pictures/textures/wall/wall{i + 1}.png", None)
        image_rect = image.get_rect()

        image = pygame.transform.scale(image, sizes)

        images.append(image)

    def __init__(self, group, x_position, y_position):
        super().__init__(group)
        self.image = BreakingWall.images[0]

        self.x_position = x_position
        self.y_position = y_position

        self.rect = self.image.get_rect()
        self.rect.x = x_position * SIZE_OF_BLOCK
        self.rect.y = y_position * SIZE_OF_BLOCK

        self.breaking = False
        self.process = 0

    def update(self, camera):
        if self.breaking:
            self.image = self.images[int(self.process)]
            self.process += 30 / fps

            if int(self.process) == len(self.images):
                self.kill()

        camera.move_camera(self)

    def replay(self, *args):
        self.rect.x = self.x_position * SIZE_OF_BLOCK
        self.rect.y = self.y_position * SIZE_OF_BLOCK

        args[0].add(self)
        self.breaking = False
        self.process = 0
        self.image = BreakingWall.images[0]

    def get_speed(self, speed, maximum_speed, left):
        return speed

    def shot(self):
        self.breaking = True

# Zero
class Platform(pygame.sprite.Sprite):
    sizes = (SIZE_OF_BLOCK, SIZE_OF_BLOCK * 0.1)

    image = load_image(f"data/pictures/textures/platform.png", None)
    image_rect = image.get_rect()

    image = pygame.transform.scale(image, sizes)


    def __init__(self, group, x_position, y_position):
        super().__init__(group)
        self.image = Platform.image

        self.x_position = x_position
        self.y_position = y_position

        self.rect = self.image.get_rect()
        self.rect.x = x_position * SIZE_OF_BLOCK
        self.rect.y = y_position * SIZE_OF_BLOCK + SIZE_OF_BLOCK * 0.45

    def update(self, camera):
        camera.move_camera(self)

    def replay(self, *args):
        self.rect.x = self.x_position * SIZE_OF_BLOCK
        self.rect.y = self.y_position * SIZE_OF_BLOCK + SIZE_OF_BLOCK * 0.45

    def get_speed(self, speed, maximum_speed, left):
        return speed

    def shot(self):
        pass
