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
speed = 0.05
x_change = 0
y_change = 0
is_falling = False

# Дорога
road_width = 400
road_height = 50
road_color = (100, 100, 100)
road_x = screen_width // 2 - road_width // 2
road_y = screen_height - road_height

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
                x_change = -speed  # изменение координаты x при нажатии на клавишу "влево"
            elif event.key == pygame.K_RIGHT:
                animation_state = state_right
                animation_frames = sprite_right
                animation_frame_index = 0
                x_change = speed  # изменение координаты x при нажатии на клавишу "вправо"
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0
                animation_state = state_standing
                animation_frames = sprite_standing
                animation_frame_index = 0

    # Проверка на выход Марио за границы дороги
    if x < road_x or x > road_x + road_width:
        is_falling = True

    # Падение Марио
    if is_falling:
        y_change += 0.1
        y += y_change

        if y > screen_height:
            running = False
    else:
        # Изменение координат Марио
        x += x_change

    # Очистка экрана
    screen.fill((0, 0, 0))

    # Отображение дороги
    pygame.draw.rect(screen, road_color, (road_x, road_y, road_width, road_height))

    # Отображение кадра анимации
    current_frame = animation_frames[animation_frame_index]
    screen.blit(current_frame, (x - current_frame.get_width() / 2, road_y - current_frame.get_height()))

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