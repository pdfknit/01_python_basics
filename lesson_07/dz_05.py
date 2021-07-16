import os

PATH = "F:\Sonya\GeekBrains\\01_python_basics"
all_sizes = {100: [0, []], 1000: [0, []], 10000: [0, []], 100_000: [0, []], 1_000_000: [0, []], 10_000_000: [0, []]}
i = 0
all_file_extensions = []
for root, dirs, files in os.walk(PATH):
    for file in files:
        f_path = os.path.join(root, file)
        size = os.stat(f_path).st_size

        if len(file.split('.')) == 1:
            file_extension = 'no.format'
        else:
            file_extension = file.split('.')[-1]

        if size > 10_000_000:
            all_file_extensions = all_sizes[10_000_000][1]
            all_file_extensions.append(file_extension)
            all_sizes[10_000_000] = [all_sizes[10_000_000][0] + 1, all_file_extensions]

        else:
            for template_size in all_sizes.keys():
                if size < template_size:
                    all_file_extensions = all_sizes[template_size][1]
                    all_file_extensions.append(file_extension)

                    all_sizes[template_size][0] = all_sizes[template_size][0] + 1
                    break
for key, cur_size in all_sizes.items():
    all_sizes[key][1] = tuple(set(all_sizes[key][1]))
print(all_sizes)
result_sum = 0

for key in all_sizes.keys():
    result_sum += all_sizes[key][0]
print('Общее количество файлов в папке, записанных с словарь с результатом:', result_sum)
