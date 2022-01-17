import random

from functions import *
from enemies_bullet import *


pygame.init()
screen = pygame.display.set_mode(size)


class Enemy(pygame.sprite.Sprite):
    def __init__(self, group, hp, armor, hit, crit, dexterity, accuracy, prize, x_pos, y_pos, stand):
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
        self.stand = stand  # Стоит враг или бегает
        self.prize = prize

        self.rect = self.image.get_rect()
        self.rect.x = x_pos * SIZE_OF_BLOCK + SIZE_OF_BLOCK // 2 - self.image.get_rect().width // 2
        self.rect.bottom = y_pos * SIZE_OF_BLOCK + SIZE_OF_BLOCK

        self.onGround = True

        self.mas_stand = []

        self.v_x = 0
        self.v_y = 0

        self.finished = True

    def get_hit(self, damage, money):
        # Получение урона
        self.process = [3, 0]
        self.hp -= damage
        if not self.is_alive():
            money += self.prize
            self.die_2()

    def is_alive(self):
        return self.hp > 0

    def die(self):
        self.kill()

    def shoot(self):
        if self.onGround and self.process[0] == 0:
            self.process = [2, 0]
        self.finished = False

    def rotate(self, main_hero_x_pos):
        """Поворачивает стоящего дроида в сторону игрoка"""
        if self.stand and self.process[0] == 0:
            self.left = main_hero_x_pos <= self.rect.x

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
        self.process = [-2, 0]



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

    hit_mas_right = []
    hit_mas_left = []

    for i in range(7):
        image = load_image(f"data/pictures/battle droid/hit/hit{i + 1}.png", -1)
        image_rect = image.get_rect()
        sizes = (image_rect.width * koeff, image_rect.height * koeff)
        image = pygame.transform.scale(image, sizes)

        hit_mas_left.append(image)
        hit_mas_right.append(pygame.transform.flip(image, True, False))

    die_1_mas_right = []
    die_1_mas_left = []

    for i in range(8):
        image = load_image(f"data/pictures/battle droid/die_1/die{i + 1}.png", -1)
        image_rect = image.get_rect()
        sizes = (image_rect.width * koeff, image_rect.height * koeff)
        image = pygame.transform.scale(image, sizes)

        die_1_mas_left.append(image)
        die_1_mas_right.append(pygame.transform.flip(image, True, False))

    shoot_mas_right = []
    shoot_mas_left = []

    for i in range(8):
        image = load_image(f"data/pictures/battle droid/shoot/shoot{i + 1}.png", -1)
        image_rect = image.get_rect()
        sizes = (image_rect.width * koeff, image_rect.height * koeff)
        image = pygame.transform.scale(image, sizes)

        shoot_mas_left.append(image)
        shoot_mas_right.append(pygame.transform.flip(image, True, False))

    stand_left = load_image(f"data/pictures/battle droid/stand.png", -1)
    image_rect = stand_left.get_rect()
    sizes = (image_rect.width * koeff, image_rect.height * koeff)
    stand_left = pygame.transform.scale(stand_left, sizes)
    stand_right = pygame.transform.flip(stand_left, True, False)

    def __init__(self, group, hp, armor, hit, crit, dexterity, accuracy, prize, x_pos, y_pos, stand, bullets):
        super().__init__(group, hp, armor, hit, crit, dexterity, accuracy, prize, x_pos, y_pos, stand)

        self.height = BATTLE_DROID_HEIGHT
        self.bullets = bullets
        self.last_shot = random.randint(0, fps * 5)

    def update(self, camera, textures):
        self.last_shot += 1

        if self.last_shot >= fps * 8:
            self.shoot()
            self.last_shot = 0

        if self.stand:
            self.v_x = 0

        elif self.left:
            self.v_x = -BATTLE_DROID_SPEED
        else:
            self.v_x = BATTLE_DROID_SPEED

        if self.process[0] == 3:
            self.process[1] += 10 / fps

            if int(self.process[1]) == len(self.hit_mas_right):
                self.process[0] = 0
                self.image = self.going_mas_right[0]
                self.rect.height = self.image.get_rect().height

            elif self.left:
                self.image = self.hit_mas_left[int(self.process[1])]
            else:
                self.image = self.hit_mas_right[int(self.process[1])]

            self.rect.height = self.image.get_rect().height
            if self.onGround:
                self.rect.bottom = self.onGround

            self.v_y += GRAVITY / fps
            self.onGround = False
            self.rect.y += self.v_y / fps
            self.check_collide_y(self.v_y, textures)

            camera.move_camera(self)
            return

        if self.process[0] == -2:
            self.process[1] += 10 / fps

            if self.process[1] < len(self.die_1_mas_left):
                if self.left:
                    self.image = self.die_1_mas_left[int(self.process[1])]
                else:
                    self.image = self.die_1_mas_right[int(self.process[1])]
            elif self.process[1] > len(self.die_1_mas_left) * 2:
                self.kill()

            bottom = self.rect.bottom
            self.rect.height = self.image.get_rect().height
            self.rect.bottom = bottom

            camera.move_camera(self)

            return

        if self.process[0] == 2:
            self.process[1] += 3 / fps

            if self.process[1] < len(self.shoot_mas_left):
                if self.left:
                    self.image = self.shoot_mas_left[int(self.process[1])]
                else:
                    self.image = self.shoot_mas_right[int(self.process[1])]
                if not self.finished and int(self.process[1]) == 6:
                    sprite = BattleDroidBullet(self.bullets, self.rect.x, self.rect.y, self.left, self)
                    self.bullets.add(sprite)
                    self.finished = True

            else:
                self.process = [0, 0]

            camera.move_camera(self)
            return

        if self.stand:
            if self.left:
                self.image = self.stand_left
            else:
                self.image = self.stand_right

        elif self.process[0] == 0:
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


