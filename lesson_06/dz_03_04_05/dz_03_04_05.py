import json


def parsing(**kwargs):
    try:
        names_f = kwargs['names_f']
    except:
        names_f = 'user.csv'
    try:
        hobby_f = kwargs['hobby_f']
    except:
        hobby_f = 'hobby.csv'
    try:
        result_f = kwargs['result_f']
    except:
        result_f = 'result.json'

    all_names = {}
    with open(names_f, 'r', encoding='utf-8') as names_file:
        with open(hobby_f, 'r', encoding='utf-8') as hobby_file:
            for name in names_file:
                hobby = hobby_file.readline()
                result_name = name.strip("\n").replace(",", " ")
                if hobby:
                    result_hobby = hobby.strip("\n").replace(",", ", ")
                else:
                    result_hobby = None
                all_names[result_name] = result_hobby
            if hobby_file.readline():
                print('Выход: Ошибка 1')
                exit(1)

            with open(result_f, 'w', encoding='utf-8') as result_file:
                json.dump(all_names, result_file, ensure_ascii=False)

            with open(result_f, 'r', encoding='utf-8') as result_file:
                result = json.load(result_file)


if __name__ == '__main__':
    import sys

    # Формат ввода параметров в консоли: names_f=путь_к_файлу (файл с именами), hobby_f=путь_к_файлу (файл с хобби),
    # result_f=путь_к_файлу(куда записать результаты). Пустые параметры запишут файлы в папку скрипта
    parsing(**dict(arg.split('=') for arg in sys.argv[1:]))
