import json

products_list = []
analytics_dict = {}

while 1:
    print("1. Добавить товар\n"
          "2. Аналитика\n"
          "3. Выход")
    menu_item = input("Ввод: ")

    if menu_item == "1":
        name = input("Название: ")
        price = int(input("Цена: "))
        count = int(input("Кол-во: "))
        measurement = input("Единицы: ")
        products_list.append((
            len(products_list) + 1,
            {
                "название": name,
                "цена": price,
                "количество": count,
                "ед": measurement
            }
        ))
    elif menu_item == "2":
        for i in products_list[0][1].keys():
            temp_list = []
            for j in products_list:
                temp_list.append(j[1].get(i))
            analytics_dict[i] = temp_list
        print(json.dumps(analytics_dict, indent=4, ensure_ascii=False))
    elif menu_item == "3":
        break

