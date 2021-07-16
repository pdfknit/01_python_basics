def output_bakery(argv):
    if len(argv) == 1:
        with open('bakery.csv', 'r', encoding='utf-8') as f:
            for line in f:
                print(line, end="")
    elif len(argv) == 2:
        with open('bakery.csv', 'r', encoding='utf-8') as f:
            i = 0
            for line in f:
                if i >= int(argv[1]) - 1:
                    print(line, end="")
                i += 1
    elif len(argv) == 3:
        with open('bakery.csv', 'r', encoding='utf-8') as f:
            i = 0
            for line in f:
                if i > int(argv[2]) - 1:
                    break
                if i >= int(argv[1]) - 1:
                    print(line, end="")
                i += 1

    else:
        print(
            'Неверное количество параметров скрипта: 0 - выводи все значения, 1 - выводит значения с заданного номера '
            'строки, 2 - выводит значения в заданном диапазоне')


if __name__ == '__main__':
    import sys

    # output_bakery([1, 3, 15])
    output_bakery(sys.argv)
