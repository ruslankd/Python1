try:
    with open("my_file.txt", "r") as my_file:
        for line in my_file.readlines():
            my_list = line.split(" ")
            print(len(my_list))
except IOError:
    print("Ошибка ввода-вывода!")
