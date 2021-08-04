class NoEqupmentError(Exception):
    pass


class Storage:
    def __init__(self):
        self.count_of_officeequipment = 0
        self.total_cost = 0
        self.all_models = {}

    def get_equipment(self, equipment, count):
        self.total_cost += float(equipment.price)
        self.count_of_officeequipment += self._validator_for_int(count)
        class_of_eq = equipment.__class__.__name__

        try:
            self.all_models[class_of_eq][f"{equipment.brand} {equipment.model}"] += count

        except:
            try:
                self.all_models[class_of_eq][f"{equipment.brand} {equipment.model}"] = count
            except:
                self.all_models[class_of_eq] = {}
                self.all_models[class_of_eq][f"{equipment.brand} {equipment.model}"] = count

    def send_equipment(self, equipment, count, department):
        class_of_eq = equipment.__class__.__name__
        try:
            result_count = self.all_models[class_of_eq][f"{equipment.brand} {equipment.model}"] - count
            if result_count < 1:
                raise NoEqupmentError
            else:
                self.all_models[class_of_eq][f"{equipment.brand} {equipment.model}"] -= count
                self.total_cost -= float(equipment.price)
                self.count_of_officeequipment -= int(count)
            department.get_equipment(equipment, count)
        except NoEqupmentError:
            print(f'Недостаточно {equipment.brand} {equipment.model} на складе для перемещения')
        except:
            print('Не могу переместить объект')

    @staticmethod
    def _validator_for_int(count):
        if not isinstance(count, int):
            raise ValueError('count must be "int"')
        return count


class OfficeEquipment:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price


class Printer(OfficeEquipment):
    def __init__(self, brand, model, price, cartridge, count_of_paper, color):
        super().__init__(brand, model, price)
        self.cartridge = cartridge
        self.count_of_paper = count_of_paper
        self.color = color


class Skaner(OfficeEquipment):
    def __init__(self, brand, model, price, format_a4):
        super().__init__(brand, model, price)
        self.format_a4 = format_a4


class Xerox(OfficeEquipment):
    def __init__(self, brand, model, price, format_a4, color):
        super().__init__(brand, model, price)
        self.format_a4 = format_a4
        self.color = color


sklad_01 = Storage()
off_01 = Xerox('Xerox', 'M21', '12300', 'A4', True)
off_02 = Xerox('HP', '1245', '3300', 'A3', True)
off_03 = Xerox('Xerox', 'M21', '12300', 'A4', True)

sklad_01.get_equipment(off_01, 2)
sklad_01.get_equipment(off_01, 2)
sklad_01.get_equipment(off_02, 2)
print(sklad_01.all_models)
print(sklad_01.count_of_officeequipment)
print(sklad_01.total_cost)

sklad_02 = Storage()
sklad_01.send_equipment(off_01, 2, sklad_02)
print(sklad_01.all_models)

sklad_01.send_equipment(off_02, 3, sklad_02)
print(sklad_02.all_models)
print(sklad_01.all_models)
print(sklad_02.count_of_officeequipment)
print(sklad_01.count_of_officeequipment)
