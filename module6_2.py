from itertools import cycle
from sys import argv

try:
    my_list = [1, 2, 3]
    _, counter = argv
    if int(counter) < 0:
        print("Введите один аргумент: натуральное число (кол-во повторений)")
    c = 0
    for i in cycle(my_list):
        if c >= (len(my_list) * int(counter)):
            break
        print(i)
        c += 1
except Exception:
    print("Введите один аргумент: натуральное число (кол-во повторений)")