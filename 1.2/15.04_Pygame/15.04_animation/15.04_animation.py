import os

import pygame

pygame.init()

# Окно игры
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Mario Animation")

# Загрузка спрайтов
sprite_folder = "animations"
sprite_left = [pygame.image.load(os.path.join(sprite_folder, f"l{i}.png")).convert_alpha()
               for i in range(1, 6)]
sprite_right = [pygame.image.load(os.path.join(sprite_folder, f"r{i}.png")).convert_alpha()
                for i in range(1, 6)]
sprite_standing = pygame.image.load(os.path.join(sprite_folder, "0.png")).convert_alpha()

# Переменные
x = 50
y = 410
width = 20
height = 71
vel = 5

is_jump = False
jump_count = 10

left = False
right = False
walk_count = 0

# Создаем объект clock для управления частотой кадров игры
clock = pygame.time.Clock()


def redraw_game_window():
    global walk_count

    # Фон голубого цвета
    screen.fill((0, 191, 255))

    # Рисуем Марио на экране
    if walk_count + 1 >= 15:
        walk_count = 0

    if left:
        screen.blit(sprite_left[walk_count // 3], (x, y))
        walk_count += 1
    elif right:
        screen.blit(sprite_right[walk_count // 3], (x, y))
        walk_count += 1
    else:
        screen.blit(sprite_standing, (x, y))

    # Рисуем дорогу
    pygame.draw.rect(screen, (128, 128, 128), (0, 443, screen_width, screen_height))

    # Обновляем экран
    pygame.display.flip()


# Цикл игры
run = True
while run:
    # Устанавливаем частоту обновления кадров
    clock.tick(27)

    # Проверяем состояние
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Перемещаем Марио влево или вправо при нажатой клавише
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < screen_width - width - vel:
        x += vel
        left = False
        right = True
    else:
        left = False
        right = False
        walk_count = 0

    # Прыжок Марио с помощью пробела, при условии, что он уже не в прыжке
    if not is_jump:
        if keys[pygame.K_SPACE]:
            is_jump = True
            left = False
            right = False
            walk_count = 0

    else:
        if jump_count >= -10:
            neg = 1

            if jump_count < 0:
                neg = -1

            y -= (jump_count ** 2) * 0.5 * neg

            jump_count -= 1

        else:
            is_jump = False

            jump_count = 10

    # Перерисовываем игровое окно с обновленными позициями Марио
    redraw_game_window()

pygame.quit()
