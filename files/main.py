import time
from game_main_process import play
from functions import *


WIDTH = 1350
HEIGHT = 700
FPS = 30

# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# распаковка переменных из БД

flag = 0
s1 = s2 = s3 = s4 = s5 = s6 = 0

prise1 = 10
prise2 = 10
prise3 = 10
prise4 = 10
prise5 = 10
prise6 = 10


class DataBase:
    """Отвечает за хранение файлов об игроке"""
    def __init__(self):
        file = open(r"data\pumping\money.txt", "r")
        self.money = int(file.readline().strip())

        file = open(r"data\pumping\main_hero_parameters.txt", "r")
        self.main_hero_parameters = []
        for i in range(6):
            self.main_hero_parameters.append(int(file.readline().strip()))


    def save(self):
        # Количество денег
        file = open(r"data\pumping\money.txt", "w")
        file.write(str(self.money))
        file.close()

        # Прокачка персонажей
        file = open(r"data\pumping\main_hero_parameters.txt", "w")

        for i in self.main_hero_parameters:
            file.write(str(i) + '\n')

    def bye(self, number):
        if self.money >= 10:
            self.main_hero_parameters[number - 1] += 1
            self.money -= 10
            time.sleep(0.2)

    def get_level(self, num):
        return self.main_hero_parameters[num]



def start_game(map_number):
    a = play(rf'data\maps\level_{map_number}.txt', data.main_hero_parameters, data.money)
    time.sleep(0.2)
    print(a)
    time.sleep(0.2)

    data.money = a[1]

    if a[0] == 'exit':
        pygame.quit()
        data.save()
        exit()


class knopka1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = knopka1_img
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, 350)

    def update(self, *args):
        global flag
        
        if args and args[0].type == pygame.MOUSEMOTION and \
                self.rect.collidepoint(args[0].pos):
            self.image = pygame.transform.scale(self.image, (310, 90))
            self.rect = self.image.get_rect()
            self.rect.center = (WIDTH / 2, 350)
        else:
            self.image = knopka1_img
            self.rect = self.image.get_rect()
            self.rect.center = (WIDTH / 2, 350)
            
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                self.rect.collidepoint(args[0].pos):
            flag = 1
            time.sleep(0.2)


class knopka2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = knopka2_img
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, 450)

    def update(self, *args):
        global flag
        if args and args[0].type == pygame.MOUSEMOTION and \
                self.rect.collidepoint(args[0].pos):
            self.image = pygame.transform.scale(self.image, (310, 90))
            self.rect = self.image.get_rect()
            self.rect.center = (WIDTH / 2, 450)
        else:
            self.image = knopka2_img
            self.rect = self.image.get_rect()
            self.rect.center = (WIDTH / 2, 450)
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                self.rect.collidepoint(args[0].pos):
            flag = 2
            time.sleep(0.2)
        

class knopka3(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = knopka3_img
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, 550)

    def update(self, *args):
        global flag
        if args and args[0].type == pygame.MOUSEMOTION and \
                self.rect.collidepoint(args[0].pos):
            self.image = pygame.transform.scale(self.image, (310, 90))
            self.rect = self.image.get_rect()
            self.rect.center = (WIDTH / 2, 550)
        else:
            self.image = knopka3_img
            self.rect = self.image.get_rect()
            self.rect.center = (WIDTH / 2, 550)
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                self.rect.collidepoint(args[0].pos):
            time.sleep(0.2)


