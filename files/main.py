import pygame
import os
import sys
import random
from functions import *
from camera import Camera

pygame.init()
pygame.display.set_caption('Star World')
screen = pygame.display.set_mode(size)


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

    image = load_image("data/pictures/clone/jump.png", -1)
    image_rect = image.get_rect()
    sizes = (image_rect.width * koeff, image_rect.height * koeff)
    image = pygame.transform.scale(image, sizes)

    jump_image_right = image
    jump_image_left = pygame.transform.flip(image, True, False)

    def __init__(self, group, x, y, start_hp):
        super().__init__(group)
        self.start_position_x = x
        self.start_position_y = y
        self.start_hp = start_hp
        self.hp = start_hp

        self.image = MainHero.start_mas[0]
        self.rect = self.image.get_rect()

        self.rect.x = x * SIZE_OF_BLOCK
        self.rect.bottom = y * SIZE_OF_BLOCK + SIZE_OF_BLOCK

        self.process = [-1, 0]  # Что в данный момент делает главный герой

        self.speed = MAIN_HERO_SPEED

        self.left = False  # Направление движения

        self.finished = True  # Окончено ли действие

        self.v_x = 0  # Скорость движения по вертикали
        self.v_y = 0  # Скорость движения по горизонтали

        self.onGround = self.start_position_y

        self.picture_width = self.rect.width
        self.picture_height = self.rect.height
        self.last_damage = 0
        self.fall = False

        self.rect.width = self.picture_width * 0.75

    def get_damage(self, damage):
        if self.process[0] not in (3, -3, -2) and self.last_damage >= 6:
            self.hp -= damage
            if self.hp <= 0:
                self.die_2()
            else:
                self.process = [3, 0]
            self.last_damage = 0

    def update(self, left, right, up, space):
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

        if self.last_damage < 6:
            self.last_damage += 10 / fps
        if self.process[0] == -1:
            self.process[1] += 10 / fps
            if int(self.process[1]) == 0:
                self.image = MainHero.start_mas[0]
                self.rect = self.image.get_rect()

                self.rect.x = self.start_position_x * SIZE_OF_BLOCK
                self.rect.bottom = self.start_position_y * SIZE_OF_BLOCK + SIZE_OF_BLOCK

            elif int(self.process[1]) + 1 == len(MainHero.start_mas):
                self.process = [0, 0]
                self.image = MainHero.going_mas_right[0]
                self.rect = self.image.get_rect()

                self.rect.x = self.start_position_x * SIZE_OF_BLOCK
                self.rect.bottom = self.start_position_y * SIZE_OF_BLOCK + SIZE_OF_BLOCK

            self.image = MainHero.start_mas[int(self.process[1])]

            camera.update(self,
                          field.level_width * SIZE_OF_BLOCK,
                          field.level_height * SIZE_OF_BLOCK
                          )
            camera.move_camera(self)
            return
        elif self.process[0] == -3:
            if self.process[1] == 0.1:
                rect = self.image.get_rect()
                height = rect.height
                self.rect.bottom += height * 0.1

            self.process[1] += 6 / fps
            if int(self.process[1]) == len(MainHero.going_mas_left):
                self.die()

            else:
                if self.left:
                    self.image = MainHero.die_2_mas_left[int(self.process[1])]
                else:
                    self.image = MainHero.die_2_mas_right[int(self.process[1])]

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

        self.v_x = 0
        if left:
            self.v_x = -self.speed
            self.left = True
        if right:
            self.v_x = self.speed
            self.left = False
        if up:
            if self.onGround:  # Прыжок произойдет, только если ты стоишь а земле
                self.v_y = -JUMP
        if space:
            self.get_damage(25)

        if not self.onGround:
            self.v_y += GRAVITY / fps
        self.v_y += 1
        self.onGround = False

        self.rect.y += self.v_y / fps
        self.check_collide_y(self.v_y, field.textures_mas)

        self.rect.x += self.v_x / fps
        self.check_collide_x(self.v_x, field.textures_mas)


        camera.update(self,
                      field.level_width * SIZE_OF_BLOCK,
                      field.level_height * SIZE_OF_BLOCK
                      )

        if self.onGround:
            if self.v_x:
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
                self.fall = False

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

                self.fall = False

        else:
            if self.process[0] not in (-2, -3):
                self.process = [1, 0]
                if self.left:
                    self.image = MainHero.jump_image_left
                else:
                    self.image = MainHero.jump_image_right
            else:
                self.fall = True

        camera.move_camera(self)

        #if self.left:
        #    self.rect = self.image.get_rect(left=self.rect.left)
        #    self.rect.width =
        #else:
        #    self.rect = self.image.get_rect(left=self.rect.left)

    def check_collide_x(self, v_x, textures):
        for texture in textures:
            if pygame.sprite.collide_rect(self, texture):  # если есть пересечение платформы с игроком
                if v_x > 0:
                    self.rect.right = texture.rect.left

                if v_x < 0:
                    self.rect.left = texture.rect.right

    def check_collide_y(self, v_y, textures):
        self.rect.y += 1
        for texture in textures:
            if pygame.sprite.collide_rect(self, texture):  # если есть пересечение платформы с игроком
                if v_y > 0:  # если падает вниз
                    self.rect.bottom = texture.rect.top  # то не падает вниз
                    self.onGround = texture.rect.top  # и становится на что-то твердое
                    self.v_y = 0  # и энергия падения пропадает

                if v_y < 0:  # если движется вверх
                    self.rect.top = texture.rect.bottom  # то не движется вверх
                    self.v_y = 0  # и энергия прыжка пропадает

    def check_if_on_the_ground(self, textures):
        self.rect.y += 5
        for texture in textures:
            if pygame.sprite.collide_rect(self, texture):  # если есть пересечение платформы с игроком
                self.rect.y -= 5
                return True

        self.rect.y -= 5
        return False

    def die_1(self):
        self.process = [-2, 0]

    def die_2(self):
        self.process = [-3, 0]

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

        self.onGround = self.start_position_y

        self.hp = self.start_hp



