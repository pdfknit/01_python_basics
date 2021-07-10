def input_bakery(argv):
    with open('bakery.csv', 'a', encoding='utf-8') as f:
        line_to_write = f'{argv[1]}\n'
        f.writelines(line_to_write)


if __name__ == '__main__':
    import sys

    input_bakery(sys.argv)
