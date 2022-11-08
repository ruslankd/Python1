try:
    with open("my_file.txt", "r") as my_file:
        my_list = [(line.strip().split(" ")[0], float((line.strip().split(" ")[1]))) for line in my_file.readlines()]
        print("Оклад меньше 20000:")
        sum_salary = 0
        for surname, salary in my_list:
            sum_salary += salary
            if salary < 20000:
                print(surname)
        print(f"Средний оклад - {(sum_salary / len(my_list)):.2f}")
except ValueError:
    print("Некорректные значения!")
except IOError:
    print("Ошибка ввода-вывода!")
