class Triangle:
    def __init__(self, x, y, a, b, c):
        self.x = x
        self.y = y
        self.a = a
        self.b = b
        self.c = c

    def display_triangle(self):
        return str(f'Triangle({self.x},{self.y},{self.a},{self.b},{self.c})')


triangle_1 = Triangle(1, 2, 3, 4, 5)
print(triangle_1.display_triangle())
