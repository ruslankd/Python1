def my_sum_list():
    my_sum = 0
    while True:
        my_str = input("Введите числа (через пробел): ")
        my_list = my_str.split(" ")
        for i in my_list:
            if i == "q":
                print(f"Итоговая сумма: {my_sum}")
                return
            my_sum += float(i)
        print(f"Промежуточная сумма: {my_sum}")


try:
    my_sum_list()
except ValueError as err:
    print(err)
