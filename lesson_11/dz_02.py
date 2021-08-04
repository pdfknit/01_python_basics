class ZeroDivision(Exception):
    pass


try:
    digit = input('Введите a/b')
    digit_list = [int(cur_digit) for cur_digit in digit.split('/')]
    if digit_list[1] == 0:
        raise ZeroDivision('Делитель не должен быть равен нулю')
except ZeroDivision:
    print('Делитель не должен быть равен нулю')
else:
    print(f'{digit_list[1]} / {digit_list[0]} = {digit_list[1] / digit_list[0]}')
