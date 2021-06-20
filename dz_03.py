# TODO: склонение слова процент

count = int(input('Введите число от 0 до 20\n'))
while count >= 0 and count <= 20:

    if count == 1:
        print(count, 'процент')
        count = int(input('Введите число от 0 до 20\n'))

    elif count in range(2, 4):
        print(count, 'процента')
        count = int(input('Введите число от 0 до 20\n'))

    else:
        print(count, 'процентов')
        count = int(input('Введите число от 0 до 20\n'))

print('Число больше 20 или меньше 0. Программа завершена')
