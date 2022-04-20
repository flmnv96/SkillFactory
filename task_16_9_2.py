import math


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def rectangle_area(self):
        return self.width * self.height


rectangle_1 = Rectangle(16, 28)

print("Длинна прямоугольника равна: ", rectangle_1.width)
print("Высота прямоугольника равна: ", rectangle_1.height)
print("Площадь прямоугольника равна: ", rectangle_1.rectangle_area())


class Trapezoid:
    def __init__(self, a, b, c, d):

        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def trapezoid_display(self):
        return str(f'Трапеция(сторона a = {self.a}, сторона b = {self.b}, сторона c = {self.c}, сторона d = {self.d})')

    def trapezoid_area(self):
        return (self.a + self.b) / 2 * math.sqrt(self.c ** 2 - ((self.b - self.a) ** 2 + self.c ** 2 - self.d ** 2)
                                                 / (2 * (self.b - self.a))) ** 2


trapezoid_1 = Trapezoid(4, 6, 5, 7)

print(trapezoid_1.trapezoid_display())
print("Площадь трапеции =", int(trapezoid_1.trapezoid_area()))
