my_list = []

n = int(input("Введите кол-во элементов списка: "))
if n <= 0:
    quit()

print("Введите элементы: ")
for i in range(0, n):
    element = input(f"{i + 1}: ")
    my_list.append(element)

print(f"Список: {my_list}")

i = 0
counter = len(my_list) // 2 * 2
while i < counter:
    temp = my_list[i]
    my_list[i] = my_list[i + 1]
    my_list[i + 1] = temp
    i += 2

print(f"Преобразованный список: {my_list}")
