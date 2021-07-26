class Worker:
    def __init__(self, name, surname, position, income_dict):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income_dict


class Position(Worker):
    def __init__(self, name, surname, position, income_dict):
        super().__init__(name, surname, position, income_dict)

    def get_full_name(self):
        return f'{self.surname} {self.name}'

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


income_dict = {"wage": 10000, "bonus": 100000}
worker_01 = Position(name='Антон', surname='Аитов', position='менеджер', income_dict=income_dict)
print(worker_01.get_full_name())
print('Доход с учетом премии:', worker_01.get_total_income())
