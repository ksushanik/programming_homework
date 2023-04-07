import turtle

from PIL import Image

# Задание размера квадратов
square_size = 5

# Загрузка изображения
image = "jocker.jpg"
img = Image.open(image)

# Изменение размера изображения до кратного размера квадрата
width, height = img.size
width = (width // square_size) * square_size
height = (height // square_size) * square_size
img = img.resize((width, height))

# Получение данных о пикселях
pixels = list(img.getdata())

# Создание списка координат квадратов и их цветов
square_data = []
for y in range(0, height, square_size):
    for x in range(0, width, square_size):
        # Получение цвета верхнего левого пикселя в квадрате
        r, g, b = pixels[y * width + x]
        square_data.append(((x - width / 2, height / 2 - y), (r / 255, g / 255, b / 255)))

# Создание окна черепахи
window = turtle.Screen()

# Создание черепахи
t = turtle.Turtle()
t.speed(0)

# Установка размера черепахи равным размеру квадрата
t.shapesize(square_size / 100, square_size / 100)

# Отрисовка квадратов черепахой
for coord, color in square_data:
    t.penup()
    t.goto(coord)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    for i in range(4):
        t.forward(square_size)
        t.left(90)
    t.end_fill()

# Закрытие окна черепахи
window.exitonclick()
