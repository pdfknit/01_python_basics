from abc import abstractmethod, ABC


class Cloth(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def calc_consumption(self):
        pass

    def __add__(self, other):
        return round(self.consumption + other.consumption, 3)

    @property
    def consumption(self):
        return self._consumption


class Jacket(Cloth):
    def __init__(self, size):
        if isinstance(size, int):
            self.size = size
            self._consumption = round(self.size / 6.5 + 0.5, 3)
        else:
            raise TypeError('elements is not "int"')


class Costume(Cloth):
    def __init__(self, height):
        if isinstance(height, int):
            self.height = height
            self._consumption = round(self.height * 2 + 0.3, 3)
        else:
            raise TypeError('elements is not "int"')


cloth_01 = Jacket(46)
print('Расход ткани на пальто:', cloth_01.consumption)

cloth_02 = Costume(171)
print('Расход ткани на костюм:', cloth_02.consumption)

print('Расход ткани на костюм и пальто:', cloth_01 + cloth_02)

N = 1000
print(f'Расход ткани на {N} экземпляров: {cloth_02.consumption * N}')
