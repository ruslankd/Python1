from sys import argv

try:
    _, work_in_hours, rate_in_hours, bonus = argv
    print(f"Зарплата = {float(work_in_hours) * float(rate_in_hours) + float(bonus)}")
except Exception:
    print("Введите 3 числовых аргумента!")