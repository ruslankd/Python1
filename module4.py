try:
    with open("dict.txt", "r") as dict_file:
        my_dict = {line.strip().split(" - ")[0].lower(): line.strip().split(" - ")[1]
                   for line in dict_file.readlines()}
        with open("start_file.txt", "r") as start_file:
            with open("end_file.txt", "w") as end_file:
                for line in start_file.readlines():
                    my_line = line.split(" ")
                    for dict_key in my_dict.keys():
                        my_line = [word.lower().replace(dict_key, my_dict.get(dict_key)) for word in my_line]
                    end_file.write(f"{' '.join(my_line)}")
except IOError:
    print("Ошибка ввода-вывода!")
