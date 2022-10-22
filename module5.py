from functools import reduce

my_list = [i for i in range(100, 1001) if i % 2 == 0]
print(reduce((lambda el1, el2: el1 * el2), my_list))
