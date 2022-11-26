from abc import ABC


class Stock:
    def __init__(self, name):
        self.name = name


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
print(printer)
print(scanner)
print(xerox)