class SuperBattleDroid(Enemy):
    image = load_image(f"data/pictures/super battle droid/going/going1.png", -1)
    image_rect = image.get_rect()
    koeff = SUPER_BATTLE_DROID_HEIGHT / image_rect.height

    sizes = (SIZE_OF_BLOCK, SIZE_OF_BLOCK)
    going_mas_right = []
    going_mas_left = []

    for i in range(8):
        image = load_image(f"data/pictures/super battle droid/going/going{i + 1}.png", -1)
        image_rect = image.get_rect()
        sizes = (image_rect.width * koeff, image_rect.height * koeff)
        image = pygame.transform.scale(image, sizes)

        going_mas_left.append(image)
        going_mas_right.append(pygame.transform.flip(image, True, False))
    run_width, run_height = sizes

    hit_mas_right = []
    hit_mas_left = []

    for i in range(5):
        image = load_image(f"data/pictures/super battle droid/hit/hit{i + 1}.png", -1)
        image_rect = image.get_rect()
        sizes = (image_rect.width * koeff, image_rect.height * koeff)
        image = pygame.transform.scale(image, sizes)

        hit_mas_left.append(image)
        hit_mas_right.append(pygame.transform.flip(image, True, False))

    die_1_mas_right = []
    die_1_mas_left = []

    for i in range(8):
        image = load_image(f"data/pictures/super battle droid/die_1/die{i + 1}.png", -1)
        image_rect = image.get_rect()
        sizes = (image_rect.width * koeff, image_rect.height * koeff)
        image = pygame.transform.scale(image, sizes)

        die_1_mas_left.append(image)
        die_1_mas_right.append(pygame.transform.flip(image, True, False))

    shoot_mas_right = []
    shoot_mas_left = []

    for i in range(6):
        image = load_image(f"data/pictures/super battle droid/shoot/shoot{i + 1}.png", -1)
        image_rect = image.get_rect()
        sizes = (image_rect.width * koeff, image_rect.height * koeff)
        image = pygame.transform.scale(image, sizes)

        shoot_mas_left.append(image)
        shoot_mas_right.append(pygame.transform.flip(image, True, False))

    stand_left = load_image(f"data/pictures/super battle droid/stand.png", -1)
    image_rect = stand_left.get_rect()
    sizes = (image_rect.width * koeff, image_rect.height * koeff)
    stand_left = pygame.transform.scale(stand_left, sizes)
    stand_right = pygame.transform.flip(stand_left, True, False)

    def __init__(self, group, hp, armor, hit, crit, dexterity, accuracy, prize, x_pos, y_pos, stand, bullets):
        super().__init__(group, hp, armor, hit, crit, dexterity, accuracy, prize, x_pos, y_pos, stand)

        self.height = BATTLE_DROID_HEIGHT
        self.bullets = bullets
        self.last_shot = random.randint(0, fps * 5)

    def update(self, camera, textures):
        self.last_shot += 1

        if self.last_shot >= fps * 8:
            self.shoot()
            self.last_shot = 0

        if self.stand:
            self.v_x = 0

        elif self.left:
            self.v_x = -SUPER_BATTLE_DROID_SPEED
        else:
            self.v_x = SUPER_BATTLE_DROID_SPEED

        if self.process[0] == 3:
            self.process[1] += 10 / fps

            if int(self.process[1]) == len(self.hit_mas_right):
                self.process[0] = 0
                self.image = self.going_mas_right[0]
                self.rect.height = self.image.get_rect().height

            elif self.left:
                self.image = self.hit_mas_left[int(self.process[1])]
            else:
                self.image = self.hit_mas_right[int(self.process[1])]

            self.rect.height = self.image.get_rect().height
            if self.onGround:
                self.rect.bottom = self.onGround

            self.v_y += GRAVITY / fps
            self.onGround = False
            self.rect.y += self.v_y / fps
            self.check_collide_y(self.v_y, textures)

            camera.move_camera(self)
            return

        if self.process[0] == -2:
            self.process[1] += 10 / fps

            if self.process[1] < len(self.die_1_mas_left):
                if self.left:
                    self.image = self.die_1_mas_left[int(self.process[1])]
                else:
                    self.image = self.die_1_mas_right[int(self.process[1])]
            elif self.process[1] > len(self.die_1_mas_left) * 2:
                self.kill()

            bottom = self.rect.bottom
            self.rect.height = self.image.get_rect().height
            self.rect.bottom = bottom

            camera.move_camera(self)

            return

        if self.process[0] == 2:
            self.process[1] += 3 / fps

            if self.process[1] < len(self.shoot_mas_left):
                if self.left:
                    self.image = self.shoot_mas_left[int(self.process[1])]
                else:
                    self.image = self.shoot_mas_right[int(self.process[1])]

            else:
                self.process = [0, 0]
                sprite = SuperBattleDroidBullet(self.bullets,
                                                self.rect.x, self.rect.y - self.rect.height * 0.2,
                                                self.left, self)
                self.bullets.add(sprite)
                self.finished = True

            camera.move_camera(self)
            return

        if self.stand:
            if self.left:
                self.image = self.stand_left
            else:
                self.image = self.stand_right

        elif self.process[0] == 0:
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


