input_list = [57.321, 16.56, 44.2, 97, 45.1, 18.45, 15.6]

unsorted_id = id(input_list)
string_for_print = ''

print('Задание А. Список цен по формату')
for i, item in enumerate(input_list):
    rub = int(item // 1)
    kop = int((item % 1) * 101)  # проверить выражение, некоторые числа меньше на 1
    input_list[i] = f'{rub} руб {kop:02d} коп'
print(", ".join(input_list))


#     string_for_print += f'{rub} руб {kop:02d} коп, '
# print(string_for_print.strip(', '))

print('\nЗадание В. Сортировка в порядке возрастания')

input_list.sort()
print(", ".join(input_list))
sorted_id = id(input_list)

#доказательство идентичных списков
if unsorted_id == sorted_id:
    print(f'\nID сортированного и несортироавнного списка равны = {sorted_id}. Значит, объект остался тот же.')

#Задание C. Без вывода инфы

string_for_print = ''
reversed_list = sorted(input_list, reverse=True)

#Задание D. 5 самых дорогих товара. По возможности, минимум кода
print('\nЗадание D. 5 самых дорогих товаров:', ", ".join(reversed_list[:5]))

