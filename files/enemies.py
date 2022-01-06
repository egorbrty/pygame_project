from functions import *
import pygame


pygame.init()
screen = pygame.display.set_mode(size)


class Enemy(pygame.sprite.Sprite):
    def __init__(self, group, hp, armor, hit, crit, dexterity, accuracy, x_pos, y_pos):
        # Группа, здоровье, броня, сила удара, вероятность критического урона, ловкость, меткость, позиция
        # Метод вызывается, когда в персонажа попала пуля
        super().__init__(group)
        self.start_hp = hp
        self.hp = hp
        self.armor = armor
        self.hit = hit
        self.crit = crit
        self.dexterity = dexterity
        self.accuracy = accuracy
        self.process = [0, 0]
        self.image = self.going_mas_right[0]
        self.left = False

        self.rect = self.image.get_rect()
        self.rect.x = x_pos * SIZE_OF_BLOCK
        self.rect.bottom = y_pos * SIZE_OF_BLOCK + SIZE_OF_BLOCK

        self.onGround = True

        self.mas_stand = []

        self.v_x = 0
        self.v_y = 0

    def hit(self, hero_hit, hero_crit, hero_dexterity, hero_accuracy):
        # Показатели главного героя, высота, в которую попала пуля
        pass

    def get_hit(self):
        pass
        # Получение урона

    def is_alive(self):
        return self.hp > 0


class BattleDroid(Enemy):
    image = load_image(f"data/pictures/battle droid/going/going1.png", -1)
    image_rect = image.get_rect()
    koeff = BATTLE_DROID_HEIGHT / image_rect.height

    sizes = (SIZE_OF_BLOCK, SIZE_OF_BLOCK)
    going_mas_right = []
    going_mas_left = []

    for i in range(8):
        image = load_image(f"data/pictures/battle droid/going/going{i + 1}.png", -1)
        image_rect = image.get_rect()
        sizes = (image_rect.width * koeff, image_rect.height * koeff)
        image = pygame.transform.scale(image, sizes)

        going_mas_left.append(image)
        going_mas_right.append(pygame.transform.flip(image, True, False))
    run_width, run_height = sizes

    def update(self, camera, textures):
        if self.left:
            self.v_x = -BATTLE_DROID_SPEED
        else:
            self.v_x = BATTLE_DROID_SPEED

        if self.process[0] == 0:
            self.process[1] += 5 / fps
            if int(self.process[1]) == len(self.going_mas_right):
                self.process[1] = 0

            if self.left:
                self.image = self.going_mas_left[int(self.process[1])]
            else:
                self.image = self.going_mas_right[int(self.process[1])]

        self.v_y += GRAVITY / fps

        self.onGround = False

        self.rect.y += self.v_y / fps
        self.check_collide_y(self.v_y, textures)

        if self.mas_stand:
            v_mas = []
            for i in self.mas_stand:
                v_mas.append(i.get_speed(self.v_x, BATTLE_DROID_SPEED, self.left))
            self.v_x = sum(v_mas) / len(v_mas)

        self.rect.x += int(self.v_x / fps)
        self.check_collide_x(self.v_x, textures)

        camera.move_camera(self)

    def check_collide_x(self, v_x, textures):
        for texture in textures:
            if pygame.sprite.collide_rect(self, texture):  # если есть пересечение платформы с игроком
                if v_x > 0:
                    self.rect.right = texture.rect.left
                    self.left = True

                if v_x < 0:
                    self.rect.left = texture.rect.right
                    self.left = False

    def check_collide_y(self, v_y, textures):
        self.rect.y += 1
        self.mas_stand.clear()
        for texture in textures:
            if pygame.sprite.collide_rect(self, texture):  # если есть пересечение платформы с игроком
                if v_y > 0:
                    self.rect.bottom = texture.rect.top
                    self.onGround = texture.rect.top
                    self.v_y = 0  # энергия падения пропадает

                if v_y < 0:  # если движется вверх
                    self.rect.top = texture.rect.bottom
                    self.v_y = 0  # энергия прыжка пропадает
                self.mas_stand.append(texture)

    def die_2(self):
        self.kill()