class Stone(pygame.sprite.Sprite):
    image = load_image(r"data\pictures\textures\stone.png", -1)

    sizes = (SIZE_OF_BLOCK, SIZE_OF_BLOCK)

    image = pygame.transform.scale(image, sizes)
    def __init__(self, group, x_position, y_position):
        super().__init__(group)
        self.image = Stone.image

        self.x_position = x_position
        self.y_position = y_position

        self.rect = self.image.get_rect()
        self.rect.x = x_position * SIZE_OF_BLOCK
        self.rect.y = y_position * SIZE_OF_BLOCK

    def update(self):
        camera.move_camera(self)

    def replay(self):
        self.rect.x = self.x_position * SIZE_OF_BLOCK
        self.rect.y = self.y_position * SIZE_OF_BLOCK

class Field:
    def __init__(self):
        pass

    def start_game(self, map_name):
        f = open(map_name)
        self.map_name = map_name

        self.main_hero_sprite = pygame.sprite.Group()
        self.main_hero_bullet_sprites = pygame.sprite.Group()

        self.persons_sprites = pygame.sprite.Group()
        self.textures_sprites = pygame.sprite.Group()

        self.persons_a = list(map(int, f.readline().split()))
        self.persons_b = list(map(int, f.readline().split()))
        self.persons_c = list(map(int, f.readline().split()))
        self.persons_d = list(map(int, f.readline().split()))
        self.persons_e = list(map(int, f.readline().split()))
        self.persons_f = list(map(int, f.readline().split()))

        self.level_width, self.level_height = map(int, f.readline().split())
        level_mas = []
        self.textures_mas = []
        main_hero_pos = (0, 0)
        for i in range(self.level_height):
            mas = []
            line = f.readline()
            for j in range(self.level_width):
                if line[j] == '3':
                    mas.append('3')
                    sprite = Stone(self.textures_sprites, j, i)
                    self.textures_mas.append(sprite)
                    self.textures_sprites.add(sprite)
                elif line[j] == '#':
                    mas.append('0')
                    main_hero_pos = (j, i)

            level_mas.append(mas)

        self.main_hero = MainHero(self.main_hero_sprite, *main_hero_pos, 100)
        self.main_hero_sprite.add(self.main_hero)
        f.close()

    def replay(self):
        self.main_hero.replay()
        for i in self.persons_sprites:
            i.replay()

        for i in self.main_hero_bullet_sprites:
            i.kill()
        for i in self.textures_sprites:
            i.replay()


    def update(self, left, right, up, space):
        self.main_hero_sprite.update(left, right, up, space)

        self.persons_sprites.update(event)
        self.persons_sprites.draw(screen)

        self.textures_sprites.update()
        self.textures_sprites.draw(screen)

        self.main_hero_bullet_sprites.update()
        self.main_hero_bullet_sprites.draw(screen)

        self.main_hero_sprite.draw(screen)

    def move_camera_back(self):
        for sprite in self.main_hero_sprite:
            camera.move_back(sprite)
        for sprite in self.persons_sprites:
            camera.move_back(sprite)
        for sprite in self.textures_sprites:
            camera.move_back(sprite)
        for sprite in self.main_hero_bullet_sprites:
            camera.move_back(sprite)


running = True
clock = pygame.time.Clock()
field = Field()
field.start_game(r'data\maps\level_1.txt')

# обновляем положение всех спрайтов

camera = Camera()

while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    field.update(
        keys[pygame.K_LEFT],
        keys[pygame.K_RIGHT],
        keys[pygame.K_UP],
        keys[pygame.K_SPACE]
    )
    pygame.display.flip()
    field.move_camera_back()
    clock.tick(fps)

pygame.quit()
