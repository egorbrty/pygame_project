from functions import *


pygame.init()
screen = pygame.display.set_mode(size)


class EnemiesBullet(pygame.sprite.Sprite):
    def __init__(self, group, x_position, y_position, left, shooter):
        super().__init__(group)
        self.x_position = x_position
        self.y_position = y_position

        self.shooter = shooter

        self.left = left

        self.stop = False
        self.process = 0


class BattleDroidBullet(EnemiesBullet):
    mas_right = []
    mas_left = []
    sizes = (MAIN_HERO_HEIGHT / 2, MAIN_HERO_HEIGHT / 2)

    for i in range(4):
        image = load_image(f"data/pictures/battle droid/shoot/bullet{i + 1}.png", -1)

        image = pygame.transform.scale(image, sizes)

        mas_left.append(image)
        mas_right.append(pygame.transform.flip(image, True, False))

    def __init__(self, group, x_position, y_position, left, shooter):
        super().__init__(group, x_position, y_position, left, shooter)
        if self.left:
            self.image = self.mas_left[0]
        else:
            self.image = self.mas_right[0]
        self.rect = self.image.get_rect()
        self.rect.x = x_position
        self.rect.y = y_position

    def update(self, camera, textures, main_hero, messages):
        if self.stop:
            # Попадание
            self.kill()
            return

        if self.left:
             self.rect.x -= 500 / fps
        else:
            self.rect.x += 500 / fps

        camera.move_camera(self)

        for texture in textures:
            if pygame.sprite.collide_rect(self, texture):
                self.kill()
                texture.shot()
                break

        if pygame.sprite.collide_rect(self, main_hero):
            if pygame.sprite.collide_mask(self, main_hero):
                self.stop = True
                if hit(self.shooter.accuracy, main_hero.dexterity):
                    damage = self.shooter.hit
                    if hit(self.shooter.crit, main_hero.armor):
                        print('Критический')
                        damage *= 2
                    if main_hero.is_alive():
                        main_hero.get_damage_ch(damage)
                else:
                    print('Мимо')
