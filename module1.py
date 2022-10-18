def my_division(a, b):
    res = float()
    try:
        res = float(a) / float(b)
        return res
    except ZeroDivisionError:
        print("Деление на ноль!")
    except ValueError:
        print("Введите числа!")


a = input("а: ")
b = input("b: ")
print(f"a / b = {my_division(a, b)}")
