import pygame.sprite

from functions import *
from camera import Camera
from textures import *
from enemies import BattleDroid, SuperBattleDroid, Destroyer
from bullet import Bullet
from hp_scale import Scale
from message import Message
from money import Money
from finish import Cup
from pause import *
from star import Star
from decorations import Decoration


class MainHero(pygame.sprite.Sprite):
    image = load_image(f"data/pictures/clone/running/run1.png", -1)
    image_rect = image.get_rect()
    koeff = MAIN_HERO_HEIGHT / image_rect.height

    sizes = (SIZE_OF_BLOCK, SIZE_OF_BLOCK)
    going_mas_right = []
    going_mas_left = []

    for i in range(8):
        image = load_image(f"data/pictures/clone/running/run{i + 1}.png", -1)
        image_rect = image.get_rect()
        sizes = (image_rect.width * koeff, image_rect.height * koeff)
        image = pygame.transform.scale(image, sizes)

        going_mas_right.append(image)
        going_mas_left.append(pygame.transform.flip(image, True, False))
    run_width, run_height = sizes

    start_mas = []

    for i in range(13):
        image = load_image(f"data/pictures/clone/start/start{i + 1}.png", -1)
        image_rect = image.get_rect()
        sizes = (image_rect.width * koeff, image_rect.height * koeff)
        image = pygame.transform.scale(image, sizes)

        start_mas.append(image)

    die_2_mas_right = []
    die_2_mas_left = []

    for i in range(8):
        image = load_image(f"data/pictures/clone/die_2/die_2_{i + 1}.png", -1)
        image_rect = image.get_rect()
        sizes = (image_rect.width * koeff, image_rect.height * koeff)
        image = pygame.transform.scale(image, sizes)

        die_2_mas_right.append(image)
        die_2_mas_left.append(pygame.transform.flip(image, True, False))

    die_1_mas_right = []
    die_1_mas_left = []

    for i in range(11):
        image = load_image(f"data/pictures/clone/die_1/die_1_{i + 1}.png", -1)
        image_rect = image.get_rect()
        sizes = (image_rect.width * koeff, image_rect.height * koeff)
        image = pygame.transform.scale(image, sizes)

        die_1_mas_right.append(image)
        die_1_mas_left.append(pygame.transform.flip(image, True, False))

    stand_mas_right = []
    stand_mas_left = []

    for i in range(3):
        image = load_image(f"data/pictures/clone/stand/stand{i + 1}.png", -1)
        image_rect = image.get_rect()
        sizes = (image_rect.width * koeff, image_rect.height * koeff)
        image = pygame.transform.scale(image, sizes)

        stand_mas_right.append(image)
        stand_mas_left.append(pygame.transform.flip(image, True, False))

    hit_mas_right = []
    hit_mas_left = []

    for i in range(6):
        image = load_image(f"data/pictures/clone/hit/hit{i + 1}.png", -1)
        image_rect = image.get_rect()
        sizes = (image_rect.width * koeff, image_rect.height * koeff)
        image = pygame.transform.scale(image, sizes)

        hit_mas_right.append(image)
        hit_mas_left.append(pygame.transform.flip(image, True, False))

    shoot_mas_right = []
    shoot_mas_left = []

    for i in range(7):
        image = load_image(f"data/pictures/clone/shoot/shoot{i + 1}.png", -1)
        image_rect = image.get_rect()
        sizes = (image_rect.width * koeff, image_rect.height * koeff)
        image = pygame.transform.scale(image, sizes)

        shoot_mas_right.append(image)
        shoot_mas_left.append(pygame.transform.flip(image, True, False))

    image = load_image("data/pictures/clone/jump.png", -1)
    image_rect = image.get_rect()
    sizes = (image_rect.width * koeff, image_rect.height * koeff)
    image = pygame.transform.scale(image, sizes)

    jump_image_right = image
    jump_image_left = pygame.transform.flip(image, True, False)

    def __init__(self, group, start_hp, armor, hit, crit, dexterity, accuracy, x_pos, y_pos, money):
        super().__init__(group)
        self.start_position_x = x_pos
        self.start_position_y = y_pos
        self.start_hp = start_hp
        self.hp = start_hp

        self.money = money

        self.armor = armor
        self.hit = hit
        self.crit = crit
        self.dexterity = dexterity
        self.accuracy = accuracy

        self.image = MainHero.start_mas[0]
        self.rect = self.image.get_rect()

        self.rect.x = x_pos * SIZE_OF_BLOCK
        self.rect.bottom = y_pos * SIZE_OF_BLOCK + SIZE_OF_BLOCK

        self.process = [-1, 0]  # Что в данный момент делает главный герой

        self.speed = MAIN_HERO_SPEED

        self.left = False  # Направление движения

        self.finished = True  # Был ли выстрел

        self.v_x = 0  # Скорость движения по вертикали
        self.v_y = 0  # Скорость движения по горизонтали

        self.onGround = self.start_position_y

        self.picture_width = self.rect.width
        self.picture_height = self.rect.height
        self.last_damage = 0
        self.fall = False

        self.rect.width = self.picture_width * 0.75

        self.mas_stand = list()  # Массив будет содержать ссылки на блоки, на которых стоит

        self.started = 0  # Как давно началась игра

    def get_damage_ch(self, damage, y_pos=None):
        # Получает урон
        if not self.is_alive():
            return

        self.hp -= damage


        if self.hp <= 0:
            if y_pos is not None:
                self.onGround = y_pos

            self.die_2()
        else:
            if self.onGround and y_pos is None:
                self.process = [3, 0]

    def get_damage_ch_shot(self, damage, left):
        # Получает урон от выстрела
        self.left = not left
        if not self.is_alive():
            return

        self.hp -= damage

        if not self.is_alive():
            self.die_1()
        else:
            if self.onGround:
                self.process = [3, 0]

    def is_alive(self):
        return self.hp > 0

    def get_damage(self, damage):
        # Получает урон если все условия соблюдены
        if self.process[0] not in (-3, -2) and self.last_damage >= 15:
            self.get_damage_ch(damage)

            self.last_damage = 0

    def check_position(self):
        """Убивает игрока, если он вылетел за пределы карты"""
        if self.rect.x < 0 or self.rect.x > width:
            self.fall = True
            self.die_2()
        elif self.rect.y < 0 or self.rect.y > height:
            self.fall = True
            self.die_2()

    def update(self, left, right, up, space):
        # Чтобы игрок не мог управлять героем первые в секунды игры
        if self.started < fps * 1.5:
            self.started += 1
            left, right, up, space = False, False, False, False

        if self.process[0] != 2:
            self.rect.width = self.picture_width * 0.75

        if self.process[0] in (-2, -3) and self.fall:
            self.rect.y += self.v_y / fps
            self.v_y += GRAVITY / fps
            if self.rect.y > SIZE_OF_BLOCK * field.level_height + 1000:
                field.replay()

            camera.update(self,
                          field.level_width * SIZE_OF_BLOCK,
                          field.level_height * SIZE_OF_BLOCK
                          )
            camera.move_camera(self)
            return

        if self.last_damage < 15:
            self.last_damage += 15 / fps
        if self.process[0] == -1:
            self.process[1] += 10 / fps
            self.image = MainHero.start_mas[0]
            self.rect = self.image.get_rect()

            self.rect.x = self.start_position_x * SIZE_OF_BLOCK
            self.rect.bottom = self.start_position_y * SIZE_OF_BLOCK + SIZE_OF_BLOCK

            if int(self.process[1]) == len(MainHero.start_mas):
                self.process = [0, 0]
                self.image = MainHero.going_mas_right[0]
                self.rect = self.image.get_rect()

                self.rect.x = self.start_position_x * SIZE_OF_BLOCK
                self.rect.bottom = self.start_position_y * SIZE_OF_BLOCK + SIZE_OF_BLOCK
                camera.update(self,
                              field.level_width * SIZE_OF_BLOCK,
                              field.level_height * SIZE_OF_BLOCK
                              )
                camera.move_camera(self)
                return

            self.image = MainHero.start_mas[int(self.process[1])]

            camera.update(self,
                          field.level_width * SIZE_OF_BLOCK,
                          field.level_height * SIZE_OF_BLOCK
                          )
            camera.move_camera(self)
            return
        elif self.process[0] == -3:
            # die_2
            self.process[1] += 2 / fps
            if int(self.process[1]) == len(MainHero.die_2_mas_left):
                self.die()

            else:
                if self.left:
                    self.image = MainHero.die_2_mas_left[int(self.process[1])]
                else:
                    self.image = MainHero.die_2_mas_right[int(self.process[1])]

            self.rect.height = MAIN_HERO_HEIGHT * 1.1

            self.rect.bottom = self.onGround
            self.rect.bottom += MAIN_HERO_HEIGHT * 0.19
            camera.update(self,
                          field.level_width * SIZE_OF_BLOCK,
                          field.level_height * SIZE_OF_BLOCK
                          )
            camera.move_camera(self)

            return

        elif self.process[0] == -2:
            # die_1
            self.process[1] += 8 / fps
            if int(self.process[1]) == len(MainHero.die_1_mas_left):
                self.die()

            else:
                if self.left:
                    self.image = MainHero.die_1_mas_left[int(self.process[1])]
                else:
                    self.image = MainHero.die_1_mas_right[int(self.process[1])]

            self.rect.height = self.image.get_height()
            self.rect.bottom = self.onGround

            camera.update(self,
                          field.level_width * SIZE_OF_BLOCK,
                          field.level_height * SIZE_OF_BLOCK
                          )
            camera.move_camera(self)

            return

        elif self.process[0] == 3:
            self.process[1] += 10 / fps
            if int(self.process[1]) == len(MainHero.hit_mas_left):
                self.process = [5, 0]
                self.check_collide_x(int(self.left), field.textures_sprites)

            else:
                if self.left:
                    self.image = MainHero.hit_mas_left[int(self.process[1])]
                else:
                    self.image = MainHero.hit_mas_right[int(self.process[1])]
                self.rect.bottom = self.onGround
                self.rect.height = self.image.get_rect().height

            camera.update(self,
                          field.level_width * SIZE_OF_BLOCK,
                          field.level_height * SIZE_OF_BLOCK
                          )
            camera.move_camera(self)

            return
            # hit_mas_left

        if space and self.process[0] in (0, 5) and self.onGround:
            if self.process[0] != 2:
                self.process = [2, 0]
                self.finished = False

                if not self.left:
                    self.rect.x += MAIN_HERO_HEIGHT * 0.18

        if self.process[0] == 2:
            if not self.onGround:
                self.process = [5, 0]
                self.finished = True

            elif self.process[1] >= len(self.shoot_mas_left):
                self.process = [5, 0]
                if not self.left:
                    self.rect.x -= MAIN_HERO_HEIGHT * 0.18

            else:
                if self.left:
                    self.image = self.shoot_mas_left[int(self.process[1])]
                else:
                    self.image = self.shoot_mas_right[int(self.process[1])]

                if int(self.process[1]) == 5 and not self.finished:
                    sprite = Bullet(field.main_hero_bullet_sprites,
                                    self.rect.x + MAIN_HERO_HEIGHT * 0.55,
                                    self.rect.y + MAIN_HERO_HEIGHT * 0.25,
                                    self.hit, self.crit, self.accuracy, self.left, self.money)
                    field.main_hero_bullet_sprites.add(sprite)
                    self.finished = True

                self.process[1] += 10 / fps

                self.rect.height = self.image.get_height()
                self.rect.bottom = self.onGround

                camera.update(self,
                              field.level_width * SIZE_OF_BLOCK,
                              field.level_height * SIZE_OF_BLOCK
                              )

                camera.move_camera(self)
                return


        self.v_x = 0
        if left and self.process[0] != 2:
            self.v_x -= self.speed
            self.left = True
        if right and self.process[0] != 2:
            self.v_x += self.speed
            self.left = False

        if up:
            if self.onGround and self.process[0] in (0, 5, 1):  # Прыжок произойдет, только если ты стоишь а земле
                self.v_y = -JUMP

        if not self.onGround:
            self.v_y += GRAVITY / fps
        self.v_y += 1
        self.onGround = False

        self.rect.y += self.v_y / fps

        self.check_collide_y(self.v_y, field.textures_sprites)
        # Рассчет скорости (зависит от блоков, по которым движется персонаж)
        if self.mas_stand:
            v_mas = []
            for i in self.mas_stand:
                v_mas.append(i.get_speed(self.v_x, self.speed, self.left))
            self.v_x = sum(v_mas) / len(v_mas)
        if self.process[0] != 2:
            self.rect.x += int(self.v_x / fps)
            self.check_collide_x(self.v_x, field.textures_sprites)

        if self.onGround and not up and self.process[0] not in (-3, 3, 2):
            if (left or right) and not (right and left):
                if self.process[0] != 0:
                    self.process = [0, 0]
            else:
                if self.process[0] != 5:
                    self.process = [5, 0]

            if self.process[0] == 0:
                self.rect.height = MainHero.run_height

                self.rect.bottom = self.onGround
                self.process[1] += 10 / fps
                if int(self.process[1]) == len(self.going_mas_left):
                    self.process[1] = 0

                if self.left:
                    self.image = MainHero.going_mas_left[int(self.process[1])]
                else:
                    self.image = MainHero.going_mas_right[int(self.process[1])]

            elif self.process[0] == 5:
                if self.left:
                    self.image = MainHero.stand_mas_left[int(self.process[1])]
                else:
                    self.image = MainHero.stand_mas_right[int(self.process[1])]

                self.process[1] += 1 / fps

                if int(self.process[1]) == len(MainHero.stand_mas_left):
                    self.process[1] = 0

                self.rect.bottom = self.onGround
                self.rect.height = self.image.get_rect().height

        elif self.process[0] != 3:
            if self.process[0] not in (-2, -3):
                self.process = [1, 0]
                if self.left:
                    self.image = MainHero.jump_image_left
                else:
                    self.image = MainHero.jump_image_right
        if self.process[0] in (0, 5):
            self.rect.bottom = self.onGround

        if self.last_damage >= 15:
            damage_sum = 0  # Урон, который персонаж
            for i in field.persons_sprites:
                if i.is_alive() and pygame.sprite.collide_rect(self, i):  # если есть пересечение врага с игроком
                    if hit(i.accuracy, self.dexterity):
                        print('Попадание')
                        damage = i.hit
                        if hit(i.crit, self.armor):
                            print('crit')
                            damage *= 2
                        damage_sum += damage
                    else:
                        print('Мимо!')

            if damage_sum:
                self.get_damage(damage_sum)

        camera.update(self,
                      field.level_width * SIZE_OF_BLOCK,
                      field.level_height * SIZE_OF_BLOCK
                      )

        camera.move_camera(self)

        self.check_position()

    def check_collide_x(self, v_x, textures):
        for texture in textures:
            if pygame.sprite.collide_rect(self, texture):  # если есть пересечение платформы с игроком
                if v_x > 0:
                    self.rect.right = texture.rect.left

                if v_x < 0:
                    self.rect.left = texture.rect.right

    def check_collide_y(self, v_y, textures):
        self.rect.y += 1
        self.mas_stand.clear()

        bottom = []  # Нижняя точка игрока
        for texture in textures:
            if pygame.sprite.collide_rect(self, texture):
                texture.touch(self)
                if v_y > 0:
                    bottom.append(texture.rect.top)
                    self.onGround = texture.rect.top
                    self.v_y = 0

                if v_y < 0:
                    self.rect.top = texture.rect.bottom
                    self.v_y = 0
                self.mas_stand.append(texture)
        if bottom:
            self.rect.bottom = min(bottom)

    def check_if_on_the_ground(self, textures):
        self.rect.y += 5
        for texture in textures:
            if pygame.sprite.collide_rect(self, texture):
                self.rect.y -= 5
                return True

        self.rect.y -= 5
        return False

    def die_1(self):
        self.process = [-2, 0]
        self.fall = not self.onGround

    def die_2(self):
        self.process = [-3, 0]
        self.fall = not self.onGround

    def die(self):
        field.replay()

    def replay(self):
        self.rect.x = self.start_position_x * SIZE_OF_BLOCK
        self.rect.bottom = self.start_position_y * SIZE_OF_BLOCK + SIZE_OF_BLOCK

        self.process = [-1, 0]  # Что в данный момент делает главный герой

        self.left = False  # Направление движения

        self.finished = True  # Окончено ли действие

        self.v_x = 0  # Скорость движения по вертикали
        self.v_y = 0  # Скорость движения по горизонтали

        self.onGround = self.start_position_y * SIZE_OF_BLOCK

        self.hp = self.start_hp

        self.started = 0


