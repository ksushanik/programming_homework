corr=False
while not corr:
    try:
        x=int(input('Введите 1-ое число: '))
        y=int(input('Введите 2-ое число: '))
        corr=True
    except TypeError:
        print('Не число, попробуйт снова: ')
corrop=False
while not corrop:
    try:
        op=str(input('Введите операцию: '))
        if op in ['+', '-', '*', '/', '//', '%']:
            corrop=True
        else:
            raise 'Ошибка'
    except Exception:
        print('Не операция, попробуйте снова: ')
        res=0
    if op=='+':
        res=x+y
        print(f'Ответ: {res}')
    elif op=='-':
        res=x-y
        print(f'Ответ: {res}')
    elif op=='*':
        res=x*y
        print(f'Ответ: {res}')
    elif op=='/':
        res=x/y
        print(f'Ответ: {res}')
    elif op=='//':
        res=x//y
        print(f'Ответ: {res}')
    elif op=='%':
        res=x%y
        print(f'Ответ: {res}')