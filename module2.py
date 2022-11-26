class MyZeroDivisionError(Exception):
    def __init__(self, txt):
        self.txt = txt


try:
    a = float(input("a = "))
    b = float(input("b = "))
    if b == 0.0:
        raise MyZeroDivisionError("На ноль делить нельзя!")
except MyZeroDivisionError as err:
    print(err)
except ValueError:
    print("Введите числа!")
else:
    print(f"Результат - {a / b}")
finally:
    print("Программа завершена")
