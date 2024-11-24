number = int(input(f'Введите число от 3 до 20: '))
if number > 2 and number < 21:
    for elem in [number]:
        password = []
    for x in range(1, elem):
        for y in range(x + 1, elem):
            if elem % (x + y) == 0:
                password += x, y
    print('Ваш пароль: ', *password)
else:
    print('Вы ввели неверное число, введите другое.')

