import yaml
import os

MAIN_FOLDER = r'F:\Sonya\GeekBrains\01_python_basics\lesson_07'
FILE = "dz_01.yaml"


def create_folder(f_path, f_name):  # создаю папку
    abs_f_name = os.path.join(f_path, f_name)
    if not os.path.exists(abs_f_name):
        os.mkdir(abs_f_name)
    return abs_f_name


def create_file(f_path, f_name):  # создаю файл
    with open(os.path.join(f_path, f_name), 'w', encoding='utf-8') as f:
        f.write('')


def is_it_folder(folder_list, path):
    if isinstance(folder_list, dict):
        for dir_name in folder_list.keys():
            abs_folder_path = create_folder(path, dir_name)
            # проверка, что корневая папка не пустая
            if folder_list.get(dir_name) == None:
                continue
            else:
                for name in folder_list[dir_name]:
                    # проверяю строка ли, создаю файл
                    if isinstance(name, str):
                        create_file(abs_folder_path, name)

                    elif isinstance(name, dict):
                        for key, item in name.items():
                            if item != None:
                                new_path = os.path.join(abs_folder_path, key)
                                is_it_folder(name, abs_folder_path)
                            create_folder(abs_folder_path, key)  # создаю пустую папку
                    elif isinstance(folder_list, list):
                        create_folder(path, dir_name)


# выбираем директорию и открываем файл с конфигурацией папок

with open(FILE, 'r', encoding='utf-8') as f:
    folder_list = yaml.safe_load(f)

is_it_folder(folder_list, MAIN_FOLDER)
