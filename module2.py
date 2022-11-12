class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculate_mass(self, mas_in_meter, thickness):
        return self._length * self._width * mas_in_meter * thickness / 1000


road = Road(5000, 20)
print(f"{road.calculate_mass(25, 5)} тонн")