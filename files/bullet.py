from functions import *
import pygame


pygame.init()
screen = pygame.display.set_mode(size)


class Bullet(pygame.sprite.Sprite):
    sizes = (MAIN_HERO_HEIGHT / 3.8, MAIN_HERO_HEIGHT / 13.25)

    image = load_image(r"data\pictures\clone\shoot\bullet.png", -1)
    image = pygame.transform.scale(image, sizes)

    def __init__(self, group, x_position, y_position, hit, crit, left):
        super().__init__(group)
        self.image = Bullet.image

        self.x_position = x_position
        self.y_position = y_position

        self.hit = hit  # Сила удара
        self.crit = crit  # Вероятность критического удара

        self.rect = self.image.get_rect()
        self.rect.x = x_position
        self.rect.y = y_position

        self.left = left

        self.stop = False

    def update(self, camera, textures, persons):
        if self.stop:
            self.kill()
            return

        if self.left:
             self.rect.x -= 1000 / fps
        else:
            self.rect.x += 1000 / fps


        camera.move_camera(self)

        for texture in textures:
            if pygame.sprite.collide_rect(self, texture):
                self.kill()

        for person in persons:
            if pygame.sprite.collide_rect(self, person):
                if pygame.sprite.collide_mask(self, person):
                    self.stop = True

