import math

# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

class Triangle:
    def __init__(self, dot_1_x, dot_1_y, dot_2_x, dot_2_y, dot_3_x, dot_3_y):
        self.dot_1_x = dot_1_x
        self.dot_1_y = dot_1_y
        self.dot_2_x = dot_2_x
        self.dot_2_y = dot_2_y
        self.dot_3_x = dot_3_x
        self.dot_3_y = dot_3_y

    def square(self):
        segment_1 = ((self.dot_2_x - self.dot_1_x)**2+(self.dot_2_y - self.dot_1_y)**2)**0.5
        segment_2 = ((self.dot_3_x - self.dot_2_x) ** 2 + (self.dot_3_y - self.dot_2_y) ** 2) ** 0.5
        segment_3 = ((self.dot_3_x - self.dot_1_x) ** 2 + (self.dot_3_y - self.dot_1_y) ** 2) ** 0.5
        p = (segment_1 + segment_2 + segment_3)/2
        square = (p * (p - segment_1) * (p - segment_2) * (p - segment_3))**0.5
        print(square)

    def high(self):
        segment_1 = ((self.dot_2_x - self.dot_1_x) ** 2 + (self.dot_2_y - self.dot_1_y) ** 2) ** 0.5
        segment_2 = ((self.dot_3_x - self.dot_2_x) ** 2 + (self.dot_3_y - self.dot_2_y) ** 2) ** 0.5
        segment_3 = ((self.dot_3_x - self.dot_1_x) ** 2 + (self.dot_3_y - self.dot_1_y) ** 2) ** 0.5
        p = (segment_1 + segment_2 + segment_3) / 2
        h = (2/segment_1) * (p * (p - segment_1) * (p - segment_2) * (p - segment_3)) ** 0.5
        print(h)

    def perimetr(self):
        segment_1 = ((self.dot_2_x - self.dot_1_x) ** 2 + (self.dot_2_y - self.dot_1_y) ** 2) ** 0.5
        segment_2 = ((self.dot_3_x - self.dot_2_x) ** 2 + (self.dot_3_y - self.dot_2_y) ** 2) ** 0.5
        segment_3 = ((self.dot_3_x - self.dot_1_x) ** 2 + (self.dot_3_y - self.dot_1_y) ** 2) ** 0.5
        perimetr = segment_1 + segment_2 + segment_3
        print(perimetr)

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class trapezoid:
    def __init__(self, dot_1_x, dot_1_y, dot_2_x, dot_2_y, dot_3_x, dot_3_y, dot_4_x, dot_4_y):
        self.dot_1_x = dot_1_x
        self.dot_1_y = dot_1_y
        self.dot_2_x = dot_2_x
        self.dot_2_y = dot_2_y
        self.dot_3_x = dot_3_x
        self.dot_3_y = dot_3_y
        self.dot_4_x = dot_4_x
        self.dot_4_y = dot_4_y

    # def segment(self, x_1, y_1, x_2, y_2):
    #     len = ((x_2 - x_1) ** 2 + ((y_2 - y_1)) ** 2) ** 0.5
    #     return len

    def check_trapezoid(self):
        diagonal_1 = ((self.dot_3_x - self.dot_1_x) ** 2 + (self.dot_3_y - self.dot_1_y) ** 2) ** 0.5
        diagonal_2 = ((self.dot_4_x - self.dot_2_x) ** 2 + (self.dot_4_y - self.dot_2_y) ** 2) ** 0.5
        if diagonal_1 == diagonal_2:
            print('Trapezia ravnobochaya')
        else:
            print('Trapezia neravnobochaya')

    def perimetr(self):
        segment_1 = ((self.dot_2_x - self.dot_1_x) ** 2 + ((self.dot_2_y - self.dot_1_y)) ** 2) ** 0.5
        segment_2 = ((self.dot_3_x - self.dot_2_x) ** 2 + ((self.dot_3_y - self.dot_2_y)) ** 2) ** 0.5
        segment_3 = ((self.dot_4_x - self.dot_3_x) ** 2 + ((self.dot_4_y - self.dot_3_y)) ** 2) ** 0.5
        segment_4 = ((self.dot_4_x - self.dot_1_x) ** 2 + ((self.dot_4_y - self.dot_1_y)) ** 2) ** 0.5
        perimetr = segment_1 + segment_2 + segment_3 + segment_4
        print(perimetr)

    def square(self):
        a = ((self.dot_3_x - self.dot_2_x) ** 2 + ((self.dot_3_y - self.dot_2_y)) ** 2) ** 0.5
        b = ((self.dot_4_x - self.dot_1_x) ** 2 + ((self.dot_4_y - self.dot_1_y)) ** 2) ** 0.5
        h = self.dot_2_y - self.dot_1_y
        square = 0.5 * h * (a + b)
        print(square)

    def len(self):
        len_1 = ((self.dot_2_x - self.dot_1_x) ** 2 + (self.dot_2_y - self.dot_1_y) ** 2) ** 0.5
        len_2 = ((self.dot_3_x - self.dot_2_x) ** 2 + (self.dot_3_y - self.dot_2_y) ** 2) ** 0.5
        len_3 = ((self.dot_4_x - self.dot_3_x) ** 2 + (self.dot_4_y - self.dot_3_y) ** 2) ** 0.5
        len_4 = ((self.dot_4_x - self.dot_1_x) ** 2 + (self.dot_4_y - self.dot_1_y) ** 2) ** 0.5
        print(len_1, ',', len_2, ',', len_3, ',', len_4)

if __name__ == '__main__':

    figure = Triangle(5, 3, 8, 3, 8, 6)

    figure.square()
    figure.high()
    figure.perimetr()

    figure = trapezoid(1, 4, 2, 6, 4, 6, 5, 4)

    figure.check_trapezoid()
    figure.perimetr()
    figure.square()
    figure.len()
