class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def weight(self):
        weight_1m2 = 25
        thick = 0.05
        weight_of_road = self._length * self._width * weight_1m2 * thick
        return int(weight_of_road)


road_to_ekb = Road(5000, 20)
print(f'Масса дороги: {road_to_ekb.weight()} т.')