class knopka4(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = knopka4_img
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 7, HEIGHT // 2)

    def update(self, *args):
        global flag
        if args and args[0].type == pygame.MOUSEMOTION and \
                self.rect.collidepoint(args[0].pos):
            self.image = pygame.transform.scale(self.image, (185, 260))
            self.rect = self.image.get_rect()
            self.rect.center = (WIDTH // 7, HEIGHT // 2)
        else:
            self.image = knopka4_img
            self.rect = self.image.get_rect()
            self.rect.center = (WIDTH // 7, HEIGHT // 2)
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                self.rect.collidepoint(args[0].pos):

            data.bye(1)


class knopka5(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = knopka5_img
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 7 * 2, HEIGHT // 2)

    def update(self, *args):
        global flag
        if args and args[0].type == pygame.MOUSEMOTION and \
                self.rect.collidepoint(args[0].pos):
            self.image = pygame.transform.scale(self.image, (185, 260))
            self.rect = self.image.get_rect()
            self.rect.center = (WIDTH // 7 * 2, HEIGHT // 2)
        else:
            self.image = knopka5_img
            self.rect = self.image.get_rect()
            self.rect.center = (WIDTH // 7 * 2, HEIGHT // 2)
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                self.rect.collidepoint(args[0].pos):
            data.bye(2)


class knopka6(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = knopka6_img
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 7 * 3, HEIGHT // 2)

    def update(self, *args):
        global flag
        if args and args[0].type == pygame.MOUSEMOTION and \
                self.rect.collidepoint(args[0].pos):
            self.image = pygame.transform.scale(self.image, (185, 260))
            self.rect = self.image.get_rect()
            self.rect.center = (WIDTH // 7 * 3, HEIGHT // 2)
        else:
            self.image = knopka6_img
            self.rect = self.image.get_rect()
            self.rect.center = (WIDTH // 7 * 3, HEIGHT // 2)
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                self.rect.collidepoint(args[0].pos):
            data.bye(3)



class knopka7(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = knopka7_img
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 7 * 4, HEIGHT // 2)

    def update(self, *args):
        global flag
        if args and args[0].type == pygame.MOUSEMOTION and \
                self.rect.collidepoint(args[0].pos):
            self.image = pygame.transform.scale(self.image, (185, 260))
            self.rect = self.image.get_rect()
            self.rect.center = (WIDTH // 7 * 4, HEIGHT // 2)
        else:
            self.image = knopka7_img
            self.rect = self.image.get_rect()
            self.rect.center = (WIDTH // 7 * 4, HEIGHT // 2)
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                self.rect.collidepoint(args[0].pos):
            data.bye(4)



class knopka8(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = knopka8_img
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 7 * 5, HEIGHT // 2)

    def update(self, *args):
        global flag
        if args and args[0].type == pygame.MOUSEMOTION and \
                self.rect.collidepoint(args[0].pos):
            self.image = pygame.transform.scale(self.image, (185, 260))
            self.rect = self.image.get_rect()
            self.rect.center = (WIDTH // 7 * 5, HEIGHT // 2)
        else:
            self.image = knopka8_img
            self.rect = self.image.get_rect()
            self.rect.center = (WIDTH // 7 * 5, HEIGHT // 2)
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                self.rect.collidepoint(args[0].pos):
            data.bye(5)



class knopka9(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = knopka9_img
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 7 * 6, HEIGHT // 2)

    def update(self, *args):
        global flag
        if args and args[0].type == pygame.MOUSEMOTION and \
                self.rect.collidepoint(args[0].pos):
            self.image = pygame.transform.scale(self.image, (185, 260))
            self.rect = self.image.get_rect()
            self.rect.center = (WIDTH // 7 * 6, HEIGHT // 2)
        else:
            self.image = knopka9_img
            self.rect = self.image.get_rect()
            self.rect.center = (WIDTH // 7 * 6, HEIGHT // 2)
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                self.rect.collidepoint(args[0].pos):
            data.bye(6)


class star_world(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = star_world_img
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, 175)


class knopkaout(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = knopkaout_img
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.topright = (WIDTH, 0)

    def update(self, *args):
        global flag
        if args and args[0].type == pygame.MOUSEMOTION and \
                self.rect.collidepoint(args[0].pos):
            self.image = pygame.transform.scale(self.image, (80, 80))
            self.rect = self.image.get_rect()
            self.rect.topright = (WIDTH, 0)
        else:
            self.image = knopkaout_img
            self.rect = self.image.get_rect()
            self.rect.topright = (WIDTH, 0)
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                self.rect.collidepoint(args[0].pos):
            flag = 0


class skrin1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = skrin1_img
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 0)


class knopka11(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = knopka11_img
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 5, HEIGHT // 3)

    def update(self, *args):
        global flag
        if args and args[0].type == pygame.MOUSEMOTION and \
                self.rect.collidepoint(args[0].pos):
            self.image = pygame.transform.scale(self.image, (210, 210))
            self.rect = self.image.get_rect()
            self.rect.center = (WIDTH // 5, HEIGHT // 3)
        else:
            self.image = knopka11_img
            self.rect = self.image.get_rect()
            self.rect.center = (WIDTH // 5, HEIGHT // 3)
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                self.rect.collidepoint(args[0].pos):
            print('I e')
            start_game(1)


class knopka12(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = knopka12_img
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 5 * 2, HEIGHT // 3)

    def update(self, *args):
        global flag
        if args and args[0].type == pygame.MOUSEMOTION and \
                self.rect.collidepoint(args[0].pos):
            self.image = pygame.transform.scale(self.image, (210, 210))
            self.rect = self.image.get_rect()
            self.rect.center = (WIDTH // 5 * 2, HEIGHT // 3)
        else:
            self.image = knopka12_img
            self.rect = self.image.get_rect()
            self.rect.center = (WIDTH // 5 * 2, HEIGHT // 3)
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                self.rect.collidepoint(args[0].pos):
            start_game(2)


class knopka13(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = knopka13_img
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 5 * 3, HEIGHT // 3)

    def update(self, *args):
        global flag
        if args and args[0].type == pygame.MOUSEMOTION and \
                self.rect.collidepoint(args[0].pos):
            self.image = pygame.transform.scale(self.image, (210, 210))
            self.rect = self.image.get_rect()
            self.rect.center = (WIDTH // 5 * 3, HEIGHT // 3)
        else:
            self.image = knopka13_img
            self.rect = self.image.get_rect()
            self.rect.center = (WIDTH // 5 * 3, HEIGHT // 3)
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                self.rect.collidepoint(args[0].pos):
            start_game(3)


class knopka14(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = knopka14_img
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 5 * 4, HEIGHT // 3)

    def update(self, *args):
        global flag
        if args and args[0].type == pygame.MOUSEMOTION and \
                self.rect.collidepoint(args[0].pos):
            self.image = pygame.transform.scale(self.image, (210, 210))
            self.rect = self.image.get_rect()
            self.rect.center = (WIDTH // 5 * 4, HEIGHT // 3)
        else:
            self.image = knopka14_img
            self.rect = self.image.get_rect()
            self.rect.center = (WIDTH // 5 * 4, HEIGHT // 3)
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                self.rect.collidepoint(args[0].pos):
            start_game(4)


class knopka15(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = knopka15_img
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 5, HEIGHT // 3 * 2)

    def update(self, *args):
        global flag
        if args and args[0].type == pygame.MOUSEMOTION and \
                self.rect.collidepoint(args[0].pos):
            self.image = pygame.transform.scale(self.image, (210, 210))
            self.rect = self.image.get_rect()
            self.rect.center = (WIDTH // 5 * 1, HEIGHT // 3 * 2)
        else:
            self.image = knopka15_img
            self.rect = self.image.get_rect()
            self.rect.center = (WIDTH // 5 * 1, HEIGHT // 3 * 2)
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                self.rect.collidepoint(args[0].pos):
            start_game(5)


class knopka16(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = knopka16_img
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 5 * 2, HEIGHT // 3 * 2)

    def update(self, *args):
        global flag
        if args and args[0].type == pygame.MOUSEMOTION and \
                self.rect.collidepoint(args[0].pos):
            self.image = pygame.transform.scale(self.image, (210, 210))
            self.rect = self.image.get_rect()
            self.rect.center = (WIDTH // 5 * 2, HEIGHT // 3 * 2)
        else:
            self.image = knopka16_img
            self.rect = self.image.get_rect()
            self.rect.center = (WIDTH // 5 * 2, HEIGHT // 3 * 2)
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                self.rect.collidepoint(args[0].pos):
            start_game(6)


class knopka17(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = knopka17_img
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 5 * 3, HEIGHT // 3 * 2)

    def update(self, *args):
        global flag
        if args and args[0].type == pygame.MOUSEMOTION and \
                self.rect.collidepoint(args[0].pos):
            self.image = pygame.transform.scale(self.image, (210, 210))
            self.rect = self.image.get_rect()
            self.rect.center = (WIDTH // 5 * 3, HEIGHT // 3 * 2)
        else:
            self.image = knopka17_img
            self.rect = self.image.get_rect()
            self.rect.center = (WIDTH // 5 * 3, HEIGHT // 3 * 2)
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                self.rect.collidepoint(args[0].pos):
            start_game(7)


class knopka18(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = knopka18_img
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 5 * 4, HEIGHT // 3 * 2)

    def update(self, *args):
        global flag
        if args and args[0].type == pygame.MOUSEMOTION and \
                self.rect.collidepoint(args[0].pos):
            self.image = pygame.transform.scale(self.image, (210, 210))
            self.rect = self.image.get_rect()
            self.rect.center = (WIDTH // 5 * 4, HEIGHT // 3 * 2)
        else:
            self.image = knopka18_img
            self.rect = self.image.get_rect()
            self.rect.center = (WIDTH // 5 * 4, HEIGHT // 3 * 2)
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                self.rect.collidepoint(args[0].pos):
            start_game(8)


# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Star world")
clock = pygame.time.Clock()

# настройка папки ассетов
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, r'data\pictures\images_for_menu')

skrin1_img = pygame.image.load(os.path.join(img_folder, 'skrin1.png')).convert()

knopka1_img = pygame.image.load(os.path.join(img_folder, 'knopka1.png')).convert()
knopka2_img = pygame.image.load(os.path.join(img_folder, 'knopka2.png')).convert()
knopka3_img = pygame.image.load(os.path.join(img_folder, 'knopka3.png')).convert()
knopka4_img = pygame.image.load(os.path.join(img_folder, 'knopka4.png')).convert()
knopka5_img = pygame.image.load(os.path.join(img_folder, 'knopka5.png')).convert()
knopka6_img = pygame.image.load(os.path.join(img_folder, 'knopka6.png')).convert()
knopka7_img = pygame.image.load(os.path.join(img_folder, 'knopka7.png')).convert()
knopka8_img = pygame.image.load(os.path.join(img_folder, 'knopka8.png')).convert()
knopka9_img = pygame.image.load(os.path.join(img_folder, 'knopka9.png')).convert()

knopka11_img = pygame.image.load(os.path.join(img_folder, 'knopka11.png')).convert()
knopka12_img = pygame.image.load(os.path.join(img_folder, 'knopka12.png')).convert()
knopka13_img = pygame.image.load(os.path.join(img_folder, 'knopka13.png')).convert()
knopka14_img = pygame.image.load(os.path.join(img_folder, 'knopka14.png')).convert()
knopka15_img = pygame.image.load(os.path.join(img_folder, 'knopka15.png')).convert()
knopka16_img = pygame.image.load(os.path.join(img_folder, 'knopka16.png')).convert()
knopka17_img = pygame.image.load(os.path.join(img_folder, 'knopka17.png')).convert()
knopka18_img = pygame.image.load(os.path.join(img_folder, 'knopka18.png')).convert()

knopkaout_img = pygame.image.load(os.path.join(img_folder, 'knopkaout.png')).convert()
star_world_img = pygame.image.load(os.path.join(img_folder, 'star_world.png')).convert()


skrin1 = skrin1()
knopka1 = knopka1()
knopka2 = knopka2()
knopka3 = knopka3()
knopka4 = knopka4()
knopka5 = knopka5()
knopka6 = knopka6()
knopka7 = knopka7()
knopka8 = knopka8()
knopka9 = knopka9()
knopkaout = knopkaout()
star_world = star_world()
knopka11 = knopka11()
knopka12 = knopka12()
knopka13 = knopka13()
knopka14 = knopka14()
knopka15 = knopka15()
knopka16 = knopka16()
knopka17 = knopka17()
knopka18 = knopka18()

all_sprites = pygame.sprite.Group()
all_sprites.add(skrin1, star_world, knopka1, knopka2, knopka3)

all_sprites2 = pygame.sprite.Group()
all_sprites2.add(skrin1, knopka4, knopka5, knopka6, knopka7, knopka8, knopka9, knopkaout)

all_sprites3 = pygame.sprite.Group()
all_sprites3.add(skrin1, knopka11, knopka12, knopka13, knopka14,
                 knopka15, knopka16, knopka17, knopka18, knopkaout)

# Цикл игры
running = True
data = DataBase()
while running:
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            data.save()
            running = False
    if flag == 0:
        # Обновление
        all_sprites.update(event)
        
        # Рендеринг
        screen.fill(BLACK)
        all_sprites.draw(screen)
        # После отрисовки всего, переворачиваем экран
        pygame.display.flip()
    elif flag == 1:
        font = pygame.font.Font(None, 50)

        # Обновление
        all_sprites2.update(event)
        
        # Рендеринг
        screen.fill(BLACK)
        all_sprites2.draw(screen)

        text = font.render("ур. " + str(data.main_hero_parameters[0]), True, (255, 50, 50))
        screen.blit(text, (WIDTH // 7 - 50, HEIGHT // 2 - 200))
        text = font.render("ур. " + str(data.main_hero_parameters[1]), True, (255, 50, 50))
        screen.blit(text, (WIDTH // 7 * 2 - 50, HEIGHT // 2 - 200))
        text = font.render("ур. " + str(data.main_hero_parameters[2]), True, (255, 50, 50))
        screen.blit(text, (WIDTH // 7 * 3 - 50, HEIGHT // 2 - 200))
        text = font.render("ур. " + str(data.main_hero_parameters[3]), True, (255, 50, 50))
        screen.blit(text, (WIDTH // 7 * 4 - 50, HEIGHT // 2 - 200))
        text = font.render("ур. " + str(data.main_hero_parameters[4]), True, (255, 50, 50))
        screen.blit(text, (WIDTH // 7 * 5 - 50, HEIGHT // 2 - 200))
        text = font.render("ур. " + str(data.main_hero_parameters[5]), True, (255, 50, 50))
        screen.blit(text, (WIDTH // 7 * 6 - 50, HEIGHT // 2 - 200))

        text = font.render("    " + str(prise1), True, (255, 255, 50))
        screen.blit(text, (WIDTH // 7 - 50, HEIGHT // 2 + 150))
        text = font.render("    " + str(prise2), True, (255, 255, 50))
        screen.blit(text, (WIDTH // 7 * 2 - 50, HEIGHT // 2 + 150))
        text = font.render("    " + str(prise3), True, (255, 255, 50))
        screen.blit(text, (WIDTH // 7 * 3 - 50, HEIGHT // 2 + 150))
        text = font.render("    " + str(prise4), True, (255, 255, 50))
        screen.blit(text, (WIDTH // 7 * 4 - 50, HEIGHT // 2 + 150))
        text = font.render("    " + str(prise5), True, (255, 255, 50))
        screen.blit(text, (WIDTH // 7 * 5 - 50, HEIGHT // 2 + 150))
        text = font.render("    " + str(prise6), True, (255, 255, 50))
        screen.blit(text, (WIDTH // 7 * 6 - 50, HEIGHT // 2 + 150))

        text = font.render(str(data.money), True, (255, 255, 0))
        screen.blit(text, (10, 10))
        
        # После отрисовки всего, переворачиваем экран
        pygame.display.flip()
    elif flag == 2:
        # Обновление
        all_sprites3.update(event)
        
        # Рендеринг
        screen.fill(BLACK)
        all_sprites3.draw(screen)
        # После отрисовки всего, переворачиваем экран
        pygame.display.flip()

pygame.quit()


