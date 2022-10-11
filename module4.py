n = int(input("Введите число: "))
max_digit = 0
while 1:
    if n % 10 >= max_digit:
        max_digit = n % 10
    n = n // 10
    if n == 0:
        break
print("Максимальная цифра: ", max_digit)
