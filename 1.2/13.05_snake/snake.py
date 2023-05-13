import random
import sys
import tkinter as tk
from tkinter import messagebox

import pygame

# Инициализация PyGame
pygame.init()

# Определение размеров и цветов
cell_size = 10
cell_number = 100
background_color = (0, 0, 0)
snake_color = (0, 255, 0)
apple_color = (255, 0, 0)

# Загрузка звуков и музыки
eat_sound = pygame.mixer.Sound("eat.wav")
crash_sound = pygame.mixer.Sound("crash.wav")
pygame.mixer.music.load("background_music.mp3")
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)

# Создание окна
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
pygame.display.set_caption("Snake Game")

# Создание змейки и яблока
snake_pos = [[50, 50], [40, 50], [30, 50]]
apple_pos = [random.randrange(1, cell_number) * cell_size, random.randrange(1, cell_number) * cell_size]
snake_speed = 10
snake_direction = pygame.K_RIGHT


# Отображение сообщения об окончании игры
def game_over():
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Game Over", "You crashed into the wall!")
    root.destroy()


# Основной игровой цикл
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT):
                snake_direction = event.key

    # Обновление позиции змейки
    x, y = snake_pos[0]
    if snake_direction == pygame.K_UP:
        y -= cell_size
    elif snake_direction == pygame.K_DOWN:
        y += cell_size
    elif snake_direction == pygame.K_LEFT:
        x -= cell_size
    elif snake_direction == pygame.K_RIGHT:
        x += cell_size
    snake_pos.insert(0, [x, y])

    # Проверка столкновения со стеной
    if x < 0 or x >= cell_number * cell_size or y < 0 or y >= cell_number * cell_size:
        crash_sound.play()
        game_over()
        pygame.quit()
        sys.exit()

    # Проверка столкновения с яблоком
    if snake_pos[0] == apple_pos:
        eat_sound.play()
        apple_pos = [random.randrange(1, cell_number) * cell_size, random.randrange(1, cell_number) * cell_size]
    else:
        snake_pos.pop()

    # Отрисовка змейки и яблока
    screen.fill(background_color)
    for pos in snake_pos:
        pygame.draw.rect(screen, snake_color, pygame.Rect(pos[0], pos[1], cell_size, cell_size))
    pygame.draw.rect(screen, apple_color, pygame.Rect(apple_pos[0], apple_pos[1], cell_size, cell_size))

    pygame.display.flip()
    pygame.time.Clock().tick(snake_speed)
