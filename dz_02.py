cube_list = []
# список из кубов
for i in range(1, 1001, 2):
    cube_list.append(i ** 3)

# а) Проверка делимого на 7
result_a = 0
for i, current_digit in enumerate(cube_list):
    current_summ = 0
    while current_digit > 0:
        current_summ += current_digit % 10
        print('current_summ', current_summ)
        current_digit = current_digit // 10
    print("current_digit", current_digit)
    print('current_summ', current_summ)

    if current_summ % 7 == 0:
        result_a += int(cube_list[i])

# b) Прибавляю 17 и проверяю делимое на 7
result_b = 0
for i, current_digit in enumerate(cube_list):
    current_summ = 0
    current_digit+=17
    while current_digit > 0:
        current_summ += current_digit % 10
        print('current_summ', current_summ)
        current_digit = current_digit // 10
    print("current_digit", current_digit)
    print('current_summ', current_summ)

    if current_summ % 7 == 0:
        result_b += int(cube_list[i])+17

print('Список кубов нечетных чисел:\n', cube_list)
print('\nСумма чисел из пункта a:', result_a)
print('Сумма чисел из пункта b:', result_b)


