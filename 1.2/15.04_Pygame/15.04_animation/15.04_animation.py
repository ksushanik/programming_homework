import pygame
import os

# Инициализация Pygame
pygame.init()

# Окно игры
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Mario Animation")

# Загрузка спрайтов
sprite_folder = "animations"
sprite_left = [pygame.image.load(os.path.join(sprite_folder, f"l{i}.png")).convert_alpha() for i in range(1, 6)]
sprite_right = [pygame.image.load(os.path.join(sprite_folder, f"r{i}.png")).convert_alpha() for i in range(1, 6)]
sprite_standing = [pygame.image.load(os.path.join(sprite_folder, "0.png")).convert_alpha()]

# Состояние персонажа
state_standing = "standing"
state_left = "left"
state_right = "right"

# Состояние анимации
animation_state = state_standing
animation_frames = sprite_standing
animation_frame_index = 0
animation_tick = 0
animation_speed = 10

# Координаты Марио
x = screen_width // 2
y = screen_height // 2

# Скорость движения Марио
speed = 5

# Цикл игры
running = True
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                animation_state = state_left
                animation_frames = sprite_left
                animation_frame_index = 0
                x -= speed  # изменение координаты x при нажатии на клавишу "влево"
            elif event.key == pygame.K_RIGHT:
                animation_state = state_right
                animation_frames = sprite_right
                animation_frame_index = 0
                x += speed  # изменение координаты x при нажатии на клавишу "вправо"

    # Очистка экрана
    screen.fill((0, 0, 0))

    # Отображение кадра анимации
    current_frame = animation_frames[animation_frame_index]
    screen.blit(current_frame, (x - current_frame.get_width() / 2, y - current_frame.get_height() / 2))

    # Обновление состояния анимации
    animation_tick += 1
    if animation_tick >= animation_speed:
        animation_frame_index += 1
        if animation_frame_index >= len(animation_frames):
            animation_frame_index = 0
        animation_tick = 0

    # Обновление экрана
    pygame.display.flip()

# Завершение Pygame
pygame.quit()
