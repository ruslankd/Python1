class Cell:
    def __init__(self, count):
        if not type(count) is int:
            raise TypeError("Кол-во ячеек - целое число")
        self.count = count

    def __add__(self, other):
        return Cell(self.count + other.count)

    def __sub__(self, other):
        if self.count < other.count:
            raise Exception("Вычитание невозможно!")
        else:
            return Cell(self.count - other.count)

    def __mul__(self, other):
        return Cell(self.count * other.count)

    def __truediv__(self, other):
        return Cell(self.count // other.count)

    def __str__(self):
        return f"клетка - ({self.count})"

    def make_order(self, n):
        output_string = ""
        for i in range(0, self.count // n):
            for j in range(0, n):
                output_string += '*'
            output_string += '\n'
        for i in range(0, self.count % n):
            output_string += '*'
        return output_string


cell1 = Cell(17)
cell2 = Cell(5)
print(cell1)
print(cell2)
print(f"Сложение: {cell1 + cell2}")
print(f"Вычитание: {cell1 - cell2}")
print(f"Умножение: {cell1 * cell2}")
print(f"Деление: {cell1 / cell2}")
print(cell1.make_order(6))
