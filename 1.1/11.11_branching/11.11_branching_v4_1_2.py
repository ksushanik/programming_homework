def is_valid_triangle(a, b, c):
    if a + b <= c or a + b <= c or b + c <= a:
        return False
    return True

a = int(input('Введите a: ')) 
b = int(input('Введите b: ')) 
c = int(input('Введите c: '))

print(('NO', 'YES')[is_valid_triangle(a, b, c)])