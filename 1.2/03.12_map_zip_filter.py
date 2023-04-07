# 1. Удвоить каждый элемент коллекции.

collection = list(range(1, 11))
print(collection)
result = list(map(lambda x: x*2, collection))
print(result)

# 2. Найти произведение по-элементно элементов из трех коллекций.

a = [1, 3, 5]
b = [2, 4, 6]
c = [3, 5, 7]

result = [x * y * z for x, y, z in zip(a, b, c)]
print(result)

# 3. Найти длину каждого элемента из коллекции.

collection = ['apple', 'orange', 'banana', [1, 2, 3]]
result = list(map(len, collection))
print(result)

# 3. Оставить только непустые элементы коллекции.

collection = [0, 1, 'Hello', '', None, [], [1,2,3], 0.1, 0.0]
print(list(filter(lambda x: x or x == 0, collection)))

# 4. Оставить только четные элементы коллекции.

collection = range(10, 30)
result = list(filter(lambda x: x % 2 == 0, collection))
print(result)

# 5. Есть три коллекции, нужно упаковать элементы тройками.

a = [1, 3, 5, 7, 9]
b = [0, 2, 4, 6, 8]
c = ['a', 'b', 'c', 'd', 'e']
result = list(zip(a, b, c))
print(result)

# 7. Есть две коллекции, нужно упаковать элементы двойками при этом элементы второй коллекции должны быть удвоенны.

a = [7, 5, 9]
b = [3, 6, 8]

result = list(zip(a, map(lambda x: x * 2, b)))
print(result)
