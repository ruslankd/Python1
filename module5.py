class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f"{self.title}: отрисовка")


class Pen(Stationery):
    def draw(self):
        print(f"{self.title}: роспись")


class Pencil(Stationery):
    def draw(self):
        print(f"{self.title}: раскраска")


class Handle(Stationery):
    def draw(self):
        print(f"{self.title}: выделение")


stationery = Stationery("HappyColor")
stationery.draw()
pen = Pen("Паркер")
pen.draw()
pencil = Pencil("Dino")
pencil.draw()
handle = Handle("Chalk")
handle.draw()
