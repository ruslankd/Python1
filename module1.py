from tabulate import tabulate


class Matrix:
    def __init__(self, table):
        if not type(table) is list:
            raise TypeError("объект не является списком")
        line_length = len(table[0])
        for line in table:
            if not type(line) is list:
                raise TypeError("не все элементы являются списком")
            if len(line) != line_length:
                raise Exception("объект не является матрицей")
        self.table = table

    def __str__(self):
        return tabulate(self.table, tablefmt="plain")

    def __add__(self, other):
        sum_list = []
        if len(self.table) != len(other.table):
            raise Exception("Разная размерность матриц для сложения")
        for i in range(0, len(self.table)):
            if len(self.table[i]) != len(other.table[i]):
                raise Exception("Разная размерность матриц для сложения")
            temp_list = []
            for j in range(0, len(self.table[i])):
                temp_list.append(self.table[i][j] + other.table[i][j])
            sum_list.append(temp_list)
        return Matrix(sum_list)


matrix1 = Matrix([[1, -2], [-3, 4]])
matrix2 = Matrix([[4, 3], [7, -2]])
print(f"{matrix1}\n")
print(f"{matrix2}\n")
print(matrix1 + matrix2)
