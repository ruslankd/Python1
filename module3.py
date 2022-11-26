class NotNumberError(Exception):
    def __init__(self, txt):
        self.txt = txt


class NumbersList:
    def __init__(self):
        self.numbers = []

    def add(self, n):
        if n.isdigit():
            self.numbers.append(int(n))
        else:
            try:
                self.numbers.append(float(n))
            except ValueError:
                raise NotNumberError("Необходимо ввести число!")


print("Ввод чисел (stop - для завершения)...")
number_list = NumbersList()
while True:
    input_number = input("Число: ")
    if input_number == "stop":
        break
    try:
        number_list.add(input_number)
    except NotNumberError as err:
        print(err)
print(number_list.numbers)
