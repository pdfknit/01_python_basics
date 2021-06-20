cube_list = []
# список из кубов
for i in range(1, 1001):
    if (i % 2) == 1:
        cube_list.append(i ** 3)

# а) Проверка делимого на 7
result_a = 0
for digit in cube_list:
    current_digit = str(digit)
    current_summ = 0
    for i in current_digit:
        current_summ += int(i)
    if current_summ % 7 == 0:
        result_a += int(current_digit)

# b) Прибавляю 17 и проверяю делимое на 7
result_b = 0
for digit in cube_list:
    current_digit = str(digit + 17)
    current_summ = 0
    for i in current_digit:
        current_summ += int(i)
    if current_summ % 7 == 0:
        result_b += int(current_digit)
print('Список кубов нечетных чисел:\n', cube_list)
print('\nСумма чисел из пункта a:', result_a)
print('Сумма чисел из пункта b:', result_b)


