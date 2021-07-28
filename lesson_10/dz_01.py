class Matrix:
    def __init__(self, matrix_num):
        self.matrix = matrix_num
        length = []
        for stroke in self.matrix:
            n = 0
            for digit in stroke:
                if not isinstance(digit, int) and not isinstance(digit, float):
                    raise TypeError('elements is not "int" or "float"')
                n += 1
            length.append(n)
        for index, digit in enumerate(length):
            if length[index] != length[index - 1]:
                raise ValueError('all lines must contain same numbers of digits')


    def __str__(self):
        string_to_print = ''
        for stroke in self.matrix:
            for digit in stroke:
                string_to_print += f'{digit:>7}'
            string_to_print += '\n'
        return string_to_print


numbers = [[10, 10, 10, 10], [13, 13, 13, 13], [12, 123, 13, 13]]
matrix_01 = Matrix(numbers)
print(matrix_01)
