# 1. Реализовать класс Matrix (матрица).
# Обеспечить перегрузку конструктора класса (метод __init__()),
# должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix.
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
# с первым элементом первой строки второй матрицы и т.д.


class Matrix():
    def __init__(self, my_arg):
        self.my_lists = my_arg

    def __getitem__(self, index):
        self.index = index
        return self.matrix[index]

    def __str__(self):
        return f"{self.my_lists[0]}\n{self.my_lists[1]}\n{self.my_lists[2]}"

    def __len__(self):
        return len(self.my_lists)

    def __add__(self, my_add_list2):
        self.my_matrix2 = my_add_list2
        new_matrix = []


        for my_str in range(len(self.my_lists)):
            new_str = []
            for el in range(len(self.my_lists)):
                new_str.append( self.my_matrix2[my_str][el] + self.my_lists[my_str][el])
            new_matrix.append(new_str)
            new = Matrix(new_matrix)
        return  new

my_list2 = [[50, 12, 63], [91, 55, 12], [23, 10, 12]]
my_list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
my_matrix2 = Matrix(my_list2)
my_matrix1 = Matrix(my_list1)
print(('Матрица №1 :'))
print(my_matrix1)
print(('Матрица №2 :'))
print(my_matrix2)

print('Новая матрица, образованная путем сложения первых двух : ')
new = (my_matrix1.__add__(my_list2))

print(new)


# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название. clothes
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто coat ) и рост (для костюма suit).
# Это могут быть обычные числа: V (size)и H (height), соответственно.
# Для определения расхода (expenditure) ткани  формула: для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта.
# Проверить на практике работу декоратора @property.


# Читаю , смотрю, вроде понимаю декораторы, но не могу на практике им место найти.

class Clothes():

    def __init__(self, title):
        self.title = title

class Coat(Clothes):

    def __init__(self, size):
        self.size = size
        super(Coat, self).__init__(size)

    def expenditure(self):
        ''' Расчет расхода ткани на пальто, принимает аргумент size (размер)
            Возвращает количество ткани на пальто.
        '''
        expenditure = round((self.size / 6.5 + 0.5),2)
        print('На ваше пальто потребуется {} метров ткани '.format(expenditure))


class Suit(Clothes):
    def __init__(self, height):
        self.height = height
        super().__init__(height)

    def expenditure(self):
        ''' Расчет расхода ткани на костюм, принимает аргумент size (размер)
            Возвращает количество ткани на костюм.
        '''
        expenditure = round((2 * self.height + 0.3), 2)
        print('На ваш костюм потребуется {} метров ткани '.format(expenditure))


my_suit = Suit(54)
my_coat = Coat(175)
my_suit.expenditure()
my_coat.expenditure()
