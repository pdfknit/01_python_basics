import os

PATH = "F:\Sonya\GeekBrains\\01_python_basics\\venv"
all_sizes = {100: 0, 1000: 0, 10000: 0, 100_000: 0, 1_000_000: 0, 10_000_000: 0}
i = 0
for root, dirs, files in os.walk(PATH):
    for file in files:
        f_path = os.path.join(root, file)
        size = os.stat(f_path).st_size
        file_extension = file.split('.')[-1]
        # print(file, file_extension, size)

        if size > 10_000_000:
            all_sizes[10_000_000] = all_sizes[10_000_000] + 1

        else:
            for template_size in all_sizes.keys():
                if size < template_size:
                    all_sizes[template_size] = all_sizes[template_size] + 1
                    break
print(all_sizes)
result_sum = 0
for count in all_sizes.values():
    result_sum += count
print(result_sum)
