revenue = float(input("Введите значение выручки: "))
cost = float(input("Введите значение издержек: "))
if revenue > cost:
    print("Вы работаете прибыльно")
    print("Рентабельность = ", (revenue - cost) / revenue)
    number = int(input("Введите кол-во сотрудников: "))
    print("Прибыль на одного сотрудника: ", (revenue - cost) / number)
elif revenue < cost:
    print("Вы работаете убыточно")
else:
    print("Вы работаете в ноль")