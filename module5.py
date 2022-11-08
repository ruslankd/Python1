from random import randint

try:
    with open("file_5.txt", "w+") as my_file:
        my_list = [str(randint(-100, 100)) for i in range(0, randint(5, 15))]
        my_file.write(" ".join(my_list))
        my_file.seek(0)
        new_list = {int(i) for i in my_file.readline().split(" ")}
        print(sum(new_list))
except IOError:
    print("Ошибка ввода-вывода!")