class Field:
    def __init__(self, money):
        self.money_sprite = pygame.sprite.Group()
        self.money = Money(self.money_sprite, money)
        self.money_sprite.add(self.money)

    def start_game(self, map_name, main_hero_parameters):
        self.main_hero_parameters = main_hero_parameters
        f = open(map_name, 'r', encoding='utf-8')
        self.map_name = map_name
        self.star_sprite = pygame.sprite.Group()

        self.main_hero_sprite = pygame.sprite.Group()
        self.main_hero_bullet_sprites = pygame.sprite.Group()
        self.enemies_bullet_sprites = pygame.sprite.Group()

        self.decoration_sprites = pygame.sprite.Group()

        self.persons_sprites = pygame.sprite.Group()
        self.textures_sprites = pygame.sprite.Group()
        self.messages = Message()

        self.cup_sprites = pygame.sprite.Group()

        self.persons_a = list(map(int, f.readline().split()))
        self.persons_b = list(map(int, f.readline().split()))
        self.persons_c = list(map(int, f.readline().split()))
        self.persons_d = list(map(int, f.readline().split()))
        self.persons_e = list(map(int, f.readline().split()))
        self.persons_f = list(map(int, f.readline().split()))

        self.level_width, self.level_height = map(int, f.readline().split())

        self.textures_mas = []

        self.start_position_a = []
        self.start_position_b = []
        self.start_position_c = []
        self.start_position_d = []
        self.start_position_e = []
        self.start_position_f = []

        main_hero_pos = (0, 0)
        star_pos = (0, 0)
        for i in range(self.level_height):
            line = f.readline()
            for j in range(self.level_width):
                if line[j] == '3':
                    sprite = Stone(self.textures_sprites, j, i)
                    self.textures_mas.append(sprite)
                    self.textures_sprites.add(sprite)

                elif line[j] == '1':
                    sprite = Grass(self.textures_sprites, j, i)
                    self.textures_mas.append(sprite)
                    self.textures_sprites.add(sprite)

                elif line[j] == '2':
                    sprite = Sand(self.textures_sprites, j, i)
                    self.textures_mas.append(sprite)
                    self.textures_sprites.add(sprite)

                elif line[j] == '6':
                    sprite = Platform(self.textures_sprites, j, i)
                    self.textures_mas.append(sprite)
                    self.textures_sprites.add(sprite)

                elif line[j] == '7':
                    sprite = Spike(self.textures_sprites, j, i)
                    self.textures_mas.append(sprite)
                    self.textures_sprites.add(sprite)

                elif line[j] == '8':
                    sprite = Ice(self.textures_sprites, j, i)
                    self.textures_mas.append(sprite)
                    self.textures_sprites.add(sprite)

                elif line[j] == '9':
                    sprite = BreakingWall(self.textures_sprites, j, i)
                    self.textures_mas.append(sprite)
                    self.textures_sprites.add(sprite)

                elif line[j] == '#':
                    main_hero_pos = (j, i)

                elif line[j] == 'A':
                    sprite = BattleDroid(self.persons_sprites, *self.persons_a, j, i, False,
                                         self.enemies_bullet_sprites)
                    self.persons_sprites.add(sprite)
                    self.start_position_a.append(((j, i), False))

                elif line[j] == 'a':
                    sprite = BattleDroid(self.persons_sprites, *self.persons_a, j, i, True,
                                         self.enemies_bullet_sprites)
                    self.persons_sprites.add(sprite)
                    self.start_position_a.append(((j, i), True))

                elif line[j] == 'B':
                    sprite = SuperBattleDroid(self.persons_sprites, *self.persons_b, j, i, False,
                                              self.enemies_bullet_sprites)
                    self.persons_sprites.add(sprite)
                    self.start_position_b.append(((j, i), False))

                elif line[j] == 'b':
                    sprite = SuperBattleDroid(self.persons_sprites, *self.persons_b, j, i, True,
                                              self.enemies_bullet_sprites)
                    self.persons_sprites.add(sprite)
                    self.start_position_b.append(((j, i), True))

                elif line[j] == 'C':
                    sprite = Destroyer(self.persons_sprites, *self.persons_c, j, i, False,
                                       self.enemies_bullet_sprites)
                    self.persons_sprites.add(sprite)
                    self.start_position_c.append(((j, i), False))

                elif line[j] == 'c':
                    sprite = Destroyer(self.persons_sprites, *self.persons_c, j, i, True,
                                       self.enemies_bullet_sprites)
                    self.persons_sprites.add(sprite)
                    self.start_position_c.append(((j, i), True))

                elif line[j] == '@':
                    sprite = Cup(self.cup_sprites, j, i)
                    self.cup_sprites.add(sprite)

                elif line[j] == 'R':
                    sprite = Decoration(self.decoration_sprites, j, i, r'data\pictures\decorations\right.png')
                    self.decoration_sprites.add(sprite)

                elif line[j] == 'L':
                    sprite = Decoration(self.decoration_sprites, j, i, r'data\pictures\decorations\left.png')
                    self.decoration_sprites.add(sprite)

                elif line[j] == '*':
                    star_pos = (j, i)

        self.main_hero = MainHero(self.main_hero_sprite, *self.main_hero_parameters, *main_hero_pos, self.money)
        self.main_hero_sprite.add(self.main_hero)

        self.star = Star(self.star_sprite, *star_pos)
        self.star_sprite.add(self.star)

        self.main_hero_scale_hp = Scale(self.main_hero)

        f.close()

    def replay(self):
        for i in self.persons_sprites:
            i.kill()
        for i in self.enemies_bullet_sprites:
            i.kill()

        self.main_hero.replay()
        for i in self.main_hero_bullet_sprites:
            i.kill()
        for i in self.textures_mas:
            i.replay(self.textures_sprites)

        for i in self.start_position_a:
            sprite = BattleDroid(self.persons_sprites, *self.persons_a, *i[0], i[1], self.enemies_bullet_sprites)
            self.persons_sprites.add(sprite)

        for i in self.start_position_b:
            sprite = SuperBattleDroid(self.persons_sprites, *self.persons_b, *i[0], i[1], self.enemies_bullet_sprites)
            self.persons_sprites.add(sprite)

        for i in self.start_position_c:
            sprite = Destroyer(self.persons_sprites, *self.persons_b, *i[0], i[1], self.enemies_bullet_sprites)
            self.persons_sprites.add(sprite)

        for i in self.decoration_sprites:
            i.replay()

        self.messages.replay()

        self.main_hero_scale_hp.replay()

        for i in self.cup_sprites:
            i.replay()

    def update(self, left, right, up, space):
        self.main_hero_sprite.update(left, right, up, space)
        self.persons_sprites.update(camera, self.textures_sprites)
        self.textures_sprites.update(camera)

        self.decoration_sprites.update(camera)
        self.decoration_sprites.draw(screen)

        self.cup_sprites.update(camera)

        self.main_hero_bullet_sprites.update(camera, self.textures_sprites, self.persons_sprites, self.messages)
        self.enemies_bullet_sprites.update(camera, self.textures_sprites, self.main_hero, self.messages)

        for i in self.persons_sprites:
            """Разворачивает стоящих в сторону игрока"""
            i.rotate(self.main_hero.rect.x)

        self.persons_sprites.draw(screen)
        self.textures_sprites.draw(screen)
        self.main_hero_bullet_sprites.draw(screen)

        self.cup_sprites.draw(screen)

        self.main_hero_sprite.draw(screen)
        self.enemies_bullet_sprites.draw(screen)

        for i in self.persons_sprites:
            health_scale(screen, i)

        self.messages.draw(screen, camera)

        self.main_hero_scale_hp.update(screen)

        self.money_sprite.update(screen)
        self.money_sprite.draw(screen)

        self.star_sprite.update(camera)
        self.star_sprite.draw(screen)

        for cup in self.cup_sprites:
            if pygame.sprite.collide_rect(self.main_hero, cup):  # если есть пересечение платформы с игроком
                return 'win'

        for star in self.star_sprite:
            if pygame.sprite.collide_rect(self.main_hero, star):  # если есть пересечение платформы с игроком
                self.star.kill()

    def move_camera_back(self):
        for sprite in self.main_hero_sprite:
            camera.move_back(sprite)

        for sprite in self.persons_sprites:
            camera.move_back(sprite)

        for sprite in self.textures_sprites:
            camera.move_back(sprite)

        for sprite in self.main_hero_bullet_sprites:
            camera.move_back(sprite)

        for sprite in self.enemies_bullet_sprites:
            camera.move_back(sprite)

        for sprite in self.cup_sprites:
            camera.move_back(sprite)

        for sprite in self.decoration_sprites:
            camera.move_back(sprite)

        for sprite in self.star_sprite:
            camera.move_back(sprite)

