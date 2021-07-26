class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return "Запуск отрисовки"


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return "Рисую ручкой"


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return "Рисую карандашом"


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return "Рисую маркером"


skrepka = Stationery('Скрепка')
print(skrepka.title, skrepka.draw())

pen_01 = Pen('Ручка')
print(pen_01.title, pen_01.draw())

pencil_01 = Pencil('Карандаш')
print(pencil_01.title, pencil_01.draw())

handle_01 = Handle('Маркер')
print(handle_01.title, handle_01.draw())
