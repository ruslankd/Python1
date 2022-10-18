def print_person_info(
        name="Ivan",
        surname="Ivanov",
        birthday="01.01.2000",
        city="Moscow",
        email="iivanov@mail.ru",
        phone="+79991112233"
):
    print(f"{surname} {name}, {birthday}, {city}, {email}, {phone}")


print_person_info()
print_person_info(name="Vasya", city="St. Petersburg")
