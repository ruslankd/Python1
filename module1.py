print("Запись в файл (выход - пустая строка):")
try:
    with open("my_file.txt", "w") as my_file:
        while True:
            s = input()
            if s == "":
                break
            my_file.write(f"{s}\n")
except IOError:
    print("Ошибка ввода-вывода!")
