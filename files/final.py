from functions import *
from pause import Button


yyy = 0
z1 = -120
z3 = 120
k = 62
k4 = 10
# настройка папки ассетов

class You_win(pygame.sprite.Sprite):
    def __init__(self):
        self.you_win_img = pygame.image.load(r'data\pictures\images_for_win\you_win.png').convert()

        pygame.sprite.Sprite.__init__(self)
        self.image = self.you_win_img
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (width // 2, 50)
        
    def update(self, result):
        star_res(result, width // 2, 50, 50, 7)


def star_res(result, k1, k2, k3, number):
    global YELLOW, BLACK2, z1, z3, k, k4
    r = 3
    st1, st2, st3 = result

    if st1 == 0:
        color1 = BLACK2
    else:
        color1 = YELLOW
    if st2 == 0:
        color2 = BLACK2
    else:
        color2 = YELLOW
    if st3 == 0:
        color3 = BLACK2
    else:
        color3 = YELLOW
    star_points1 = [(16.5 * r + k1 - k + z1, 15.1 * r + k2 + k3),
                    (20.0 * r + k1 - k + z1, 2.0 * r + k2 + k3),
                    (23.5 * r + k1 - k + z1, 15.1 * r + k2 + k3),
                    (37.1 * r + k1 - k + z1, 14.4 * r + k2 + k3),
                    (25.7 * r + k1 - k + z1, 21.9 * r + k2 + k3),
                    (30.6 * r + k1 - k + z1, 34.6 * r + k2 + k3),
                    (20.0 * r + k1 - k + z1, 26.0 * r + k2 + k3),
                    (9.4 * r + k1 - k + z1, 34.6 * r + k2 + k3),
                    (14.3 * r + k1 - k + z1, 21.9 * r + k2 + k3),
                    (2.9 * r + k1 - k + z1, 14.4 * r + k2 + k3)]
    pygame.draw.polygon(screen, color1, star_points1)
    star_points2 = [(16.5 * r + k1 - k, 15.1 * r + k2 + k3 - k4),
                    (20.0 * r + k1 - k, 2.0 * r + k2 + k3 - k4),
                    (23.5 * r + k1 - k, 15.1 * r + k2 + k3 - k4),
                    (37.1 * r + k1 - k, 14.4 * r + k2 + k3 - k4),
                    (25.7 * r + k1 - k, 21.9 * r + k2 + k3 - k4),
                    (30.6 * r + k1 - k, 34.6 * r + k2 + k3 - k4),
                    (20.0 * r + k1 - k, 26.0 * r + k2 + k3 - k4),
                    (9.4 * r + k1 - k, 34.6 * r + k2 + k3 - k4),
                    (14.3 * r + k1 - k, 21.9 * r + k2 + k3 - k4),
                    (2.9 * r + k1 - k, 14.4 * r + k2 + k3 - k4)]
    pygame.draw.polygon(screen, color2, star_points2)
    star_points3 = [(16.5 * r + k1 - k + z3, 15.1 * r + k2 + k3),
                    (20.0 * r + k1 - k + z3, 2.0 * r + k2 + k3),
                    (23.5 * r + k1 - k + z3, 15.1 * r + k2 + k3),
                    (37.1 * r + k1 - k + z3, 14.4 * r + k2 + k3),
                    (25.7 * r + k1 - k + z3, 21.9 * r + k2 + k3),
                    (30.6 * r + k1 - k + z3, 34.6 * r + k2 + k3),
                    (20.0 * r + k1 - k + z3, 26.0 * r + k2 + k3),
                    (9.4 * r + k1 - k + z3, 34.6 * r + k2 + k3),
                    (14.3 * r + k1 - k + z3, 21.9 * r + k2 + k3),
                    (2.9 * r + k1 - k + z3, 14.4 * r + k2 + k3)]
    pygame.draw.polygon(screen, color3, star_points3)


def show_window(result):
    window_buttons = pygame.sprite.Group()
    exit_button = Button(window_buttons, 'data/pictures/exit.png', (width * 0.4, height * 0.7))
    replay_button = Button(window_buttons, 'data/pictures/replay.png', (width * 0.6, height * 0.7))

    window_buttons.add(exit_button)
    window_buttons.add(replay_button)

    clock = pygame.time.Clock()
    you_win = You_win()

    all_sprites = pygame.sprite.Group()
    all_sprites.add(you_win)

    # Цикл игры
    running = True

    while running:
        clock.tick(fps)
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'exit'
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                click = True
    
        # Рендеринг
        screen.fill(BLACK)
        all_sprites.draw(screen)
        # Обновление
        all_sprites.update(result)
        # После отрисовки всего, переворачиваем экран

        mouse_pos = pygame.mouse.get_pos()

        window_buttons.update(mouse_pos)
        window_buttons.draw(screen)

        if click and exit_button.rect.collidepoint(mouse_pos):
            return 'menu'
        elif click and replay_button.rect.collidepoint(mouse_pos):
            return 'replay'

        pygame.display.flip()


