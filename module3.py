winter_list = [1, 2, 12]
spring_list = [3, 4, 5]
summer_list = [6, 7, 8]
autumn_list = [9, 10, 11]

my_dict = {
    1: "Зима", 2: "Зима", 12: "Зима",
    3: "Весна", 4: "Весна", 5: "Весна",
    6: "Лето", 7: "Лето", 8: "Лето",
    9: "Осень", 10: "Осень", 11: "Осень"
}

n = int(input("Введите номер месяца: "))

if n in winter_list:
    print("Зима")
elif n in spring_list:
    print("Весна")
elif n in summer_list:
    print("Лето")
elif n in autumn_list:
    print("Осень")

print(f"Из словаря: {my_dict.get(n)}")
