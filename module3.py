def my_func(a, b, c):
    return a + b + c - min(a, b, c)


try:
    a, b, c = float(input("a: ")), float(input("b: ")), float(input("c: "))
    print(my_func(a, b, c))
except ValueError:
    print("Введите числа!")
