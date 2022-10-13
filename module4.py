input_str = input("Введите строку: ")

word_list = input_str.split(" ")
for i, word in enumerate(word_list):
    print(f"{i + 1}) {word[0:10]}")
