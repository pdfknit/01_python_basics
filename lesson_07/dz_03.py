import os
import shutil

PATH = "F:\Sonya\GeekBrains\\01_python_basics\lesson_07\my_project"
TO_PATH = 'F:\Sonya\GeekBrains\\01_python_basics\lesson_07\\templates'
try:
    for root, dirs, files in os.walk(PATH):
        if 'templates' in dirs:
            subfolder_path = os.path.join(root, 'templates')
            for root2, dirs2, files2 in os.walk(subfolder_path):
                for dir_to_copy in dirs2:
                    path_to_copy = os.path.join(root2, dir_to_copy)
                    shutil.copytree(path_to_copy, os.path.join(TO_PATH, dir_to_copy))
                # прохожусь по файлам внутри папки templates без подпапки
                for file_to_copy in files2:
                    if dirs2:
                        file_path = os.path.join(root2, file_to_copy)
                        path_for_files = os.path.join(TO_PATH, dirs2[0])
                        shutil.copy(file_path, TO_PATH, follow_symlinks=True)

except FileExistsError:
    print('Невозможно перенести файлы в папку с шаблонами, так как они уже существуют')
