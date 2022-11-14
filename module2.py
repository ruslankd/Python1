from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def sum_cloth(self):
        pass


class Coat(Clothes):
    def __init__(self, name, v):
        self.name = name
        self.v = v

    @property
    def sum_cloth(self):
        return self.v / 6.5 + 0.5


class Costume(Clothes):
    def __init__(self, h):
        self.h = h

    @property
    def sum_cloth(self):
        return self.h * 2 + 0.3


coat = Coat("aaa", 32)
print(coat.sum_cloth)
costume = Costume(1.7)
print(costume.sum_cloth)