def play(map_name, main_hero_parameters, start_money):  # Сколько денег у игрока было в момент игры
    global camera, field
    running = True
    clock = pygame.time.Clock()
    money = start_money

    field = Field(money)

    field.start_game(map_name, main_hero_parameters)

    camera = Camera()

    game_paused = False

    pause_sprite_group = pygame.sprite.Group()
    pause = Pause(pause_sprite_group)
    pause_sprite_group.add(pause)

    pause_window_buttons = pygame.sprite.Group()
    exit_button = Button(pause_window_buttons, 'data/pictures/exit.png', (width * 0.3, height // 2))
    replay_button = Button(pause_window_buttons, 'data/pictures/replay.png', (width * 0.5, height // 2))
    continue_button = Button(pause_window_buttons, 'data/pictures/continue.png', (width * 0.7, height // 2))

    pause_window_buttons.add(exit_button)
    pause_window_buttons.add(replay_button)
    pause_window_buttons.add(continue_button)

    while running:
        screen.fill((0, 0, 0))
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'exit', field.money.number
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                click = True

        if game_paused:
            mouse_pos = pygame.mouse.get_pos()

            # --------------------------------------Отрисовка окна паузы------------------------------------------------
            pygame.draw.rect(screen, (255, 255, 255),
                             (int(width * 0.2), int(height * 0.3), int(width * 0.6), int(height * 0.4)),
                             5
                             )
            pause_window_buttons.update(mouse_pos)
            pause_window_buttons.draw(screen)

            if click and exit_button.rect.collidepoint(mouse_pos):
                return 0, field.money.number
            elif click and replay_button.rect.collidepoint(mouse_pos):
                field.replay()
                game_paused = False
            elif click and continue_button.rect.collidepoint(mouse_pos):
                game_paused = False

            # --------------------------------------Отрисовка окна паузы------------------------------------------------

            pygame.display.update((int(width * 0.2), int(height * 0.3), int(width * 0.6), int(height * 0.4)))
            clock.tick(fps)

            continue

        keys = pygame.key.get_pressed()

        res = field.update(
            keys[pygame.K_LEFT],
            keys[pygame.K_RIGHT],
            keys[pygame.K_UP],
            keys[pygame.K_SPACE]
        )
        if res == 'win':
            return (True, not len(field.persons_sprites), not len(field.star_sprite)), field.money.number
            # Первая звезда точно есть. Вторая - если все враги убиты

        mouse_pos = pygame.mouse.get_pos()

        mouse_is_on_pause_button = pause.rect.collidepoint(mouse_pos)

        pause_sprite_group.update(mouse_is_on_pause_button)
        pause_sprite_group.draw(screen)

        if mouse_is_on_pause_button and click:
            game_paused = True

        pygame.display.flip()
        field.move_camera_back()
        clock.tick(fps)

    pygame.quit()


