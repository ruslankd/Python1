start_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [start_list[i] for i in range(1, len(start_list)) if start_list[i] > start_list[i - 1]]
print(new_list)
