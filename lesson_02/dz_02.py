input_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
i = 0

while i < len(input_list):
    if (input_list[i].isdigit() == True) or ('+' in input_list[i]):
        input_list.insert(i, '"')
        input_list.insert(i + 2, '"')

        if '+' in input_list[i + 1]:
            input_list[i + 1] = f'+{int(input_list[i + 1]):02d}'
        else:
            input_list[i + 1] = f'{int(input_list[i + 1]):02d}'
        i += 3
    else:
        i += 1

string_to_print = ' '.join(input_list)
print(string_to_print)
result = ''
j = 0
i = 0
index_list = []
while i < len(string_to_print)+1:
    index_01 = string_to_print.find('"', i)
    if index_01 == -1:
        index_list.append(len(string_to_print))
        break
    else:
        i = index_01 + 1
    index_list.append(index_01)

new_string = ''
for i in range(0, len(index_list)-1):
    if i % 2 == 0:
        new_string += string_to_print[index_list[i]:index_list[i + 1]].replace(' ', '')
    else:
        new_string += string_to_print[index_list[i]:index_list[i + 1]]
print(new_string)
