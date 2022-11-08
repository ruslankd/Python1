import json

try:
    with open("file_7.txt", encoding="utf-8", mode="r") as my_file:
        start_list = [line.split(" ") for line in my_file.readlines()]
        firm_dict = {}
        sum_profit = 0
        count_profit = 0
        for i in start_list:
            revenue = int(i[2])
            cost = int(i[3])
            firm_dict[i[0]] = revenue - cost
            if revenue > cost:
                sum_profit += firm_dict[i[0]]
                count_profit += 1
        end_list = [firm_dict, {"average_profit": int(sum_profit / count_profit)}]
        with open("end_file_7.json", encoding="utf-8", mode="w") as json_file:
            json.dump(end_list, json_file, ensure_ascii=False)
except IOError:
    print("Ошибка ввода-вывода!")
except ValueError:
    print("Некорректные данные!")