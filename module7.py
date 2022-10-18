def int_func(word):
    return str(word).title()


input_string = input("Введите строку: ")
word_list = []
for word in input_string.split(" "):
    word_list.append(int_func(word))
print(" ".join(word_list))
