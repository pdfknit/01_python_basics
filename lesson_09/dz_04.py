class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def stop(self):
        return 'Машина остановилась'

    def go(self):
        return 'Машина поехала'

    def turn(self, direction):
        return f'Машина повернула {direction}'

    def show_speed(self):
        return f'Скорость автомобиля: {self.speed}'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        self.is_police = True


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60 and not self.is_police:
            return f'Превышение скорости! Текущая скорость: {self.speed}'
        else:
            return f'Скорость автомобиля: {self.speed}'


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40 and not self.is_police:
            return f'Превышение скорости! Текущая скорость: {self.speed}'
        else:
            return f'Скорость автомобиля: {self.speed}'


car_01 = PoliceCar(80, 'Синий', 'Ford', True)
print(car_01.color, car_01.name, car_01.show_speed())
print(car_01.stop())
print(car_01.go())
print(car_01.turn('налево'))

car_02 = TownCar(80, 'Зеленый', 'Ford', True)
print(car_02.color, car_02.name, car_02.show_speed())
print(car_02.stop())
print(car_02.go())
print(car_02.turn('направо'))

car_03 = WorkCar(44, 'Красный', 'Ford', False)
print(car_03.color, car_03.name, car_03.show_speed())

car_04 = WorkCar(36, 'Пурпурный', 'Ford', False)
print(car_04.color, car_04.name, car_04.show_speed())
