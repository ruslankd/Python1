try:
    with open("file_6.txt", encoding="utf-8", mode="r") as my_file:
        my_dict = {}
        for line in my_file.readlines():
            words = line.split(" ")
            hour_sum = 0
            for j in range(1, len(words)):
                if words[j] == "-":
                    continue
                hour_sum += int(words[j].split("(")[0])
            my_dict[words[0][0:-1]] = hour_sum
        print(my_dict)
except IOError:
    print("Ошибка ввода-вывода!")
