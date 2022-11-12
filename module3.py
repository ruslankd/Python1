class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def get_full_name(self):
        return f"{self.surname} {self.name}"

    def get_total_income(self):
        return self._income.get("wage") + self._income.get("bonus")


try:
    worker = Position("Василий", "Петров", "Инженер", {"wage": 12500, "bonus": 4300})
    print(f"Полное имя - {worker.get_full_name()}, должность - {worker.position}, доход - {worker.get_total_income()}")

    worker = Position("Иван", "Сидоров", "Программист", {"wage": 15700, "bonus": 5800})
    print(f"Полное имя - {worker.get_full_name()}, должность - {worker.position}, доход - {worker.get_total_income()}")
except Exception as err:
    print(err)
