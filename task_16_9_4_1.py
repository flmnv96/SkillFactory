class Volunteer:
    def __init__(self, p1, p2, p3, p4):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4

    def __str__(self):
        return f'"{self.p1} {self.p2}, г.{self.p3}, статус "{self.p4}"'
