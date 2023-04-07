a = int(input('Введите a: '))
b = int(input('Введите b: '))

if (a ==  b == 0):
    print('INF')
elif (a == 0 or (b % a) != 0):
    print('NO')
else: 
    print(int(-b / a))