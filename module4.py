def my_func(x, y):
    abs_y = abs(y)
    new_x = x
    for i in range(0, abs_y - 1):
        new_x *= x
    return 1 / new_x


try:
    x = float(input("Введите х (действительное положительное): "))
    if x < 0:
        print("x - положительное")
        exit()
    y = int(input("Ведите у (целое отрицательное): "))
    if y >= 0:
        print("y - отрицательное")
        exit()
    print(f"x ^ y = {my_func(x, y)}")
except ValueError:
    print("Неверный формат данных!")
