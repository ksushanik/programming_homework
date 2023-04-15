import pygame

# Инициализация Pygame
pygame.init()

# Создание экрана
screen = pygame.display.set_mode((300, 300))

# Задание начальной позиции квадрата
x = 145
y = 145

# Задание начального цвета квадрата и списка цветов
colors = [(255, 0, 0), (255, 165, 0), (255, 255, 0), (0, 128, 0), (0, 0, 255), (75, 0, 130), (238, 130, 238)]
color_index = 0
color = colors[color_index]

# Задание начальной ширины и высоты квадрата
width = 10
height = 10

# Задание начальной скорости квадрата
speed = 5

# Главный цикл программы
while True:
    # Обработка событий Pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            # Обработка нажатий клавиш
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
            elif event.key == pygame.K_w or event.key == pygame.K_UP:
                y = max(y - speed, 0)
            elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                x = max(x - speed, 0)
            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                y = min(y + speed, screen.get_height() - height)
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                x = min(x + speed, screen.get_width() - width)
            elif event.key == pygame.K_c:
                # Смена цвета квадрата по нажатию клавиши "c"
                color_index = (color_index + 1) % len(colors)
                color = colors[color_index]

    # Очистка области, занимаемой квадратом на предыдущем кадре
    pygame.draw.rect(screen, (0, 0, 0), (x, y, width, height))

    # Отрисовка следа квадрата
    pygame.draw.rect(screen, color, (x, y, width, height))

    # Обновление экрана
    pygame.display.update()
