a = int(input('Введите число A: '))
i = 2
res = 0
fib_prev = 1
fib_prev_prev = 0
fib = fib_prev_prev + fib_prev
while a >= fib:
    if a == fib:
        res = i
        break
    i += 1
    fib_prev_prev = fib_prev
    fib_prev = fib
    fib = fib_prev_prev + fib_prev
if res:
    print(f'n={res}')
else:
    print("-1")