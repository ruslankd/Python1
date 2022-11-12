class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"{self.color} {self.name} поехала")

    def stop(self):
        print(f"{self.color} {self.name} остановилась")
        self.speed = 0

    def turn(self, degrees):
        print(f"{self.color} {self.name} повернула на {degrees} градусов")

    def show_speed(self):
        if self.speed == 0:
            print(f"{self.color} {self.name} не движется")
        else:
            print(f"{self.color} {self.name} движется со скоростью {self.speed}")


class SportCar(Car):
    pass


class PoliceCar(Car):
    pass


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print(f"{self.color} {self.name} превышает скорость")


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print(f"{self.color} {self.name} превышает скорость")


try:
    sport_car = SportCar(120, "Красная", "Ferrari", False)
    sport_car.go()
    sport_car.show_speed()
    sport_car.turn(45)
    sport_car.stop()

    police_car = PoliceCar(96, "Белая", "Granta", True)
    print(f"{police_car.color} {police_car.name} полицейская - {police_car.is_police}")
    police_car.go()
    police_car.turn(90)
    police_car.show_speed()
    police_car.turn(-90)
    police_car.stop()
    police_car.show_speed()

    town_car = TownCar(72, "Синий", "Ford", False)
    town_car.go()
    town_car.show_speed()
    town_car.stop()

    work_car = WorkCar(43, "Желтый", "Белаз", False)
    work_car.go()
    work_car.show_speed()
    work_car.turn(-80)
    work_car.stop()
except Exception as err:
    print(err)
