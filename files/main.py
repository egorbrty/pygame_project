from game_main_process import play
from functions import *
import pygame


running = True
clock = pygame.time.Clock()

while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            a = play(r'data\maps\level_1.txt', [100, 100, 25, 200, 100, 900], 100)
            print(a)

            if a[0] == 'exit':
                running = False

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()


