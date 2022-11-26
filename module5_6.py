from abc import ABC


class Stock:
    def __init__(self, name):
        self.name = name
        self.__stock_dict = {}

    def __str__(self):
        return f"Склад '{self.name}':\n{self.__stock_dict}\n"

    def add_office_equipment(self, office_equipment, count):
        current_count = self.__stock_dict.get(office_equipment.name)
        try:
            if current_count is None:
                self.__stock_dict[office_equipment.name] = int(count)
            else:
                self.__stock_dict[office_equipment.name] = current_count + int(count)
        except ValueError:
            print("Невалидное кол-во техники")

    def send_in_subdivision(self, office_equipment, subdivision, count):
        try:
            print(
                f"Передача {int(count)} {office_equipment.name} из склада '{self.name}' в подразделение '{subdivision.name}'..."
            )
            current_count_in_stock = 0 if self.__stock_dict.get(office_equipment.name) is None \
                else self.__stock_dict[office_equipment.name]
            if current_count_in_stock == 0:
                print("Передача техники невозможна: отсутствует на складе")
            elif current_count_in_stock < int(count):
                print("Передача техники невозможна: недостаточно на складе")
            else:
                current_count_in_subdivision = subdivision.things.get(office_equipment.name)
                if current_count_in_subdivision is None:
                    subdivision.things[office_equipment.name] = int(count)
                else:
                    subdivision.things[office_equipment.name] = current_count_in_subdivision + int(count)
                if current_count_in_stock - int(count) == 0:
                    del self.__stock_dict[office_equipment.name]
                else:
                    self.__stock_dict[office_equipment.name] = current_count_in_stock - int(count)
        except ValueError:
            print("Невалидное кол-во техники")


class Subdivision:
    def __init__(self, name):
        self.name = name
        self.things = {}

    def __str__(self):
        return f"Подразделение '{self.name}', имущество: {self.things}"


class OfficeEquipment(ABC):
    def __init__(self, name):
        self.name = name


class Printer(OfficeEquipment):
    def __init__(self, name, is_color):
        super().__init__(name)
        self.is_color = is_color

    def __str__(self):
        return_str = f"Принтер: {self.name} "
        return_str += "(цветная печать)" if self.is_color else "(черно-белая печать)"
        return return_str


class Scanner(OfficeEquipment):
    def __init__(self, name, resolution):
        super().__init__(name)
        self.resolution = resolution

    def __str__(self):
        return f"Сканер: {self.name} (разрешение - {self.resolution})"


class Xerox(OfficeEquipment):
    def __init__(self, name, is_two_side):
        super().__init__(name)
        self.is_two_side = is_two_side

    def __str__(self):
        return_str = f"Ксерокс: {self.name} "
        return_str += "(двусторонний)" if self.is_two_side else "(односторонний)"
        return return_str


printer = Printer("Pantum", False)
scanner = Scanner("Epson", "1000x1000")
xerox = Xerox("Xerox", True)
stock = Stock("Оргтехника")
stock.add_office_equipment(scanner, 3)
stock.add_office_equipment(printer, 5)
stock.add_office_equipment(printer, 1)
print(stock)
subdivision = Subdivision("Бухгалтерия")
stock.send_in_subdivision(printer, subdivision, 5)
print(stock)
print(subdivision)
