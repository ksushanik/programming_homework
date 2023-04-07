n = int(input('Введите количество городов (0 ≤ N ≤ 100): '))

arr = []
for i in range(n):
    arr.append(list(map(int, input(f"Введите через пробел {i+1} строку матрицы: ").split())))

total = 0
for el in arr:
    total += sum(el)

print('Количество дорог на планете: ', int(total / 2))
