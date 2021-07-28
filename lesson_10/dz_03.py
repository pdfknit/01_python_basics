class Multicellular:
    def __init__(self, cell):

        if isinstance(cell, int):
            self.cell = cell
        else:
            raise ValueError('Count of cell must be "int"')

    def __add__(self, other):
        return Multicellular(self.cell + other.cell)

    def __sub__(self, other):
        if self.cell > other.cell:
            return Multicellular(self.cell - other.cell)
        else:
            raise ValueError("can't sub for A < B")

    def __mul__(self, other):
        return Multicellular(self.cell * other.cell)

    def __truediv__(self, other):
        return Multicellular(self.cell // other.cell)

    def __str__(self):
        return str(self.cell)

    def make_order(self, cell_in_line):

        if not isinstance(cell_in_line, int):
            raise ValueError('cell_in_line must be "int"')

        result = []
        tale = self.cell % cell_in_line

        for cell in range(self.cell // cell_in_line):
            for line in range(0, cell_in_line):
                result.append('*')
            result.append('/n')

        if tale == 0:
            result.pop()
        else:
            for cell in range(0, tale):
                result.append('*')
        return ''.join(result)


cell_01 = Multicellular(3)
print('cell_01', cell_01)
cell_02 = Multicellular(15)
print('cell_02', cell_02)
print('add', cell_01 + cell_02)
# print('sub', cell_01-cell_02)
print('sub', cell_02 - cell_01)
print('mul', cell_02 * cell_01)
print('div', cell_02 / cell_01)
print(cell_02.make_order(6))
print(cell_02.make_order(5))
print(cell_01.make_order(6))
