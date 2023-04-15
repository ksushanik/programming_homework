"""
1. Написать программу, которая будет писать в консоль названия нажатых клавиш.
Реализовать поддержку enter, space, w, a, s, d, esc, стрелок.
"""
import pygame

# инициализация Pygame
pygame.init()

# создание окна
window = pygame.display.set_mode((400, 400))

# основной цикл программы
while True:
    # обработка событий
    for event in pygame.event.get():
        # проверка на нажатие клавиши
        if event.type == pygame.KEYDOWN:
            # получение названия клавиши
            key_name = pygame.key.name(event.key)
            print(key_name)

            # проверка на выход
            if event.key == pygame.K_ESCAPE:
                print("Нажмите клавишу Q для выхода из программы")

        # проверка на нажатие клавиши Q для выхода из программы
        elif event.type == pygame.KEYUP and event.key == pygame.K_q:
            pygame.quit()
            quit()
