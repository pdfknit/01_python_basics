file = open('nginx_logs.txt', 'r', encoding='utf-8')
count = 0
spamer = {}
for line in file:
    line_data_01 = line.strip("\n").split(" - - ")
    line_data_02 = line_data_01[1].split(' ')
    line_data = (line_data_01[0], line_data_02[2].replace('"', ''), line_data_02[3])

    if line_data[0] not in spamer.keys():
        spamer[line_data[0]] = 1
    else:
        count = spamer[line_data[0]]
        spamer[line_data[0]] = count + 1

previous_max = 0
for ip, count_get in spamer.items():
    if count_get > previous_max:
        result = (ip, count_get)
        previous_max = count_get
    else:
        pass
print(result)
file.close()
