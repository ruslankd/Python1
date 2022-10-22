from itertools import count
from sys import argv

try:
    _, start_number, counter = argv
    for i in count(int(start_number)):
        if i > int(counter):
            break
        else:
            print(i)
except Exception:
    print("Введите два аргумента:\n"
          "Первый - стартовое целое число\n"
          "Второй - финишное целое число")
