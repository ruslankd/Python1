def fact(n):
    if n == 0:
        yield 1
    else:
        s = 1
        for i in range(1, n + 1):
            s *= i
            yield s


try:
    n = int(input("n = "))
    if n < 0:
        raise Exception
    for el in fact(n):
        print(el)
except Exception:
    print("Введите целое число >= 0")
