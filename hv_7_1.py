"""1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
принимать данные (список списков) для формирования матрицы. Подсказка: матрица — система некоторых математических
величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
(двух матриц). Результатом сложения должна быть новая матрица. Подсказка: сложение элементов матриц выполнять
поэлементно — первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй
матрицы и т.д."""


class Matrix:

    def __init__(self, content):
        self.content = content

    def __str__(self):
        for element in self.content:
            print(" ".join([str(i) for i in element]))

    def __add__(self, other):
        if len(self.content) == len(other.content):
            general_res_matrix_list = [[] for _ in range(len(self.content))]
            for el in range(len(general_res_matrix_list)):
                if len(self.content[el]) == len(other.content[el]):
                    local_res_matrix_list = [self.content[el][i] + other.content[el][i] for i in
                                             range(len(self.content[el]))]
                    general_res_matrix_list[el] = local_res_matrix_list
                else:
                    print("Размеры локальных списков не совпадают!")
            return Matrix(general_res_matrix_list)
        else:
            print("Размеры складываемых матриц не совпадают")


matrix_list_1 = Matrix([[1, 3], [2, 5], [3, 2]])
matrix_list_2 = Matrix([[2, 4], [3, 6], [4, 3]])



c = matrix_list_1.__add__(matrix_list_2)

c.__str__()
