my_list = [7, 4, 3, 2, 1, 1]
print(my_list)

end_word = ""
while 1:
    input_sym = input("Введите рейтинг (q - для выхода): ")
    if input_sym == "q":
        break
    n = int(input_sym)
    last_pos = 0
    for i, rating in enumerate(my_list):
        if rating >= n:
            last_pos = i + 1
    my_list.insert(last_pos, n)
    print(f"{my_list} (на {last_pos} позиции)")
